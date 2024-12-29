from flask import jsonify
from bson.objectid import ObjectId

def handle_majority_vote(ballot, user_id, selected_option):
    if selected_option not in ballot["poll_response"]:
        return jsonify({"error": "Option invalide."}), 400

    existing_vote = next((participant for participant in ballot["participants"] if str(participant["user_id"]) == user_id), None)

    if existing_vote:
        # Mise à jour du vote existant
        ballot_collection.update_one(
            {"_id": ObjectId(ballot["_id"]), "participants.user_id": ObjectId(user_id)},
            {"$set": {"participants.$.choice": selected_option}}
        )
        return jsonify({"message": "Votre vote a été mis à jour avec succès."}), 200
    else:
        # Ajouter un nouveau vote
        ballot_collection.update_one(
            {"_id": ObjectId(ballot["_id"])},
            {"$push": {"participants": {"user_id": ObjectId(user_id), "choice": selected_option}}}
        )
        return jsonify({"message": "Votre vote a été enregistré avec succès."}), 200
