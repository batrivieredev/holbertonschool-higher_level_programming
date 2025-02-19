# API REST avec Flask

Ce projet implémente une API REST simple avec Flask, permettant de gérer des utilisateurs en mémoire. Vous pouvez l'utiliser pour ajouter, récupérer et lister des utilisateurs, ainsi que vérifier l'état du serveur.

## Fonctionnalités

- **Ajouter un utilisateur** (POST `/add_user`)
- **Récupérer les informations d'un utilisateur** (GET `/users/<username>`)
- **Lister les utilisateurs** (GET `/data`)
- **Vérifier l'état du serveur** (GET `/status`)
- **Route d'accueil** (GET `/`)

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les dépendances suivantes :

- [Python 3.x](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)

Installation de Flask :
```bash
pip install Flask
```

## Structure du projet
```
/api
  ├── app.py          # Le fichier principal de l'application Flask
  └── README.md       # Ce fichier
```

## Utilisation

### 1. Lancer l'application
Exécutez la commande suivante pour démarrer l'application :
```bash
python app.py
```
Cela démarrera le serveur Flask sur `http://127.0.0.1:5000/`.

### 2. Routes disponibles

#### Route d'accueil
- **URL :** `/`
- **Méthode :** GET
- **Description :** Affiche un message de bienvenue.

#### Lister les utilisateurs
- **URL :** `/data`
- **Méthode :** GET
- **Description :** Retourne la liste des noms d'utilisateurs sous forme de JSON.

#### Vérifier l'état du serveur
- **URL :** `/status`
- **Méthode :** GET
- **Description :** Retourne "OK" indiquant que le serveur fonctionne.

#### Récupérer les infos d'un utilisateur
- **URL :** `/users/<username>`
- **Méthode :** GET
- **Description :** Retourne les informations d'un utilisateur spécifique.

#### Ajouter un utilisateur
- **URL :** `/add_user`
- **Méthode :** POST
- **Description :** Ajoute un utilisateur avec des données JSON.
- **Exemple de requête :**
```bash
curl -X POST http://127.0.0.1:5000/add_user \
     -H "Content-Type: application/json" \
     -d '{"username": "john", "name": "John Doe", "age": 30, "city": "Paris"}'
```

## Tester l'API avec `curl`

Vérifier que le serveur fonctionne :
```bash
curl http://127.0.0.1:5000/status
```

Obtenir la liste des utilisateurs :
```bash
curl http://127.0.0.1:5000/data
```

Récupérer les infos d'un utilisateur :
```bash
curl http://127.0.0.1:5000/users/john
```

Tester un utilisateur inexistant :
```bash
curl http://127.0.0.1:5000/users/mike
```

## Améliorations Possibles

- **Utilisation d'une base de données :** Actuellement, les données sont stockées en mémoire. Pour les rendre persistantes, vous pouvez utiliser SQLite avec SQLAlchemy.
- **Ajout d'authentification :** On peut protéger certaines routes en utilisant Flask-Login ou JWT.
- **Ajout d'une route DELETE :** Une route DELETE `/users/<username>` permettrait de supprimer un utilisateur.

N'hésitez pas à contribuer et à améliorer ce projet ! 🎉
