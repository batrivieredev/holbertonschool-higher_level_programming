#!/usr/bin/env python3

# Importation des modules nécessaires
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Définition de la classe de gestion des requêtes HTTP
class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Gère les requêtes GET et renvoie différentes réponses en fonction de l'URL demandée.
        """
        if self.path == '/':
            # Réponse pour la racine du serveur
            self.send_response(200)  # Code HTTP 200 (OK)
            self.send_header("Content-type", "text/plain")  # Définition du type de contenu
            self.end_headers()  # Fin de l'envoi des en-têtes
            self.wfile.write(b"Hello, this is a simple API!")  # Envoi du message

        elif self.path == '/data':
            # Réponse JSON pour l'endpoint /data
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}  # Données JSON
            self.wfile.write(json.dumps(data).encode('utf-8'))  # Conversion et envoi des données

        elif self.path == '/status':
            # Réponse JSON pour vérifier le statut de l'API
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode('utf-8'))

        elif self.path == '/info':
            # Réponse JSON avec des informations sur l'API
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            # Réponse pour les URLs non définies (404 Not Found)
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode('utf-8'))

# Fonction pour démarrer le serveur HTTP
def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Démarre un serveur HTTP sur le port spécifié."""
    server_address = ('', port)  # Adresse et port d'écoute
    httpd = server_class(server_address, handler_class)
    print(f"Serveur démarré sur le port {port}")
    httpd.serve_forever()  # Boucle infinie pour écouter les requêtes

# Exécute le serveur si le script est lancé directement
if __name__ == "__main__":
    run()
