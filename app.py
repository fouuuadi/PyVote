#Flask : moteur de l'application   
#Render_template : Affiche les gabarit d'affochage (remplate)
#Requets : Traitement des requetes HTTP
#url_for : Génere les URL   
#redirect : redirection HTTP
import os
from flask import Flask,render_template, jsonify, request, url_for, redirect, session
from flask_session import Session
#Object d'interraction avec MongoDB
from pymongo import MongoClient
print("fouad_app")
#Gestion des ids de MongoDB
from bson.objectid import ObjectId
from bson import json_util
from mongoDB.config.connection_db import get_database
from mongoDB.config.initialize_db import initialize_collections
from api.routes.auth import auth_bp
from utils.decorators import login_required



app = Flask(__name__)

# Enregistrer les Blueprint
# Avec le prefix sa sera /auth/signup et non /signup
app.register_blueprint(auth_bp, url_prefix='/auth')



app.secret_key = os.getenv("SECRET_KEY", "fallback_default_key")






# initialisation des collections
# crée les collections si elles sont inexistantes.
initialize_collections()

@app.route('/')
@login_required
def home():
    return render_template('home.html', pseudo=session['pseudo'])

#Le port sur lequel ton serveur flask fonctionne
FLASK_PORT = os.getenv("FLASK_PORT")

if __name__ == "__main__":
    app.run(debug=True, port=FLASK_PORT)
