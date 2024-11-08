from flask import Flask, jsonify
from waitress import serve

app = Flask(__name__)

# Dados simulados para emular um LIS
local_data = {
    "id": 1,
    "name": "Localização X",
    "coordinates": {"lat": 40.7128, "lon": -74.0060},  # Exemplo: coordenadas de NY
    "status": "ativo"
}

@app.route('/lis', methods=['GET'])
def get_lis_data():
    return jsonify(local_data)

if __name__ == "__main__":
    # Usando o Waitress para servir a aplicação
    serve(app, host='0.0.0.0', port=5000)