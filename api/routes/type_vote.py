from flask import Blueprint, jsonify
from bson.objectid import ObjectId
from mongoDB.config.connection_db import get_database
from utils.decorators import login_required
from utils.enums import TypeVote
from utils.majoritaire import vote_majoritaire
from datetime import datetime

type_vote_bp = Blueprint('type_vote', __name__)

db = get_database()
ballot_collection = db["Ballots"]

@type_vote_bp.route('/process_vote/<ballot_id>', methods=['GET'])
@login_required
def process_vote(ballot_id):
    """
    Route pour traiter un scrutin en fonction de son type de vote.
    """
    ballot = ballot_collection.find_one({"_id": ObjectId(ballot_id)})

    if not ballot:
        return jsonify({"error": "Scrutin introuvable"}), 404

    # Vérifier si le scrutin est terminé
    if datetime() < datetime.strptime(ballot['end_date'], '%Y-%m-%d'):
        return jsonify({"error": "Les résultats seront disponibles uniquement après la fin du scrutin."}), 400

    if ballot["type_vote"] == TypeVote.MAJORITAIRE.value:
        result = vote_majoritaire(ballot)
    else:
        return jsonify({"error": "Type de vote non pris en charge"}), 400

    return jsonify(result)

