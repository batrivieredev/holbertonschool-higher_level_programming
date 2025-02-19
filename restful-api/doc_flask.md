# API REST avec Flask

Ce projet implémente une API REST simple avec Flask, permettant de gérer des utilisateurs en mémoire. Vous pouvez l'utiliser pour ajouter, récupérer et lister des utilisateurs, ainsi que vérifier l'état du serveur.

## 📌 Fonctionnalités

- **Ajouter un utilisateur** (POST `/add_user`)
- **Récupérer les informations d'un utilisateur** (GET `/users/<username>`)
- **Lister les utilisateurs** (GET `/data`)
- **Vérifier l'état du serveur** (GET `/status`)
- **Route d'accueil** (GET `/`)

---

## 🚀 Prérequis

Avant de commencer, assurez-vous d'avoir installé les dépendances suivantes :

- [Python 3.x](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)

### Installation de Flask :

```bash
pip install Flask
```

---

## 📂 Structure du projet

```
/api
  ├── app.py          # Le fichier principal de l'application Flask
  └── README.md       # Ce fichier
```

---

## ▶️ Utilisation

### 1️⃣ Lancer l'application

Exécutez la commande suivante pour démarrer l'application :

```bash
python app.py
```

Cela démarrera le serveur Flask sur [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### 2️⃣ Routes disponibles

#### Route d'accueil
- **URL** : `/`
- **Méthode** : `GET`
- **Description** : Affiche un message de bienvenue.

#### Lister les utilisateurs
- **URL** : `/data`
- **Méthode** : `GET`
- **Description** : Retourne la liste des noms d'utilisateurs sous forme de JSON.

#### Vérifier l'état du serveur
- **URL** : `/status`
- **Méthode** : `GET`
- **Description** : Retourne "OK" indiquant que le serveur fonctionne.

#### Récupérer les infos d'un utilisateur
- **URL** : `/users/<username>`
- **Méthode** : `GET`
- **Description** : Retourne les informations d'un utilisateur spécifique.

#### Ajouter un utilisateur
- **URL** : `/add_user`
- **Méthode** : `POST`
- **Description** : Ajoute un utilisateur avec des données JSON.

##### Exemple de requête :

```bash
curl -X POST http://127.0.0.1:5000/add_user \
     -H "Content-Type: application/json" \
     -d '{"username": "john", "name": "John Doe", "age": 30, "city": "Paris"}'
```

---

## 🛠️ Tester l'API avec curl

#### Vérifier que le serveur fonctionne :
```bash
curl http://127.0.0.1:5000/status
```

#### Obtenir la liste des utilisateurs :
```bash
curl http://127.0.0.1:5000/data
```

#### Récupérer les infos d'un utilisateur :
```bash
curl http://127.0.0.1:5000/users/john
```

#### Tester un utilisateur inexistant :
```bash
curl http://127.0.0.1:5000/users/mike
```

---

## 💻 Code de l'application

### Initialisation de l'application Flask

```python
from flask import Flask, jsonify, request

app = Flask(__name__)
```

### Stockage des Données

Les utilisateurs sont stockés dans un dictionnaire Python en mémoire.

```python
users = {}
```

### Définition des Routes

#### Route d'Accueil (GET /)

```python
@app.route('/')
def home():
    return "Welcome to the Flask API!"
```

#### Lister les utilisateurs (GET /data)

```python
@app.route('/data')
def json_response():
    user = list(users.keys())
    return jsonify(user)
```

#### Vérifier l'état du Serveur (GET /status)

```python
@app.route('/status')
def status():
    return "OK"
```

#### Récupérer les Infos d'un Utilisateur (GET /users/<username>)

```python
@app.route('/users/<username>')
def user_data(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])
```

#### Ajouter un Utilisateur (POST /add_user)

```python
@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = request.get_json()
    if 'username' not in new_user:
        return jsonify({"error": "Username is required"}), 400
    username = new_user['username']
    users[username] = {
        "username": new_user.get('username'),
        "name": new_user.get('name'),
        "age": new_user.get('age'),
        "city": new_user.get('city')
    }
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201
```

### Exécution de l'Application

Lancez l'application Flask avec la commande suivante :

```python
if __name__ == "__main__":
    app.run()
```

---
