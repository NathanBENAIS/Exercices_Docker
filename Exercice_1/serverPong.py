from flask import Flask, jsonify
adresse_IP = '127.0.0.1'
app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    # Traitez la requête ping du serveur "ping"
    # return jsonify({"message": "pong"})
     return "pong"

if __name__ == '__main__':
    app.run(host=adresse_IP, port=5000)
