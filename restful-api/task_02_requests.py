#!/usr/bin/env python3

import requests
import csv

# Fonction pour récupérer et afficher les titres des posts depuis l'API
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Affichage du statut de la requête
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        # Parcours et affichage des titres des posts
        for post in posts:
            print(post['title'])
    else:
        print("Échec de la récupération des posts.")

# Fonction pour récupérer les posts et les enregistrer dans un fichier CSV
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        # Structuration des données sous forme de liste de dictionnaires
        data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        # Écriture des données dans un fichier CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)

        print("Données sauvegardées avec succès dans posts.csv")
    else:
        print("Échec de la récupération des posts.")
