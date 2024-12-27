from flask import Blueprint, jsonify, render_template
from mongoDB.config.connection_db import get_database

# Création du Blueprint pour gérer les scrutins
ballots_bp = Blueprint('ballots', __name__, template_folder='templates')

db = get_database()
ballots_collection = db["Ballots"]

@ballots_bp.route('/latest_ballots', methods=['GET'])
def latest_ballots():
    """
    Route pour récupérer les 10 derniers scrutins créés.
    """
    latest_ballots = list(ballots_collection.find().sort("start_date", -1).limit(10))
    
    # Nettoyer les données pour éviter de renvoyer l'ObjectId sous forme d'objet BSON
    for ballot in latest_ballots:
        ballot["_id"] = str(ballot["_id"])  # Convertir ObjectId en string
    
    return jsonify(latest_ballots)

@ballots_bp.route('/active_ballots', methods=['GET'])
def active_ballots():
    """
    Route pour récupérer les 10 derniers scrutins actifs.
    """
    active_ballots = list(ballots_collection.find({"status": "active"}).sort("start_date", -1).limit(10))
    
    # Nettoyer les données pour éviter de renvoyer l'ObjectId sous forme d'objet BSON
    for ballot in active_ballots:
        ballot["_id"] = str(ballot["_id"])  # Convertir ObjectId en string
    
    return jsonify(active_ballots)
