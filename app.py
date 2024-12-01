#Flask : moteur de l'application   
#Render_template : Affiche les gabarit d'affochage (remplate)
#Requets : Traitement des requetes HTTP
#url_for : Génere les URL   
#redirect : redirection HTTP
import os
from flask import Flask,render_template, jsonify, request, url_for, redirect
#Object d'interraction avec MongoDB
from pymongo import MongoClient
#Gestion des ids de MongoDB
from bson.objectid import ObjectId
from bson import json_util
from mongoDB.config.connection_db import get_database
from mongoDB.config.initialize_db import initialize_collections


app = Flask(__name__)

# initialisation des collections
# crée les collections si elles sont inexistantes.
initialize_collections()

@app.route("/")
def home():
    return

#Le port sur lequel ton serveur flask fonctionne
FLASK_PORT = os.getenv("FLASK_PORT")

if __name__ == "__main__":
    app.run(debug=True, port=FLASK_PORT)
