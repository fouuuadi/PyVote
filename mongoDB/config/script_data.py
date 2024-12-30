# from pymongo import MongoClient

# def write_data():
#     # Connexion au MongoDB local
#     client = MongoClient("mongodb://localhost:27017")
#     print("Connexion à MongoDB réussie.")

#     # Base cible
#     target_db = client["admin"]
#     print("Accès à la base 'admin' réussi.")

#     # Collection où insérer les données
#     target_collection = target_db["Ballots"] 
#     print("Accès à la collection 'Ballots' réussi.")
    
#     # Données à insérer dans la collection
#     ballots = [{
#   "name_poll": "Ballon d'Or 2024",
#   "poll_question": "Quel joueur mérite le Ballon d'Or 2024 ?",
#   "poll_text": "Votez pour votre joueur préféré.",
#   "poll_response": [
#     "Rodri",
#     "Kylian Mbappé",
#     "Erling Haaland",
#     "Vinicius Jr.",
#     "Jude Bellingham",
#     "Dani Carvajal",
#     "Lautaro Martinez",
#     "Toni Kroos",
#     "Harry Kane",
#     "Phil Foden",
#     "Lamine Yamal",
#     "Florian Wirtz",
#     "Nico Williams",
#     "Emiliano Martinez",
#     "Dani Olmo"
#   ],
#   "created_by": "user_id_001",
#   "end_date": "2025-01-16",
#   "start_date": "2024-12-20",
#   "status": "Open",
#   "participants": [
#     {
#       "player_id": "player_id_001",
#       "name": "Rodri",
#       "age": 27,
#       "nationality": "Espagnol",
#       "club": "Manchester City",
#       "position": "Milieu",
#       "teams": {
#         "club": "Manchester City",
#         "national_team": "Espagne"
#       },
#       "stats": {
#         "goals": 12,
#         "assists": 15,
#         "palmares": [
#           "Euro 2024",
#           "Premier League",
#           "Club World Cup",
#           "UEFA Super Cup"
#         ]
#       }
#     },
#     {
#       "player_id": "player_id_002",
#       "name": "Kylian Mbappé",
#       "age": 25,
#       "nationality": "Française",
#       "club": "Real Madrid",
#       "position": "Attaquant",
#       "teams": {
#         "club": "Real Madrid",
#         "national_team": "France"
#       },
#       "stats": {
#         "goals": 52,
#         "assists": 21,
#         "palmares": [
#           "Ligue 1",
#           "Coupe de France",
#           "Trophée des Champions"
#         ]
#       }
#     },
#     {
#       "player_id": "player_id_003",
#       "name": "Erling Haaland",
#       "age": 24,
#       "nationality": "Norvégien",
#       "club": "Manchester City",
#       "position": "Attaquant",
#       "teams": {
#         "club": "Manchester City",
#         "national_team": "Norvège"
#       },
#       "stats": {
#         "goals": 45,
#         "assists": 6,
#         "palmares": [
#           "Premier League",
#           "Club World Cup",
#           "UEFA Super Cup"
#         ]
#       }
#     },
#     {
#       "player_id": "player_id_004",
#       "name": "Vinicius Jr.",
#       "age": 23,
#       "nationality": "Brésilienne",
#       "club": "Real Madrid",
#       "position": "Attaquant",
#       "teams": {
#         "club": "Real Madrid",
#         "national_team": "Brésil"
#       },
#       "stats": {
#         "goals": 26,
#         "assists": 12,
#         "palmares": [
#           "Champions League",
#           "La Liga",
#           "Supercopa de España"
#         ]
#       }
#     },
#     {
#       "player_id": "player_id_005",
#       "name": "Jude Bellingham",
#       "age": 21,
#       "nationality": "Anglais",
#       "club": "Real Madrid",
#       "position": "Milieu",
#       "teams": {
#         "club": "Real Madrid",
#         "national_team": "Angleterre"
#       },
#       "stats": {
#         "goals": 27,
#         "assists": 17,
#         "palmares": [
#           "Champions League",
#           "La Liga",
#           "Supercopa de España"
#         ]
#       }
#     },
#     {
#       "player_id": "player_id_006",
#       "name": "Dani Carvajal",
#       "age": 32,
#       "nationality": "Espagnol",
#       "club": "Real Madrid",
#       "position": "Défenseur",
#       "teams": {
#         "club": "Real Madrid",
#         "national_team": "Espagne"
#       },
#       "stats": {
#         "goals": 7,
#         "assists": 8,
#         "palmares": [
#           "Euro 2024",
#           "Champions League",
#           "La Liga",
#           "Supercopa de España"
#         ]
#       }
#     },
#     {
#       "player_id": "player_id_007",
#       "name": "Lautaro Martinez",
#       "age": 26,
#       "nationality": "Argentine",
#       "club": "Inter Milan",
#       "position": "Attaquant",
#       "teams": {
#         "club": "Inter Milan",
#         "national_team": "Argentine"
#       },
#       "stats": {
#         "goals": 35,
#         "assists": 8,
#         "palmares": [
#           "Copa América",
#           "Serie A",
#           "Supercoppa Italiana"
#         ]
#       }
#     },
#     {
#       "player_id": "player_id_008",
#       "name": "Toni Kroos",
#       "age": 34,
#       "nationality": "Allemand",
#       "club": "Real Madrid",
#       "position": "Milieu",
#       "teams": {
#         "club": "Real Madrid",
#         "national_team": "Allemagne"
#       },
#       "stats": {
#         "goals": 1,
#         "assists": 12,
#         "palmares": [
#           "Champions League",
#           "La Liga",
#           "Supercopa de España"
#         ]
#       }
#     },
#     {
#       "player_id": "player_id_009",
#       "name": "Harry Kane",
#       "age": 31,
#       "nationality": "Anglais",
#       "club": "Bayern Munich",
#       "position": "Attaquant",
#       "teams": {
#         "club": "Bayern Munich",
#         "national_team": "Angleterre"
#       },
#       "stats": {
#         "goals": 52,
#         "assists": 14,
#         "palmares": []
#       }
#     },
#     {
#       "player_id": "player_id_010",
#       "name": "Phil Foden",
#       "age": 24,
#       "nationality": "Anglais",
#       "club": "Manchester City",
#       "position": "Attaquant",
#       "teams": {
#         "club": "Manchester City",
#         "national_team": "Angleterre"
#       },
#       "stats": {
#         "goals": 28,
#         "assists": 12,
#         "palmares": [
#           "Premier League",
#           "Club World Cup",
#           "UEFA Super Cup"
#         ]
#       }
#     },
#     {
#       "player_id": "player_id_011",
#       "name": "Lamine Yamal",
#       "age": 17,
#       "nationality": "Espagnole",
#       "club": "FC Barcelone",
#       "position": "Attaquant",
#       "teams": {
#         "club": "FC Barcelone",
#         "national_team": "Espagne"
#       },
#       "stats": {
#         "goals": 10,
#         "assists": 18,
#         "palmares": [
#           "Euro 2024"
#         ]
#       }
#     },
#     {
#       "player_id": "player_id_012",
#       "name": "Florian Wirtz",
#       "age": 21,
#       "nationality": "Allemand",
#       "club": "Bayer Leverkusen",
#       "position": "Milieu",
#       "teams": {
#         "club": "Bayer Leverkusen",
#         "national_team": "Allemagne"
#       },
#       "stats": {
#         "goals": 21,
#         "assists": 21,
#         "palmares": [
#           "Bundesliga",
#           "DFB-Pokal"
#         ]
#       }
#     },
#     {
#       "player_id": "player_id_013",
#       "name": "Nico Williams",
#       "age": 22,
#       "nationality": "Espagnol",
#       "club": "Athletic Club",
#       "position": "Attaquant",
#       "teams": {
#         "club": "Athletic Club",
#         "national_team": "Espagne"
#       },
#       "stats": {
#         "goals": 11,
#         "assists": 25,
#         "palmares": [
#           "Euro 2024",
#           "Copa del Rey"
#         ]
#       }
#     },
#     {
#       "player_id": "player_id_014",
#       "name": "Emiliano Martinez",
#       "age": 32,
#       "nationality": "Argentin",
#       "club": "Aston Villa",
#       "position": "Gardien de but",
#       "teams": {
#         "club": "Aston Villa",
#         "national_team": "Argentine"
#       },
#       "stats": {
#         "goals": 0,
#         "assists": 0,
#         "palmares": [
#           "Copa América"
#         ]
#       }
#     },
#     {
#       "player_id": "player_id_015",
#       "name": "Dani Olmo",
#       "age": 25,
#       "nationality": "Espagnol",
#       "club": "RB Leipzig",
#       "position": "Attaquant",
#       "teams": {
#         "club": "RB Leipzig",
#         "national_team": "Espagne"
#       },
#       "stats": {
#         "goals": 13,
#         "assists": 7,
#         "palmares": [
#           "Euro 2024",
#           "DFL-Supercup"
#         ]
#       }
#     }
#   ],
#   "voting": [
#     {
#       "user_id": "user_id_001",
#       "has_voted": True,
#       "response": "Vinicious Jr"
#     },
#     {
#       "user_id": "user_id_002",
#       "has_voted": False,
#       "response": "Rodri"
#     },
#     {
#       "user_id": "user_id_003",
#       "has_voted": True,
#       "response": "Kylian Mbappé"
#     }
#   ],
#   "end_date_display": "Lundi 16 Janvier 23:59",
#   "type_vote": "Vote Majoritaire"
# },
# {
#   "name_poll": "Élection des délégués",
#   "poll_question": "Qui souhaitez-vous élire comme délégué ?",
#   "poll_text": "Choisissez votre prochain délégué",
#   "poll_response": [
#     "Candidat 1",
#     "Candidat 2",
#     "Candidat 3",
#     "Candidat 4",
#     "Candidat 5"
#   ],
#   "created_by": "user_id_001",
#   "status": "Open",
#   "start_date": "2024-12-20",
#   "end_date": "2025-01-16",
#   "voting": [
#     {
#       "user_id": "user_id_001",
#       "has_voted": True,
#       "response": "Candidat 1"
#     },
#     {
#       "user_id": "user_id_002",
#       "has_voted": False,
#       "response": None
#     },
#     {
#       "user_id": "user_id_003",
#       "has_voted": True,
#       "response": "Candidat 2"
#     }
#   ],
#   "end_date_display": "Lundi 16 Janvier 23:59",
#   "type_vote": "Vote Majoritaire"
# },
# {
#   "name_poll": "Élections présidentielles 2017",
#   "poll_question": "Qui devrait être le président de la République ?",
#   "poll_text": "Votez pour le candidat de votre choix parmi les finalistes.",
#   "poll_response": [
#     "Candidat 1 - Emmanuel Macron",
#     "Candidat 2 - Marine Le Pen"
#   ],
#   "created_by": "user_id_002",
#   "status": "Open",
#   "start_date": "2024-12-20",
#   "end_date": "2025-01-16",
#   "voting": [
#     {
#       "user_id": "user_id_001",
#       "has_voted": True,
#       "response": "Candidat 1 - Emmanuel Macron"
#     },
#     {
#       "user_id": "user_id_002",
#       "has_voted": False,
#       "response": None
#     },
#     {
#       "user_id": "user_id_003",
#       "has_voted": True,
#       "response": "Candidat 2 - Marine Le Pen"
#     }
#   ],
#   "end_date_display": "Lundi 16 Janvier 23:59",
#   "type_vote": "Vote Majoritaire"
# },
# {
#   "name_poll": "Sélection du meilleur film de l'année",
#   "poll_question": "Quel est ton film préféré parmi ceux-ci ?",
#   "poll_text": "Votez pour le film qui vous a le plus marqué parmi la liste suivante.",
#   "poll_response": [
#     "American Gangster",
#     "Le Parrain",
#     "Le Crime de l'Orient-Express",
#     "Troie",
#     "The Batman",
#     "À couteaux tirés",
#     "Parasite (2019)",
#     "La Fureur du dragon",
#     "La Haine",
#     "Flight",
#     "Fight Club",
#     "Glass Onion",
#     "Mort sur le Nil",
#     "Casino Royale",
#     "300",
#     "Matrix",
#     "Scarface",
#     "Creed 3",
#     "Devotion (2022)",
#     "À la recherche du bonheur",
#     "Détective Dee"
#   ],
#   "created_by": "user_id_001",
#   "status": "Open",
#   "start_date": "2024-12-20",
#   "end_date": "2025-01-16",
#   "voting": [
#     {
#       "user_id": "user_id_001",
#       "has_voted": True,
#       "response": "Le Parrain"
#     },
#     {
#       "user_id": "user_id_002",
#       "has_voted": False,
#       "response": None
#     },
#     {
#       "user_id": "user_id_003",
#       "has_voted": True,
#       "response": "Fight Club"
#     }
#   ],
#   "end_date_display": "Lundi 16 Janvier 23:59",
#   "type_vote": "Vote Majoritaire"
# },
# {
#   "name_poll": "Prix du meilleur manga de l'année",
#   "poll_question": "Quel manga préférez-vous ?",
#   "poll_text": "Votez pour votre manga préféré parmi la liste suivante.",
#   "poll_response": [
#     "Détective Conan",
#     "Shamo",
#     "Eyeshield 21",
#     "Yuyu Hakusho",
#     "Full metal Alchemist",
#     "Bluelock",
#     "Dragon Ball",
#     "Death note",
#     "JoJo's Bizarre Adventure",
#     "Cowboy Bebop",
#     "Kuroko no Basket",
#     "Monster",
#     "Magi",
#     "Bouncer",
#     "Baki",
#     "K",
#     "Ao Ashi",
#     "Bungou Stray Dogs",
#     "Magic kaito",
#     "Enfer et Paradis",
#     "Psycho-Pass"
#   ],
#   "created_by": "user_id_001",
#   "status": "Open",
#   "start_date": "2024-12-20",
#   "end_date": "2025-01-16",
#   "voting": [
#     {
#       "user_id": "user_id_001",
#       "has_voted": True,
#       "response": "Shamo"
#     },
#     {
#       "user_id": "user_id_002",
#       "has_voted": False,
#       "response": None
#     },
#     {
#       "user_id": "user_id_003",
#       "has_voted": True,
#       "response": "Dragon Ball"
#     }
#   ],
#   "end_date_display": "Lundi 16 Janvier 23:59",
#   "type_vote": "Vote Majoritaire"
# },
# {
#   "name_poll": "Prix du meilleur livre",
#   "poll_question": "Quel est ton livre préféré parmi ceux-ci ?",
#   "poll_text": "Votez pour le livre qui vous a le plus marqué parmi la liste suivante.",
#   "poll_response": [
#     "Une étude en rouge",
#     "Double Assassinat dans la rue Morgue",
#     "Le Mystère de Marie Roget",
#     "Ainsi parlait Zarathoustra",
#     "L'antéchrist",
#     "Crime et Châtiment",
#     "L'étranger",
#     "Nutrition et dégénérescence physique",
#     "The Big Fat Surprise",
#     "L'alchimiste",
#     "Le Rouge et le Noir",
#     "Le Capital",
#     "L'Origine des espèces",
#     "A.B.C Contre Poirot",
#     "Oliver Twist",
#     "Le Portrait de Dorian Gray",
#     "Le Comte de Monte-Cristo",
#     "L'Art de la guerre",
#     "Toxic Superfoods",
#     "The Real Meal Revolution"
#   ],
#   "created_by": "user_id_001",
#   "voting": [
#     {
#       "user_id": "user_id_001",
#       "has_voted": True,
#       "response": "Crime et Châtiment"
#     },
#     {
#       "user_id": "user_id_002",
#       "has_voted": False,
#       "response": None
#     },
#     {
#       "user_id": "user_id_003",
#       "has_voted": True,
#       "response": "L'alchimiste"
#     }
#   ],
#   "status": "Open",
#   "start_date": "2024-12-20",
#   "end_date": "2025-01-16",
#   "participants": [
#     {
#       "book_id": 1,
#       "name": "Une étude en rouge",
#       "genre": "Fiction policière",
#       "author": "Arthur Conan Doyle"
#     },
#     {
#       "book_id": 2,
#       "name": "Double Assassinat dans la rue Morgue",
#       "genre": "Fiction policière",
#       "author": "Edgar Allan Poe"
#     },
#     {
#       "book_id": 3,
#       "name": "Le Mystère de Marie Roget",
#       "genre": "Fiction policière",
#       "author": "Edgar Allan Poe"
#     },
#     {
#       "book_id": 4,
#       "name": "Ainsi parlait Zarathoustra",
#       "genre": "Philosophie",
#       "author": "Friedrich Nietzsche"
#     },
#     {
#       "book_id": 5,
#       "name": "L'antéchrist",
#       "genre": "Philosophie",
#       "author": "Friedrich Nietzsche"
#     },
#     {
#       "book_id": 6,
#       "name": "Crime et Châtiment",
#       "genre": "Fiction psychologique",
#       "author": "Fiodor Dostoïevski"
#     },
#     {
#       "book_id": 7,
#       "name": "L'étranger",
#       "genre": "Fiction existentielle",
#       "author": "Albert Camus"
#     },
#     {
#       "book_id": 8,
#       "name": "Nutrition et dégénérescence physique",
#       "genre": "Santé et bien-être",
#       "author": "Weston Price"
#     },
#     {
#       "book_id": 9,
#       "name": "The Big Fat Surprise",
#       "genre": "Santé et bien-être",
#       "author": "Nina Teicholz"
#     },
#     {
#       "book_id": 10,
#       "name": "L'alchimiste",
#       "genre": "Roman d'aventure",
#       "author": "Paulo Coelho"
#     },
#     {
#       "book_id": 11,
#       "name": "Le Rouge et le Noir",
#       "genre": "Roman historique",
#       "author": "Stendhal"
#     },
#     {
#       "book_id": 12,
#       "name": "Le Capital",
#       "genre": "Économie",
#       "author": "Karl Marx"
#     },
#     {
#       "book_id": 13,
#       "name": "L'Origine des espèces",
#       "genre": "Science",
#       "author": "Charles Darwin"
#     },
#     {
#       "book_id": 14,
#       "name": "A.B.C Contre Poirot",
#       "genre": "Fiction policière",
#       "author": "Agatha Christie"
#     },
#     {
#       "book_id": 15,
#       "name": "Oliver Twist",
#       "genre": "Roman social",
#       "author": "Charles Dickens"
#     },
#     {
#       "book_id": 16,
#       "name": "Le Portrait de Dorian Gray",
#       "genre": "Fiction gothique",
#       "author": "Oscar Wilde"
#     },
#     {
#       "book_id": 17,
#       "name": "Le Comte de Monte-Cristo",
#       "genre": "Roman d'aventure",
#       "author": "Alexandre Dumas"
#     },
#     {
#       "book_id": 18,
#       "name": "L'Art de la guerre",
#       "genre": "Philosophie",
#       "author": "Sun Tzu"
#     },
#     {
#       "book_id": 19,
#       "name": "Toxic Superfoods",
#       "genre": "Santé et bien-être",
#       "author": "Nina Teicholz"
#     },
#     {
#       "book_id": 20,
#       "name": "The Real Meal Revolution",
#       "genre": "Santé et bien-être",
#       "author": "Tim Noakes, Sally-Ann Creed"
#     }
#   ],
#   "end_date_display": "Lundi 16 Janvier 23:59",
#   "type_vote": "Vote Majoritaire"
# },
# {
#   "name_poll": "Élection du plat gastronomique préféré",
#   "poll_question": "Quel est ton plat préféré parmi ceux-ci ?",
#   "poll_text": "Votez pour le plat qui vous plaît le plus parmi la liste suivante.",
#   "poll_response": [
#     "Canard laqué pékinois",
#     "Riz sauté aux crevettes",
#     "Dumplings de porc vapeur",
#     "Poulet aux noix de cajou et légumes",
#     "Le bouillon haïtien",
#     "Poulet en sauce créole",
#     "Légumes malanga et riz",
#     "Pain patate",
#     "Bacalhau à Brás",
#     "Caldeirada de peixe",
#     "Cozido à portuguesa",
#     "Pastéis de nata",
#     "Couscous aux légumes et viande d'agneau",
#     "Tajine de poulet aux olives",
#     "Mechoui (agneau rôti)",
#     "Chorba",
#     "Tajine de poulet aux citrons confits et olives",
#     "Couscous royal",
#     "Bastilla",
#     "Zaalouk"
#   ],
#   "created_by": "user_id_001",
#   "participants": [
#     {
#       "menu_id": "menu_001",
#       "name": "Canard laqué pékinois",
#       "country": "Chine"
#     },
#     {
#       "menu_id": "menu_002",
#       "name": "Riz sauté aux crevettes",
#       "country": "Chine"
#     },
#     {
#       "menu_id": "menu_003",
#       "name": "Dumplings de porc vapeur",
#       "country": "Chine"
#     },
#     {
#       "menu_id": "menu_004",
#       "name": "Poulet aux noix de cajou et légumes",
#       "country": "Chine"
#     },
#     {
#       "menu_id": "menu_005",
#       "name": "Le bouillon haïtien",
#       "country": "Haïti"
#     },
#     {
#       "menu_id": "menu_006",
#       "name": "Poulet en sauce créole",
#       "country": "Haïti"
#     },
#     {
#       "menu_id": "menu_007",
#       "name": "Légumes malanga et riz",
#       "country": "Haïti"
#     },
#     {
#       "menu_id": "menu_008",
#       "name": "Pain patate",
#       "country": "Haïti"
#     },
#     {
#       "menu_id": "menu_009",
#       "name": "Bacalhau à Brás",
#       "country": "Portugal"
#     },
#     {
#       "menu_id": "menu_010",
#       "name": "Caldeirada de peixe",
#       "country": "Portugal"
#     },
#     {
#       "menu_id": "menu_011",
#       "name": "Cozido à portuguesa",
#       "country": "Portugal"
#     },
#     {
#       "menu_id": "menu_012",
#       "name": "Pastéis de nata",
#       "country": "Portugal"
#     },
#     {
#       "menu_id": "menu_013",
#       "name": "Couscous aux légumes et viande d'agneau",
#       "country": "Maroc"
#     },
#     {
#       "menu_id": "menu_014",
#       "name": "Tajine de poulet aux olives",
#       "country": "Maroc"
#     },
#     {
#       "menu_id": "menu_015",
#       "name": "Mechoui (agneau rôti)",
#       "country": "Maroc"
#     },
#     {
#       "menu_id": "menu_016",
#       "name": "Chorba",
#       "country": "Algérie"
#     },
#     {
#       "menu_id": "menu_017",
#       "name": "Tajine de poulet aux citrons confits et olives",
#       "country": "Maroc"
#     },
#     {
#       "menu_id": "menu_018",
#       "name": "Couscous royal",
#       "country": "Maroc"
#     },
#     {
#       "menu_id": "menu_019",
#       "name": "Bastilla",
#       "country": "Maroc"
#     },
#     {
#       "menu_id": "menu_020",
#       "name": "Zaalouk",
#       "country": "Maroc"
#     }
#   ],
#   "status": "Open",
#   "start_date": "2024-12-20",
#   "end_date": "2025-01-16",
#   "voting": [
#     {
#       "user_id": "user_id_001",
#       "has_voted": True,
#       "response": "Canard laqué pékinois"
#     },
#     {
#       "user_id": "user_id_002",
#       "has_voted": False,
#       "response": None
#     },
#     {
#       "user_id": "user_id_003",
#       "has_voted": True,
#       "response": "Riz sauté aux crevettes"
#     }
#   ],
#   "end_date_display": "Lundi 16 Janvier 23:59",
#   "type_vote": "Vote Majoritaire"
# },
# {
#   "name_poll": "Récompense de la meilleure série TV",
#   "poll_question": "Quelle est ta série préférée parmi celles-ci ?",
#   "poll_text": "Choisis la série que tu préfères.",
#   "poll_response": [
#     "Sherlock",
#     "La Traque dans le sang",
#     "Vikings",
#     "Game of Thrones",
#     "Power",
#     "Snowfall",
#     "Breaking Bad",
#     "Narcos",
#     "Prison Break",
#     "Peaky Blinders",
#     "Mad Men",
#     "Euphoria",
#     "The Walking Dead",
#     "Black Mirror",
#     "Mindhunter",
#     "The Boys",
#     "Gomorrah",
#     "The Bear",
#     "Luther",
#     "Outer Banks",
#     "Riverdale"
#   ],
#   "created_by": "user_id_001",
#   "status": "Open",
#   "start_date": "2024-12-20",
#   "end_date": "2025-01-16",
#   "voting": [
#     {
#       "user_id": "user_id_001",
#       "has_voted": True,
#       "response": "Breaking Bad"
#     },
#     {
#       "user_id": "user_id_002",
#       "has_voted": False,
#       "response": None
#     },
#     {
#       "user_id": "user_id_003",
#       "has_voted": True,
#       "response": "Sherlock"
#     }
#   ],
#   "end_date_display": "Lundi 16 Janvier 23:59",
#   "type_vote": "Vote Majoritaire"
# },
# {
#   "name_poll": "Élection de la meilleure équipe de football",
#   "poll_question": "Quelle est ton équipe de football préférée parmi celles-ci ?",
#   "poll_text": "Votez pour l'équipe qui vous passionne le plus.",
#   "poll_response": [
#     "Manchester United",
#     "Paris Saint-Germain",
#     "Borussia Dortmund",
#     "Real Madrid Club de Fútbol",
#     "Chelsea Football Club",
#     "Atlético Madrid",
#     "SSC Napoli",
#     "Bayer 04 Leverkusen",
#     "Inter Milan",
#     "FC Barcelone",
#     "LOSC Lille",
#     "Bayern Munich",
#     "Sporting Clube",
#     "Arsenal Football Club",
#     "AC Milan",
#     "Liverpool Football Club",
#     "Tottenham Hotspur Football Club",
#     "Juventus Football Club",
#     "Olympique de Marseille",
#     "Benfica Lisbonne"
#   ],
#   "created_by": "user_id_001",
#   "status": "Open",
#   "start_date": "2024-12-20",
#   "end_date": "2025-01-16",
#   "voting": [
#     {
#       "user_id": "user_id_001",
#       "has_voted": True,
#       "response": "Manchester United"
#     },
#     {
#       "user_id": "user_id_002",
#       "has_voted": False,
#       "response": None
#     },
#     {
#       "user_id": "user_id_003",
#       "has_voted": True,
#       "response": "Paris Saint-Germain"
#     }
#   ],
#   "end_date_display": "Lundi 16 Janvier 23:59",
#   "type_vote": "Vote Majoritaire"
# },
# {
#   "name_poll": "Quelle destination rêvez-vous de visiter en 2025 ?",
#   "poll_question": "Parmi ces pays, lequel choisiriez-vous pour votre prochain voyage ?",
#   "poll_text": "Votez pour la destination de vos rêves et partagez votre passion pour le voyage.",
#   "poll_response": [
#     "Panama",
#     "Etats-Unis",
#     "Chine",
#     "Maroc",
#     "Cameroun",
#     "Algérie",
#     "Portugal",
#     "Haïti",
#     "Japon",
#     "Pays-Bas",
#     "Canada",
#     "République-Dominicaine",
#     "Brésil",
#     "Côte-d'Ivoire",
#     "République démocratique du Congo",
#     "Tunisie",
#     "Indonésie",
#     "Thaïlande"
#   ],
#   "created_by": "user_id_001",
#   "voting": [
#     {
#       "user_id": "user_id_001",
#       "has_voted": True,
#       "response": "Haïti"
#     },
#     {
#       "user_id": "user_id_002",
#       "has_voted": False,
#       "response": None
#     },
#     {
#       "user_id": "user_id_003",
#       "has_voted": True,
#       "response": "Chine"
#     }
#   ],
#   "status": "Open",
#   "start_date": "2024-12-20",
#   "end_date": "2025-01-16",
#   "end_date_display": "Lundi 16 Janvier 23:59",
#   "type_vote": "Vote Majoritaire"
# }]
    
#     for ballot in ballots:
#         # Vérifier si le document existe déjà avec le poll_name unique
#         if target_collection.count_documents({"name_poll": ballot["name_poll"]}) == 0:
#             target_collection.insert_one(ballot)
#             print(f"Document inséré : {ballot}")
#         else:
#             print(f"Document déjà existant : {ballot['name_poll']}")


# if __name__ == "__main__":
#   write_data()

 