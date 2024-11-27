# TP_FLASK_MONGO_JINJA

# Une application de gestion de scrutins

## Contexte

Avec quelques amis, vous avez été convaincu par le mouvement de la **Civic
Tech**, dont l’ambition est de proposer des outils numériques pour offrir des méthodes alternatives au vote majoritaire.

Bien que ce dernier soit la méthodes la plus répandue (et la plus simple) pour prendre des décisions, et en particulier pour les processus politiques locaux et nationaux, il existe depuis très longtemps des approches différentes, plus représentatives, mais
aussi plus difficiles à mettre en œuvre manuellement.

Parmi celles-ci, on peut compter au moins (en Europe) deux travaux majeurs. Tout d’abord celui du philosophe catalan **Ramon Lull**, qui écrit sur le sujet un ouvrage intitulé *De arte electionis* en 1299. L’autre auteur le plus connu sur le sujet est le mathématicien **Nicolas de Condorcet**, qui proposa lors de la Révolution française un système pour organiser des élections reflétant plus justement les préférences des citoyens. Connue depuis lors sous les noms de « méthode de Condorcet » ou
« vote Condorcet », cette approche a vu sa popularité s’agrandir à nouveau dans les mouvements du logiciel libre et les milieux associatifs où les prises de décision se font (en général) davantage sur le mode du consensus.

La possibilité et la part grandissante du vote numérique, même pour les éléctions générales, favorise donc les projets logiciels visant à mettre en œuvre des algorithmes plus sophistiqués que le simple décompte.

Vous avez donc constitué une équipe pour réaliser une plate-forme de vote que vous voudriez par la suite proposer à des organisations de toutes sortes, aussi bien privées que publiques, afin qu’elles puissent organiser en ligne des consultations et des votes.

Naturellement, un tel projet comporte de nombreuses facettes, en particulier la question délicate de la protection des données personnelles de votants, du processus de vote, de la sincérité et de la validation du vote, de la conservation des données, de la disponibilité du service, etc.

Vous avez collectivment opté pour développer l'application en Python avec Flask.

## Objectifs

Les objectifs principaux de votre travail sont les suivants :

1. Concevoir le modèle des données de l'application

2. Réaliser un prototype permettant l'organisation, le déroulement et l'affichage des résultat d'un scrutin. L'appllication devra permettre de choisir l'algorithme de décision.

3. Réaliser une interface d'administration permettant de modérer les scrutins et d'afficher des statistiques concernant ceux-ci.. 
