# fichier pour l'intialisation de la connexion à MongoDB et création des collections

# import de la base de donnée et de la fonction
from data.db.db_config import get_database

def initialize_database():
    #Si la db a mal été créée
    db = get_database()
    if db is None:
        print("Impossible d'initialiser la base de données.")
        return
    
    # Définir les collections à créer
    collections = ["user", "vote", "option", "question"]

    # Création des collections si elles n'existent pas
    # for collection in collections:
    #     if collection not in db.list_collection_names():
    #         db.create_collection(collection)
    #         print(f"Collection '{collection}' créée avec succès.")
    #     else:
    #         print(f"Collection '{collection}' existe déjà.")