import json
import os
from mongoDB.config.connection_db import get_database


def initialize_collections():
    db = get_database()
    if db is not None:
        try:
            # Base directory du projet
            base_dir = os.path.dirname(os.path.abspath(__file__))

            # Liste des collections et fichiers JSON correspondants
            collections_files = {
                "Users": os.path.join(base_dir, "../collections/Users.json"),
                "Ballots": os.path.join(base_dir, "../collections/Ballots.json")
            }

            # Récupère les collections existantes
            existing_collections = db.list_collection_names()

            # Parcourir les collections et leurs fichiers
            for collection, file in collections_files.items():
                # Supprime la collection si elle existe déjà
                if collection in existing_collections:
                    #db[collection].drop()
                    #print(f"Collection '{collection}' supprimée.")
                    # Crée la collection
                    db.create_collection(collection)
                    print(f"Collection '{collection}' créée.")
                

                # Charger les données depuis le fichier JSON
                with open(file, "r") as f:
                    data = json.load(f)
                    print(f"Contenu brut de {file}: {data}")

                # Extraire les données spécifiques (par exemple, la clé "user" ou "poll")
                if "user" in data:
                    data_to_insert = [data["user"]]  # Encapsuler dans une liste
                elif "poll" in data:
                    data_to_insert = [data["poll"]]  # Encapsuler dans une liste
                else:
                    data_to_insert = []

                # Insérer les données dans la collection
                if data_to_insert:
                    db[collection].insert_many(data_to_insert)
                    print(f"Documents insérés dans la collection '{collection}'.")
                else:
                    print(f"Aucune donnée à insérer dans la collection '{collection}'.")
        except Exception as e:
            print(f"Erreur lors de l'initialisation des collections : {e}")


if __name__ == "__main__":
    initialize_collections()
