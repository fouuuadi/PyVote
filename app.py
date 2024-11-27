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

app = Flask(__name__)

#Configuration de la base de donnee MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
#Client MongoDB
client = MongoClient(MONGO_URI)
db = client["admin"]
collection = db["restaurants"]

@app.route('/', methods=['GET'])
def index():
    #tjrs render le fichier enfant Pas le parent 
    return render_template('layout.html')

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
#     # Récupérer les 10 premiers restaurants, triés par nom
#     cursor = collection.find().sort("name", 1).limit(10)
#     # Convertir les données en JSON compatible avec Flask
#     data = json_util.dumps(cursor)
#     return data, 200
    cursor = collection.find().sort("name", 1).limit(10)
    restaurants = list(cursor)  # Convertir le curseur en liste
    return render_template('layout.html', restaurants=restaurants)




if __name__ == "__main__":
    app.run(debug=True, port=4001)
