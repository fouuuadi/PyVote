from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo.errors import DuplicateKeyError
from mongoDB.config.connection_db import get_database
from utils.enums import Gender, ActiveUser


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
                "creation_pulls": [],
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
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        password = request.form['password']

        user = users_collection.find_one({"pseudo": pseudo})

        if user and check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            session['pseudo'] = user['pseudo']
            print(f"Utilisateur connecté : {pseudo}")
            flash('Connexion réussie.', 'success')
            return redirect(url_for('home'))  # Redirige vers la page d'accueil
        else:
            print(f"Erreur de connexion pour le pseudo : {pseudo}")
            flash('Pseudo ou mot de passe incorrect.', 'danger')

    return render_template('login.html')

@auth_bp.route('/logout', methods=['POST'])
def logout():
    if 'pseudo' in session:
        print(f"Utilisateur déconnecté : {session['pseudo']}")
    session.clear()
    flash('Vous avez été déconnecté.', 'info')
    return redirect(url_for('auth.login'))
