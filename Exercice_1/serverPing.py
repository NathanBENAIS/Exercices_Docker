import requests
import time

adresse_IP_pong = '127.0.0.1'  # Remplacez ceci par l'adresse IP réelle du serveur "pong"

def send_ping():
    while True:
        print("Envoi d'une requête 'ping'")
        response = requests.get(f'http://{adresse_IP_pong}:5000/ping')
        
        if response.text == 'pong':
            print("Reçu 'pong'")
            time.sleep(0.5)  # Attendre une demi-seconde
            print("Envoi d'une requête 'pong'")
            requests.get(f'http://{adresse_IP_pong}:5000/pong')
            # Envoyer une requête "pong" au serveur "pong"
            # puis continuer à attendre pour envoyer un nouveau "ping"

if __name__ == '__main__':
    send_ping()
