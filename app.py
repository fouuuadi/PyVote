#Flask : moteur de l'application   
#Render_template : Affiche les gabarit d'affochage (remplate)
#Requets : Traitement des requetes HTTP
#url_for : Génere les URL   
#redirect : redirection HTTP
import os
from datetime import datetime
from flask import Flask, render_template, jsonify, request, url_for, redirect, session, get_flashed_messages
from flask_session import Session
#Object d'interraction avec MongoDB
from pymongo import MongoClient
print("fouad_app")
#Gestion des ids de MongoDB
from bson.objectid import ObjectId
from bson import json_util
from mongoDB.config.connection_db import get_database
from mongoDB.config.initialize_db import initialize_collections
# from mongoDB.config.script_data import write_data
from api.routes.auth import auth_bp
from api.routes.profile import profile_bp
from api.routes.ballot import ballot_bp
from api.routes.type_vote import type_vote_bp
from utils.decorators import login_required



app = Flask(__name__)

# Enregistrer les Blueprint
# Avec le prefix sa sera /auth/signup et non /signup
app.register_blueprint(auth_bp, url_prefix='/auth') 
app.register_blueprint(profile_bp, url_prefix='/user')
app.register_blueprint(ballot_bp, url_prefix='/ballot')



app.secret_key = os.getenv("SECRET_KEY", "fallback_default_key")

#Elle permet d'injecter la variable current_time contenant la date et l'heure actuelles dans tous les templates de l'application Flask
@app.context_processor
def inject_current_time():
    return {'current_time': datetime.now()}

@app.context_processor
def inject_vote_messages():
    messages = get_flashed_messages(with_categories=True)
    vote_errors = [msg for category, msg in messages if category == 'vote_error']
    return {'vote_errors': vote_errors}






# initialisation des collections
# crée les collections si elles sont inexistantes.
initialize_collections()

# écriture des données
# write_data()

@app.route('/')
def home():
    return render_template('home.html')

#Le port sur lequel ton serveur flask fonctionne
FLASK_PORT = os.getenv("FLASK_PORT")

app.secret_key = os.getenv("SECRET_KEY", "fallback_default_key")



if __name__ == "__main__":
    app.run(debug=True, port=FLASK_PORT)
