from flask import Blueprint, request, render_template, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo.errors import DuplicateKeyError
from mongoDB.config.connection_db import get_database
from utils.enums import Gender, ActiveUser
from utils.decorators import login_required
from bson.objectid import ObjectId



auth_bp = Blueprint('auth', __name__, template_folder='templates')

db = get_database()
users_collection = db["Users"]

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        age = request.form['age']
        gender = request.form.get('gender') #recupere la valeur de la class ENUM
        active_user = ActiveUser.ACTIVE.value #recupere la valeur de la class ENUM, par defaut l'utilisateur va etre sur Actif a la création du compte
        
        if gender not in [genders.value for genders in Gender]:
            flash("valeur de genre invalide.", "danger")
            return render_template('signup.html')

        try:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

            user_data = {
                "pseudo": pseudo,
                "first_name": first_name,
                "last_name": last_name,
                "password": hashed_password,
                "age": age,
                "gender": gender,
                "participation_poll": [],
                "location": [],
                "creations_polls": [],
                "active_user": active_user,
                "commentaire": []
            }

            users_collection.insert_one(user_data)
            print(f"Nouvel utilisateur inscrit : {pseudo}")
            flash('Inscription réussie ! Vous pouvez maintenant vous connecter.', 'success')
            return redirect(url_for('auth.login'))

        except DuplicateKeyError:
            print(f"Erreur : Le pseudo '{pseudo}' est déjà utilisé.")
            flash('Le pseudo est déjà utilisé. Veuillez en choisir un autre.', 'danger')

    return render_template('signup.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Route pour la connexion des utilisateurs.
    """
    if request.method == 'POST':
        pseudo = request.form.get('pseudo')
        password = request.form.get('password')

        user = users_collection.find_one({'pseudo': pseudo})

        if user and user['password'] and check_password_hash(user['password'], password):
            if user.get('active_user') == 'Fermé':
                flash("Votre compte est inactif. Veuillez contacter l'administration.", "warning")
                return redirect(url_for('auth.login'))

            session['user_id'] = str(user['_id'])
            session['pseudo'] = user['pseudo']
            flash("Connexion réussie !", "success")
            return redirect(url_for('home'))
        else:
            flash("Échec de la connexion. Vérifiez vos identifiants.", "danger")
            return redirect(url_for('auth.login'))
    
    return render_template('login.html')


@auth_bp.route('/logout', methods=['POST'])
def logout():
    if 'pseudo' in session:
        print(f"Utilisateur déconnecté : {session['pseudo']}")
    session.clear()
    flash('Vous avez été déconnecté.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/delete_profile', methods=['POST'])
@login_required
def delete_profile():
    """
    Marque un profil utilisateur comme "fermé" en effaçant ses données personnelles
    tout en conservant son pseudonyme et son historique de votes.
    """
    try:
        user_id = session.get('user_id')
        
        if not user_id:
            return jsonify({'error': 'Utilisateur non authentifié'}), 401

        user = users_collection.find_one({'_id': ObjectId(user_id)})

        if not user:
            return jsonify({'error': 'Utilisateur introuvable'}), 404

        # mise a jour de tout les champs sauf pseudo
        updated_data = {
            "first_name": None,
            "last_name": None,
            "password": None,
            "age": None,
            "gender": None,
            "location": None,
            "active_user": "Fermé"
        }

        users_collection.update_one(
            {'_id': ObjectId(user_id)},
            {'$set': updated_data}
        )

        # supprime tout dans la session en cour
        session.clear()

        return jsonify({'message': 'Profil utilisateur marqué comme fermé avec succès.'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500