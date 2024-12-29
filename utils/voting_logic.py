from flask import jsonify, flash, redirect, url_for
from bson.objectid import ObjectId
from mongoDB.config.connection_db import get_database

db = get_database()
ballot_collection = db["Ballots"]


def handle_majority_vote(ballot, user_id, selected_option):
    if selected_option not in ballot["poll_response"]:
        flash("Option invalide.", "danger")
        return redirect(url_for('ballot.view_ballots', filter='latest'))

    existing_vote = next((participant for participant in ballot["participants"] if str(participant["user_id"]) == user_id), None)

    if existing_vote:
        # Mise à jour du vote existant
        ballot_collection.update_one(
            {"_id": ObjectId(ballot["_id"]), "participants.user_id": ObjectId(user_id)},
            {"$set": {"participants.$.choice": selected_option}}
        )
        flash("Votre vote a été mis à jour avec succès.", "success")
    else:
        # Ajouter un nouveau vote
        ballot_collection.update_one(
            {"_id": ObjectId(ballot["_id"])},
            {"$push": {"participants": {"user_id": ObjectId(user_id), "choice": selected_option}}}
        )
        flash("Votre vote a été enregistré avec succès.", "success")
    
    db["Users"].update_one(
        {"_id": ObjectId(user_id)},
        {"$addToSet": {"participation_poll": str(ballot["_id"])}}
    )

    return redirect(url_for('ballot.view_ballots', filter='latest'))

def handle_condorcet_vote(ballot, user_id, selected_option):
    pass

def handle_proportional_vote(ballot, user_id, selected_option):
    pass