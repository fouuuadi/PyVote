from functools import wraps
from flask import session, redirect, url_for, flash

# Permet de protéger les routes pour lesquelles l'utilisateur doit être connecté
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:  # Vérifie si l'utilisateur est connecté avec son _id
            flash("Vous devez être connecté pour accéder à cette page.", "warning")
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function
