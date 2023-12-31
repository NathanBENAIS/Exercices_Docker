from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
server_ping_url = "http://localhost:5372"

def send_ping():
    while True:
        time.sleep(0.5)
        try:
            response = requests.get(server_ping_url + "/ping")
            print("Server Ping received ping from Server Pong:", response.text)
        except requests.exceptions.RequestException as e:
            print("Error sending ping:", e)

@app.route('/pong')
def pong():
    return "pong"

if __name__ == '__main__':
    ping_thread = Thread(target=send_ping)
    ping_thread.start()    
    app.run(port=4567)