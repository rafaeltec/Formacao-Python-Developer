from flask import Flask, jsonify
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Iniciar ngrok quando o app for iniciado

# Dados simulados baseados na planilha
data = [
    {"Number": 1, "Name": "Mahesh", "Age": 25, "City": "Bangalore", "Country": "India"},
    {"Number": 2, "Name": "Alex", "Age": 26, "City": "London", "Country": "UK"},
    {"Number": 3, "Name": "David", "Age": 27, "City": "San Francisco", "Country": "USA"},
    {"Number": 4, "Name": "John", "Age": 28, "City": "Toronto", "Country": "Canada"},
    {"Number": 5, "Name": "Chris", "Age": 29, "City": "Paris", "Country": "France"}
]

@app.route('/index')
def index():
    return jsonify(data)

if __name__ == '__main__':
    app.run()
