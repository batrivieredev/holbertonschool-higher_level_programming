import socket  # Module utilisé pour la communication réseau
import json  # Module utilisé pour la sérialisation et désérialisation des données

def start_server(host='127.0.0.1', port=65432):  # Fonction serveur qui écoute et traite les connexions
    """Starts a server that listens for incoming connections and processes received data."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()  # Le serveur commence à écouter les connexions entrantes
        print(f"Server listening on {host}:{port}")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024)  # Réception des données envoyées par le client
            if data:
                received_dict = json.loads(data.decode('utf-8'))
                print("Received Dictionary from Client:")
                print(received_dict)

def send_data(data, host='127.0.0.1', port=65432):  # Fonction client qui envoie des données au serveur
    """Sends a serialized dictionary to the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        serialized_data = json.dumps(data).encode('utf-8')  # Sérialisation des données avant l'envoi
        client_socket.sendall(serialized_data)
        print("Data sent to server.")
