from collections import defaultdict

def condorcet_winner(votes):
    """
    Trouve le gagnant de Condorcet, s'il existe.
    
    :param votes: Liste des préférences des électeurs. Chaque préférence est une liste de candidats classés par ordre.
    :return: Le gagnant de Condorcet ou None s'il n'y en a pas.
    """
    # Obtenir la liste des candidats
    candidates = set(candidate for ballot in votes for candidate in ballot)
    pairwise_wins = defaultdict(int)  # Comptage des victoires en confrontation directe
    pairwise_losses = defaultdict(int)  # Comptage des défaites en confrontation directe
    
    # Comparer chaque paire de candidats
    for candidate1 in candidates:
        for candidate2 in candidates:
            if candidate1 != candidate2:
                # Comptons combien d'électeurs préfèrent candidate1 à candidate2
                votes_for_c1 = sum(
                    ballot.index(candidate1) < ballot.index(candidate2)
                    for ballot in votes
                )
                votes_for_c2 = len(votes) - votes_for_c1
                if votes_for_c1 > votes_for_c2:
                    pairwise_wins[candidate1] += 1
                    pairwise_losses[candidate2] += 1

    # Chercher le candidat qui gagne contre tous les autres
    for candidate in candidates:
        if pairwise_wins[candidate] == len(candidates) - 1:
            return candidate

    return None  # Aucun gagnant de Condorcet trouvé

# Exemple d'utilisation
votes = [
    ['A', 'B', 'C'],  # Électeur 1 : A > B > C
    ['B', 'C', 'A'],  # Électeur 2 : B > C > A
    ['C', 'A', 'B'],  # Électeur 3 : C > A > B
    ['C', 'A', 'B'],  # Électeur 3 : C > A > B
    ['C', 'A', 'B'],  # Électeur 3 : C > A > B
]

winner = condorcet_winner(votes)
if winner:
    print(f"Le gagnant de Condorcet est : {winner}")
else:
    print("Aucun gagnant de Condorcet.")
