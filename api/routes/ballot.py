from datetime import datetime
from flask import Blueprint, render_template, session, redirect, url_for, flash, request, jsonify
from mongoDB.config.connection_db import get_database
from bson.objectid import ObjectId  # Pour gérer les ObjectId
from utils.decorators import login_required

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
            "created_by": str(ObjectId(created_by)),  
            "participants": [],  
            "status": status,  
            "start_date": start_date,
            "end_date": end_date
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
        return jsonify({'message': 'Scrutin créé avec succès.', 'ballot': ballot_data}), 201
    
    
    except Exception as e:
            # Gestion des erreurs
            return jsonify({'error': str(e)}), 500   


@ballot_bp.route('/latest_ballots', methods=['GET'])
def latest_ballots():
    """
    Route pour récupérer les 10 derniers scrutins créés.
    """
    latest_ballots = list(ballot_collection.find().sort("start_date", -1).limit(10))
    
    # Nettoyer les données pour éviter de renvoyer l'ObjectId sous forme d'objet BSON
    for ballot in latest_ballots:
        ballot["_id"] = str(ballot["_id"])  # Convertir ObjectId en string
    
    return jsonify(latest_ballots)

@ballot_bp.route('/active_ballots', methods=['GET'])
def active_ballots():
    """
    Route pour récupérer les 10 derniers scrutins actifs.
    """
    active_ballots = list(ballot_collection.find({"status": "active"}).sort("start_date", -1).limit(10))
    
    # Nettoyer les données pour éviter de renvoyer l'ObjectId sous forme d'objet BSON
    for ballot in active_ballots:
        ballot["_id"] = str(ballot["_id"])  # Convertir ObjectId en string
    
    return jsonify(active_ballots)
