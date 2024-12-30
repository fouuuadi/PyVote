from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from mongoDB.config.connection_db import get_database
from bson.objectid import ObjectId  # Pour gérer les ObjectId
from utils.decorators import login_required

profile_bp = Blueprint('profile', __name__, template_folder='templates')

db = get_database()
users_collection = db["Users"]
ballot_collection = db["Ballots"]

@profile_bp.route('/profile', methods=['GET'])
@login_required
def profile():
    """
    Afficher le profil utilisateur.
    
    On verifie si il y a un utilisateur dans la session, si non il est rediriger pour se connecter.
    
    Si oui, on affiche les données de l'utilisateur
    """
    
    user = users_collection.find_one({"_id": ObjectId(session['user_id'])})

    if 'user_id' not in session:
        flash("Vous devez être connecté pour accéder a votre profil.", "warning")
        return redirect(url_for('auth.login'))
    
    # Récupérer l'utilisateur connecté
    user = users_collection.find_one({"_id": ObjectId(session['user_id'])})

    # Gestion de l'utilisateur introuvable
    if not user:
        flash("Utilisateur introuvable.", "danger")
        return redirect(url_for('auth.login'))
    
    # Récupérer les scrutins créés par cet utilisateur
    ballots = list(ballots_collection.find({"created_by": ObjectId(session['user_id'])}))

    # Rendu du template avec les données utilisateur et les scrutins
    return render_template('profile.html', user=user, ballots=ballots)

@profile_bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """
    Modifier le profil utilisateur.
    """
    
    user = users_collection.find_one({"_id": ObjectId(session['user_id'])})
    
    if 'user_id' not in session:
        flash("Vous devez être connecté pour modifier votre profil.", "warning")
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        updated_fields = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "age": request.form.get("age"),
            "gender": request.form.get("gender"),
            "location": request.form.getlist("location"),
        }
    
        # Supprimer les champs vides
        for key in list(updated_fields.keys()):
            if not updated_fields[key]:  # Si la valeur est vide (None, "", etc.)
                del updated_fields[key]  # Supprime ce champ du dictionnaire

        
        # Mettre à jour uniquement les champs modifiables
        users_collection.update_one({"_id": ObjectId(session['user_id'])}, {"$set": updated_fields})
        flash("Profil mis à jour avec succès.", "success")
        return redirect(url_for('profile.profile'))

    return render_template('edit_profile.html', user=user)

def get_user_with_polls(user_id):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if user and 'creations_polls' in user and user['creations_polls']:
        # Récupérer les sondages par leurs IDs
        poll_ids = [ObjectId(poll_id) for poll_id in user['creations_polls'] if poll_id]
        polls = ballot_collection.find({"_id": {"$in": poll_ids}})
        user['polls_details'] = list(polls)  # Ajouter les détails des sondages
    else:
        user['polls_details'] = []  # Ajouter une liste vide par défaut
    return user
