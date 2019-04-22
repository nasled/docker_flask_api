from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "API endpoints usage: /entries or /entry/<id>"

@app.route("/entry/<int:id>", methods=['GET'])
def get_entry(id):
    return jsonify(id=id, title="title")

@app.route("/entries", methods=['GET'])
def get_entries():
    data = {"id": str(id), "title": "title"}
    return jsonify([data,data,data])