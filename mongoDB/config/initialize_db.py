from mongoDB.config.connection_db import get_database

def initialize_collections():
    db = get_database()
    if db is not None:
        try:
            # Liste des collections nécessaires
            required_collections = ["Ballots", "Users"]

            # Récupère les collections existantes
            existing_collections = db.list_collection_names()

            # Crée les collections manquantes
            for collection in required_collections:
                if collection not in existing_collections:
                    db.create_collection(collection)
                    print(f"Collection '{collection}' créée.")
                else:
                    print(f"Collection '{collection}' existe déjà.")
        except Exception as e:
            print(f"Erreur lors de l'initialisation des collections : {e}")

if __name__ == "__main__":
    initialize_collections()

