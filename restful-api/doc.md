# Doc sur les API RESTful

## 1. Introduction aux API RESTful

Les API RESTful (Representational State Transfer) sont des services web permettant une communication stateless entre un client et un serveur via le protocole HTTP. Elles sont largement utilisées en raison de leur simplicité et de leur compatibilité avec de nombreux systèmes.

### Ressources :
- [Introduction aux API RESTful - OpenClassrooms](https://openclassrooms.com/fr/courses/6573181-concevez-des-api-restful-avec-symfony/6573187-decouvrez-les-api-restful)

## 2. Comprendre le protocole HTTP/HTTPS

HTTP (HyperText Transfer Protocol) est un protocole de communication permettant d'échanger des informations sur le Web. HTTPS (HTTP Secure) est une version sécurisée utilisant SSL/TLS pour chiffrer les échanges.

### Principales méthodes HTTP :
- `GET` : Récupérer des données depuis un serveur
- `POST` : Envoyer des données au serveur
- `PUT` : Mettre à jour une ressource
- `DELETE` : Supprimer une ressource

### Ressources :
- [Le protocole HTTP sur Wikipédia](https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
- [Comprendre HTTPS - SSL France](https://www.sslfrance.com/https/)

## 3. Tester une API depuis la ligne de commande

Utiliser `cURL` ou `httpie` permet d'interagir avec une API directement en ligne de commande.

Exemple avec `cURL` :
```sh
curl -X GET https://jsonplaceholder.typicode.com/posts/1
```

### Ressources :
- [Utiliser cURL pour tester des API REST - Dev.to](https://dev.to/abderrahmane_hadjou/utiliser-curl-pour-tester-des-api-rest-1flc)

## 4. Consommation d'une API avec Python

Python permet de consommer des API facilement avec la bibliothèque `requests` :

```python
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.json())
```

### Ressources :
- [Utiliser l'API Requests de Python - OpenClassrooms](https://openclassrooms.com/fr/courses/4425126-perfectionnez-vous-en-python/4459541-utilisez-lapi-requests)

## 5. Développement d'une API avec `http.server`

Python dispose du module `http.server` pour créer rapidement un serveur HTTP minimaliste :

```sh
python -m http.server 8000
```

### Ressources :
- [Le module http.server de Python](https://docs.python.org/fr/3/library/http.server.html)

## 6. Développement d'une API avec Flask

Flask est un micro-framework Python permettant de créer des API RESTful légères et flexibles.

Exemple d'API simple avec Flask :
```python
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(debug=True)
```

### Ressources :
- [Développez votre application web avec Flask - OpenClassrooms](https://openclassrooms.com/fr/courses/4425061-developpez-votre-application-web-avec-flask)

## 7. Sécurisation et authentification des API

Il est essentiel de sécuriser une API via HTTPS et des mécanismes d'authentification comme :
- JWT (JSON Web Tokens)
- OAuth2
- API Keys

Exemple de protection avec Flask :
```python
from flask import Flask, request, jsonify

app = Flask(__name__)
API_KEY = "mon_secret_key"

@app.route("/secure-data")
def secure_data():
    if request.headers.get("X-API-KEY") == API_KEY:
        return jsonify({"data": "Accès autorisé"})
    return jsonify({"error": "Accès refusé"}), 403

if __name__ == "__main__":
    app.run(debug=True)
```

### Ressources :
- [Sécuriser une API REST avec Flask](https://flask-restful.readthedocs.io/en/latest/intermediate-usage.html#authentication)

## 8. Standards et documentation avec OpenAPI

OpenAPI permet de documenter une API REST de manière standardisée.

Exemple de documentation en YAML :
```yaml
openapi: 3.0.0
info:
  title: API Exemple
  version: 1.0.0
paths:
  /api:
    get:
      summary: Récupère un message
      responses:
        '200':
          description: Succès
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
```

### Ressources :
- [Introduction à OpenAPI - OpenClassrooms](https://openclassrooms.com/fr/courses/6573181-concevez-des-api-restful-avec-symfony/6573194-documentez-votre-api-avec-openapi)
