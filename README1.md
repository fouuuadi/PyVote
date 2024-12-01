Pour lancer votre environnement de développement :
# source env/bin/activate  # Sur macOS/Linux
# env\Scripts\activate  # Sur Windows

Ensuite, installez n'importe quelle bibliothèque dont vous avez besoin.

Important : Si vous essayez de lancer votre projet et qu'il ne fonctionne pas, il est possible que vous n'ayez pas démarré votre environnement de développement.

Pour générer un fichier requirements.txt avec toutes les dépendances de votre environnement de développement, utilisez la commande suivante :

# pip freeze > requirements.txt

pip freeze > requirements.txt permet également de mettre à jour le fichier requirements.txt.

Bien qu'il existe des outils comme pip-tools, pour ce projet, nous allons rester sur cette première solution.


brew services restart mongodb/brew/mongodb-community