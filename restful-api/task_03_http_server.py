#!/usr/bin/python3

# Importation des modules nécessaires
import http.server  # Module pour créer un serveur HTTP
import socketserver  # Module pour gérer les connexions réseau
import json  # Module pour manipuler des données JSON

# Définition d'un gestionnaire de requêtes HTTP
class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Gère les requêtes GET et renvoie des réponses différentes selon l'URL demandée.
        """
        if self.path == '/':
            # Réponse pour la racine du serveur
            self.send_response(200)  # Envoi du code HTTP 200
            self.send_header('Content-type', 'text/html')  # Définition du type de contenu
            self.end_headers()  # Fin de l'envoi des en-têtes
            self.wfile.write(b"Hello, this is a simple API!")  # Envoi du message

        elif self.path == '/data':
            # Réponse JSON pour l'endpoint /data
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}  # Données JSON
            self.wfile.write(json.dumps(data).encode())  # Conversion et envoi des données

        elif self.path == '/status':
            # Réponse pour l'endpoint /status indiquant que l'API fonctionne
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            # Réponse pour les URLs non définies
            self.send_error(404, "Endpoint not found")

# Vérification si le script est exécuté directement
if __name__ == "__main__":
    PORT = 8000  # Port sur lequel le serveur écoutera
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Serving at port {PORT}")  # Affichage du port utilisé
        httpd.serve_forever()  # Boucle infinie pour écouter les requêtes
