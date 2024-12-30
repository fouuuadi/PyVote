#Vote majoritaire
from datetime import datetime
from mongoDB.config.connection_db import get_database


db = get_database()
ballots_collection = db["Ballots"]

def vote_majoritaire():
    """
    Cette fonction va servir a Dépouiller un scrutin
    """
    if datetime() < datetime.strptime(ballots_collection['end_date'], '%Y-%m-%d'):
        return {"error": "Les résultats seront disponibles uniquement après la fin du scrutin."}

    # Initialiser un dictionnaire pour compter les votes
    counts = {option: 0 for option in ballots_collection['poll_response']}
    for participant in ballots_collection.get('participants', []):
        if participant['choice'] in counts:
            counts[participant['choice']] += 1

    # Trier les résultats par nombre de votes décroissant
    sorted_results = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    return {"results": sorted_results}