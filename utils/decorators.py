from functools import wraps
from flask import session, flash, redirect, url_for
from bson.objectid import ObjectId
from mongoDB.config.connection_db import get_database

db = get_database()
users_collection = db["Users"]

def login_required(f):
    """
    Permet de protéger les routes pour lesquelles l'utilisateur doit être connecté
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Vérifie si 'user_id' est dans la session
        if 'user_id' not in session:
            flash("Vous devez être connecté pour accéder à cette page.", "warning")
            return redirect(url_for('auth.login'))
        
        # Vérifie si l'utilisateur existe dans la base de données
        user = users_collection.find_one({"_id": ObjectId(session["user_id"])})
        if not user:
            flash("Votre session n'est plus valide. Veuillez vous reconnecter.", "warning")
            session.clear() 
            return redirect(url_for('auth.login'))
        
        return f(*args, **kwargs)
    return decorated_function
