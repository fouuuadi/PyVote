#Flask : moteur de l'application   
#Render_template : Affiche les gabarit d'affochage (remplate)
#Requets : Traitement des requetes HTTP
#url_for : Génere les URL   
#redirect : redirection HTTP
import os
from flask import Flask,render_template, request, url_for, redirect
#Object d'interraction avec MongoDB
from pymongo import MongoClient
#Gestion des ids de MongoDB
from bson.objectid import ObjectId

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

@app.route('/data', methods=['GET'])
def dataExemple():




if __name__ == "__main__":
    app.run(debug=True, port=4001)
