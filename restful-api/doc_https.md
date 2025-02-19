# Simple API en Python

Ce projet est une API HTTP simple écrite en Python en utilisant le module `http.server`. Elle fournit plusieurs endpoints pour retourner des réponses en texte et en JSON.

## Prérequis
- Python 3 installé sur votre machine

## Installation
Aucune installation de dépendances supplémentaires n'est requise. Assurez-vous simplement d'avoir Python 3 installé.

## Utilisation
1. Téléchargez le fichier Python.
2. Exécutez la commande suivante pour démarrer le serveur :
   ```bash
   python3 script.py
   ```
3. Le serveur s'exécute par défaut sur le port `8000`.

## Endpoints disponibles
| Méthode | Endpoint   | Description |
|---------|-----------|-------------|
| GET     | `/`       | Retourne un message d'accueil. |
| GET     | `/data`   | Retourne des données JSON avec un nom, un âge et une ville. |
| GET     | `/status` | Retourne un message de statut "OK". |

## Comment créer ce code pas à pas

1. **Importer les modules nécessaires**
   - `http.server` pour gérer le serveur HTTP.
   - `json` pour manipuler les données JSON.

   ```python
   import json
   from http.server import BaseHTTPRequestHandler, HTTPServer
   ```

2. **Créer une classe qui hérite de `BaseHTTPRequestHandler`**
   - Cette classe servira à gérer les requêtes entrantes.
   - Redéfinir la méthode `do_GET()` pour répondre aux requêtes GET.

   ```python
   class SimpleAPI(BaseHTTPRequestHandler):
       def do_GET(self):
           # Gestion de favicon pour éviter les erreurs 404
           if self.path == '/favicon.ico':
               self.send_response(204)
               self.end_headers()
               return
   ```

3. **Gérer différents endpoints**
   - Définir des conditions pour retourner différentes réponses en fonction du chemin demandé.
   
   ```python
           if self.path == '/':
               self.send_response(200)
               self.send_header('Content-type', 'text/html')
               self.end_headers()
               self.wfile.write(b"Hello, this is a simple API!")
           elif self.path == '/data':
               self.send_response(200)
               self.send_header('Content-type', 'application/json')
               self.end_headers()
               data = {
                   "name": "John",
                   "age": 30,
                   "city": "New York"
               }
               self.wfile.write(json.dumps(data).encode())
           elif self.path == '/status':
               self.send_response(200)
               self.send_header('Content-type', 'text/plain')
               self.end_headers()
               self.wfile.write(b"OK")
           else:
               self.send_response(404)
               self.send_header('Content-type', 'text/plain')
               self.end_headers()
               self.wfile.write(b"Endpoint not found")
   ```

4. **Créer et exécuter le serveur HTTP**
   - Définir une fonction `run()` qui instancie un serveur HTTP.

   ```python
   def run(server_class=HTTPServer, handler_class=SimpleAPI, port=8000):
       server_address = ('', port)
       httpd = server_class(server_address, handler_class)
       print(f'Starting simple API server on port {port}...')
       httpd.serve_forever()
   ```

5. **Exécuter le script**
   - Vérifier que le script s'exécute uniquement en tant que programme principal.
   
   ```python
   if __name__ == '__main__':
       run()
   ```

## Débogage
Si vous rencontrez des problèmes :
- Vérifiez que le port `8000` n'est pas déjà utilisé par une autre application.
- Testez les endpoints avec `curl` ou un navigateur.
- Ajoutez des impressions (`print()`) dans le code pour suivre les requêtes reçues.

## Déploiement
Pour déployer cette API en production :
- Utilisez un serveur web comme `gunicorn` ou `uwsgi`.
- Configurez un proxy inverse avec `nginx` ou `Apache`.
- Hébergez l'API sur un service cloud comme AWS, GCP ou un VPS.

## Sécurité
- Évitez d'exposer cette API directement sur internet sans configuration supplémentaire.
- Ajoutez des logs pour suivre les requêtes et détecter d'éventuels abus.
- Implémentez des contrôles d'accès si nécessaire.

## Arrêt du serveur
Pour arrêter le serveur, utilisez `CTRL + C` dans le terminal où il est exécuté.

## Ressources supplémentaires
- [Documentation officielle de http.server](https://docs.python.org/3/library/http.server.html)
- [Tutoriel sur les serveurs HTTP en Python](https://realpython.com/python-http-server/)
--- 
