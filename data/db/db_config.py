# Import du module mongo
from pymongo import MongoClient

# Configuration de MongoDB

# Liaison à la bdd
# avec l'url et le port par défaut
MONGO_URL = "mongodb://localhost:27017"
# client = MongoClient('localhost', 27017)

# nom de la base de donnée
DB_NAME = "scrutindb"

def get_database() :

    # Connexion à la base de donnée
    try:
        client = MongoClient(MONGO_URL)
        db = client[DB_NAME]
        print("Connexion à '{DB_NAME} réussie.")
        return db
    except:
        print("Erreur dans la connexion")
        return None

