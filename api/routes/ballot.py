from datetime import datetime
from flask import Blueprint, render_template, session, redirect, url_for, flash, request, jsonify
from mongoDB.config.connection_db import get_database
from bson.objectid import ObjectId  # Pour gérer les ObjectId
from utils.decorators import login_required
from utils.enums import TypeVote
from utils.voting_logic import handle_majority_vote, handle_condorcet_vote, handle_proportional_vote


ballot_bp = Blueprint('ballot', __name__, template_folder='templates')

db = get_database()
users_collection = db["Users"]
ballot_collection = db["Ballots"]


@ballot_bp.route('/create_ballot_form', methods=['GET'])
@login_required
def create_ballot_form():
    """
    Affiche le formulaire pour créer un scrutin.
    """
    return render_template('ballot_form.html')

@ballot_bp.route('/create_ballot', methods=['POST'])
@login_required
def create_ballot():
    """
    Route pour creer un scrutin.
    Ici, on aurait pu récupérer le pseudo, car il est unique. 
    Mais j'ai préféré récupérer l'ID
    Traite la soumission du formulaire et crée un scrutin.
    
    """
    try:
        # récuperer les donnees du formulaire
        name_poll = request.form.get('name_poll')
        poll_question = request.form.get('poll_question')
        poll_text = request.form.get('poll_text')
        poll_response = [response.strip() for response in request.form.getlist('poll_response') if response.strip()] #pour supprimer les espaces
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        type_vote = request.form.get('type_vote')
        created_by = session.get('user_id')
        
        # validation des données
        
        if not name_poll or not poll_question or not poll_text:
            return jsonify({'error': 'Tous les champs obligatoire doivent être remplit'}), 400
        
        if len(poll_response) < 2:
            return jsonify({'error': 'Le scrutin doit contenir au moins deux réponses possible'}), 400
        
        if not start_date or not end_date:
            return jsonify({'error': 'Les dates de début et de fin sont obligatoires'}), 400
        
        if datetime.strptime(end_date, '%Y-%m-%d') <= datetime.strptime(start_date, '%Y-%m-%d'):
            return jsonify({'error': 'La date de fin doit être postérieure à la date de début.'}), 400
        
        if type_vote not in [tv.value for tv in TypeVote]:
            return jsonify({"error" : "Type de vote invalide." }), 400
        
        #determine la date du scrutin
        date_ballot = datetime.now()
        if date_ballot < datetime.strptime(start_date, '%Y-%m-%d'): # si date_ballot est inferieur a la date de creation du scrutin alors il est ferme
            status = "Closed"  
        elif date_ballot > datetime.strptime(end_date, '%Y-%m-%d'): # si date_ballot est superieur a la date de fin du scrutin alors il est ferme
            status = "Closed"  
        else:
            status = "active"  # Entre les deux dates
        
        # dictonnaire qui contient les donnees du scrutin qu'on va push
        ballot_data = {
            "name_poll": name_poll,
            "poll_question": poll_question,
            "poll_text": poll_text,
            "poll_response": poll_response,
            "created_by": str(ObjectId(created_by)),  
            "participants": [],  
            "status": status,  
            "start_date": start_date,
            "end_date": end_date,
            "type_vote":type_vote
        }
        
        ballot_id = ballot_collection.insert_one(ballot_data).inserted_id
        
        users_collection.update_one(
            {'_id': ObjectId(created_by)},
            {"$push": {"creations_polls": str(ballot_id)}}
        )
        
        ballot_data['_id'] = str(ballot_id)
        ballot_data['created_by'] = str(ballot_data['created_by'])
        
        #
        flash("Scrutin créé avec succès!", "success")
        #return jsonify({'message': 'Scrutin créé avec succès.', 'ballot': ballot_data}), 201
        return redirect(url_for('ballot.view_ballots', filter='latest'))  

    
    
    except Exception as e:
            # Gestion des erreurs
            return jsonify({'error': str(e)}), 500   


# @ballot_bp.route('/latest_ballots', methods=['GET'])
# def latest_ballots():
#     """
#     Route pour récupérer les 10 derniers scrutins créés et les afficher sur une page.
#     """
#     latest_ballots = list(ballot_collection.find().sort("start_date", -1).limit(10))
    
#     # Convertir les ObjectId en chaînes de caractères
#     for ballot in latest_ballots:
#         ballot["_id"] = str(ballot["_id"])
    
#     # Passer les scrutins au template
#     return render_template('home_scrutin.html', latest_ballots=latest_ballots)

# @ballot_bp.route('/active_ballots', methods=['GET'])
# def active_ballots():
#     """
#     Route pour récupérer les 10 derniers scrutins actifs et les afficher sur une page.
#     """
#     active_ballots = list(ballot_collection.find({"status": "active"}).sort("start_date", -1).limit(10))
    
#     # Convertir les ObjectId en chaînes de caractères
#     for ballot in active_ballots:
#         ballot["_id"] = str(ballot["_id"])
    
#     # Passer les scrutins au template
#     return render_template('home_scrutin.html', active_ballots=active_ballots)

