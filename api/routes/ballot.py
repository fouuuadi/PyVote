from datetime import datetime
from flask import Blueprint, render_template, session, redirect, url_for, flash, request, jsonify
from mongoDB.config.connection_db import get_database
from bson.objectid import ObjectId
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
        poll_response = [response.strip() for response in request.form.getlist('poll_response') if response.strip()] #strip pour supprimer les espaces
        print(poll_response)
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        type_vote = request.form.get('type_vote')
        created_by = session.get('user_id')
        print(request.form)  # Affiche toutes les données reçues
        
        # validation des données
        
        if not name_poll or not poll_question or not poll_text:
            return jsonify({'error': 'Tous les champs obligatoire doivent être remplit'}), 400
        
        if not poll_response or len(poll_response) < 2:
            return jsonify({'error': 'Le scrutin doit contenir au moins deux réponses possibles'}), 400
        
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
            status = "Open"  # Entre les deux dates
        
        # dictonnaire qui contient les donnees du scrutin qu'on va push
        ballot_data = {
            "name_poll": name_poll,
            "poll_question": poll_question,
            "poll_text": poll_text,
            "poll_response": poll_response,
            "created_by": ObjectId(created_by),  
            "participants": [],  
            "status": status,  
            "start_date": start_date,
            "end_date": end_date,
            "type_vote":type_vote
        }
        
        ballot_id = ballot_collection.insert_one(ballot_data).inserted_id
        
        users_collection.update_one(
            {'_id': ObjectId(created_by)},
            {"$push": {"creations_polls": ballot_id}}
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

@ballot_bp.route('/user_ballots', methods=['GET'])
@login_required
def user_ballots():
    """
    Affiche tous les scrutins créés par l'utilisateur connecté.
    """
    current_time = datetime.now()
    user_id = session.get('user_id')
    ballots = list(ballot_collection.find({"created_by": ObjectId(user_id)}))

    for ballot in ballots:
        ballot['_id'] = str(ballot['_id'])
        ballot['start_date'] = datetime.strptime(ballot['start_date'], '%Y-%m-%d')
        ballot['end_date'] = datetime.strptime(ballot['end_date'], '%Y-%m-%d')

    return render_template('user_ballots.html', ballots=ballots, current_time=current_time)

@ballot_bp.route('/edit_ballot/<ballot_id>', methods=['GET', 'POST'])
@login_required
def edit_ballot(ballot_id):
    """
    Permet de modifier un scrutin existant tant qu'il n'est pas encore ouvert.
    """
    # Récupérer le scrutin depuis la base de données
    ballot = ballot_collection.find_one({"_id": ObjectId(ballot_id)})
    
    if not ballot:
        flash("Scrutin introuvable.", "danger")
        return redirect(url_for('ballot.user_ballots'))

    # Vérifier si l'utilisateur connecté est le créateur du scrutin
    if str(ballot['created_by']) != session.get('user_id'):
        flash("Vous n'avez pas l'autorisation de modifier ce scrutin.", "danger")
        return redirect(url_for('ballot.user_ballots'))

    # Vérifier si le scrutin a déjà commencé
    if datetime.strptime(ballot['start_date'], '%Y-%m-%d') <= datetime.now():
        flash("Le scrutin a déjà commencé, il ne peut plus être modifié.", "warning")
        return redirect(url_for('ballot.user_ballots'))

    if request.method == 'POST':
        # Récupérer les nouvelles données du formulaire
        name_poll = request.form.get('name_poll')
        poll_question = request.form.get('poll_question')
        poll_text = request.form.get('poll_text')

        # Validation des données
        if not name_poll or not poll_question or not poll_text:
            flash("Tous les champs sont obligatoires.", "danger")
            return redirect(url_for('ballot.edit_ballot', ballot_id=ballot_id))

        # Mettre à jour les données dans la base
        update_data = {
            "name_poll": name_poll,
            "poll_question": poll_question,
            "poll_text": poll_text
        }
        ballot_collection.update_one({"_id": ObjectId(ballot_id)}, {"$set": update_data})

        flash("Scrutin modifié avec succès.", "success")
        return redirect(url_for('ballot.user_ballots'))

    # Rendre le formulaire pré-rempli avec les données existantes
    return render_template('edit_ballot.html', ballot=ballot)





@ballot_bp.route('/view_ballots', methods=['GET'])
def view_ballots():
    """
    Route pour afficher la liste des scrutins avec des filtres.
    """
    filter_type = request.args.get('filter', 'latest')  # Par défaut : derniers scrutins créés
    type_vote = request.args.get('type_vote', 'all')  # Par défaut : tous les types

    # Construire la requête MongoDB
    query = {}
    if filter_type == 'Open':
        query["status"] = "Open"  # Scrutins actifs
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



@ballot_bp.route('/vote/<ballot_id>', methods=['GET'])
@login_required
def vote_page(ballot_id):
    """
    Affiche une page de vote spécifique selon le type de scrutin.
    """
    ballot = ballot_collection.find_one({"_id": ObjectId(ballot_id)})
    
    if not ballot:
        return jsonify({"error": "Scrutin introuvable"}), 404

    if ballot["status"] != "Open":
        return jsonify({"error": "Le scrutin est fermé, vous ne pouvez pas voter."}), 403

    # Vérifier le type de scrutin
    if ballot["type_vote"] == "Vote Majoritaire":
        return render_template('vote_majority.html', ballot=ballot)
    elif ballot["type_vote"] == "Vote Proportionnel":
        flash("Ce type de vote n'est pas encore disponible. Veuillez créer un scrutin de type Majoritaire pour tester.", "vote_error")
        return redirect(url_for('ballot.view_ballots'))
    elif ballot["type_vote"] == "Vote Condorcet":
        flash("Ce type de vote n'est pas encore disponible. Veuillez créer un scrutin de type Majoritaire pour tester.", "vote_error")
        return redirect(url_for('ballot.view_ballots'))
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

    if ballot["status"] != "Open":
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
