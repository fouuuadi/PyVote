from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

# Récupérer les configurations depuis le fichier .env
MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME")

def get_database():
    """
    Connecte à MongoDB et retourne l'objet de base de données.
    """
    try:
        client = MongoClient(MONGO_URL)
        db = client[DB_NAME]
        print(f"Connexion à la base de données '{DB_NAME}' réussie.")
        return db
    except Exception as e:
        print(f"Erreur lors de la connexion à MongoDB : {e}")
        return None


#