@ballot_bp.route('/view_ballots', methods=['GET'])
def view_ballots():
    """
    Route pour afficher la liste des scrutins avec des filtres.
    """
    filter_type = request.args.get('filter', 'latest')  # Par défaut : derniers scrutins créés
    type_vote = request.args.get('type_vote', 'all')  # Par défaut : tous les types

    # Construire la requête MongoDB
    query = {}
    if filter_type == 'active':
        query["status"] = "active"  # Scrutins actifs
    if type_vote != 'all':
        query["type_vote"] = type_vote  # Filtrer par type de vote si sélectionné

    # Récupérer les scrutins correspondant
    ballots = list(ballot_collection.find(query).sort("start_date", -1).limit(10))
    
    # Convertir les ObjectId en chaînes de caractères
    for ballot in ballots:
        ballot["_id"] = str(ballot["_id"])
    
    return render_template(
        'view_ballots.html',
        ballots=ballots,
        filter_type=filter_type,
        type_vote=type_vote
    )

@ballot_bp.route('/edit_ballot/<ballot_id>', methods=['GET', 'POST'])
@login_required
def edit_ballot(ballot_id):
    """
    Permet de modifier un scrutin existant tant qu'il n'est pas encore ouvert.
    Les options ne peuvent pas être modifiées.
    """
    try:
        # Récupération du scrutin à modifier
        ballot = ballot_collection.find_one({"_id": ObjectId(ballot_id)})
        if not ballot:
            return jsonify({'error': "Scrutin introuvable."}), 404

        # Vérification des droits : seul le créateur peut modifier
        if str(ballot['created_by']) != session.get('user_id'):
            return jsonify({'error': "Vous n'avez pas l'autorisation de modifier ce scrutin."}), 403

        # Vérification du statut : modification autorisée seulement si le scrutin n'est pas ouvert
        if datetime.strptime(ballot['start_date'], '%Y-%m-%d') <= datetime.now():
            return jsonify({'error': "Le scrutin est déjà ouvert. Les modifications ne sont plus autorisées."}), 400

        if request.method == 'GET':
            # Envoi des données existantes pour pré-remplir le formulaire
            ballot['_id'] = str(ballot['_id'])  # Convertir ObjectId en chaîne pour le JSON
            return jsonify(ballot)

        if request.method == 'POST':
            # Récupération des données du formulaire
            name_poll = request.form.get('name_poll')
            poll_question = request.form.get('poll_question')
            poll_text = request.form.get('poll_text')

            # Validation des données
            if not name_poll or not poll_question or not poll_text:
                return jsonify({'error': 'Tous les champs textuels sont obligatoires.'}), 400

            # Mise à jour des champs de textes
            update_data = {
                "name_poll": name_poll,
                "poll_question": poll_question,
                "poll_text": poll_text
            }

            ballot_collection.update_one({"_id": ObjectId(ballot_id)}, {"$set": update_data})
            
            flash("Scrutin modifié avec succès!", "success")
            return jsonify({'message': "Scrutin modifié avec succès."}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500



@ballot_bp.route('/vote/<ballot_id>', methods=['GET'])
@login_required
def vote_page(ballot_id):
    """
    Affiche une page de vote spécifique selon le type de scrutin.
    """
    ballot = ballot_collection.find_one({"_id": ObjectId(ballot_id)})
    
    if not ballot:
        return jsonify({"error": "Scrutin introuvable"}), 404

    if ballot["status"] != "active":
        return jsonify({"error": "Le scrutin est fermé, vous ne pouvez pas voter."}), 403

    # Vérifier le type de scrutin
    if ballot["type_vote"] == "Vote Majoritaire":
        return render_template('vote_majority.html', ballot=ballot)
    elif ballot["type_vote"] == "Vote Proportionnel":
        return render_template('vote_proportional.html', ballot=ballot)
    elif ballot["type_vote"] == "Vote Condorcet":
        return render_template('vote_condorcet.html', ballot=ballot)
    else:
        return jsonify({"error": "Type de vote non pris en charge"}), 400


@ballot_bp.route('/submit_vote/<ballot_id>', methods=['POST'])
@login_required
def submit_vote(ballot_id):
    """
    Permet à un utilisateur de voter pour un scrutin.
    Empêche de voter plusieurs fois, mais autorise la modification du vote avant la date de fin.
    """
    # Récupérer le scrutin
    ballot = ballot_collection.find_one({"_id": ObjectId(ballot_id)})

    if not ballot:
        flash("Scrutin introuvable.", "danger")
        return redirect(url_for('ballot.view_ballots', filter='latest'))

    if ballot["status"] != "active":
        flash("Le scrutin est fermé, vous ne pouvez pas voter.", "danger")
        return redirect(url_for('ballot.view_ballots', filter='latest'))

    # Récupérer l'utilisateur et l'option sélectionnée
    user_id = session.get("user_id")
    if not user_id:
        flash("Vous devez être connecté pour voter.", "warning")
        return redirect(url_for('auth.login'))

    selected_option = request.form.get("selected_option")

    # Gestion des types de vote
    if ballot["type_vote"] == "Vote Majoritaire":
        return handle_majority_vote(ballot, user_id, selected_option)

    elif ballot["type_vote"] == "Vote Condorcet":
        return handle_condorcet_vote(ballot, user_id, selected_option)

    elif ballot["type_vote"] == "Vote Proportionnel":
        return handle_proportional_vote(ballot, user_id, selected_option)

    else:
        flash("Type de vote non pris en charge.", "danger")
        return redirect(url_for('ballot.view_ballots', filter='latest'))
