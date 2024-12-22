Pour lancer votre environnement de développement :
# source env/bin/activate  # Sur macOS/Linux
# env\Scripts\activate  # Sur Windows

Ensuite, installez n'importe quelle bibliothèque dont vous avez besoin.

Après avoir cloné le repository avec git clone, si aucun environnement virtuel n'est créé, vous devrez en créer un avec cette commande. Assurez-vous d'être à la racine de votre projet avant de l'exécuter :

python3 -m venv venv

Toujours à la racine de votre projet, utilisez cette commande pour activer votre environnement virtuel :

source venv/bin/activate # Sur macOS/Linux venv\Scripts\activate # Sur Windows

Pour desactiver ton environnement :

deactivate

Pour savoir les dépendances installer sur environnement :

pip list ou pip3 list

Pour installer les dépendences du fichier requirements.txt :

pip install -r requirements.txt

Ensuite, vous pourrez installer toutes les dépendances nécessaires à ce projet.

À la fin, une fois vos dépendances installées, vous pourrez créer un fichier .txt contenant la liste de toutes les dépendances avec cette commande :

pip freeze > requirements.txt

# Commande Mongo

brew services restart mongodb/brew/mongodb-community
