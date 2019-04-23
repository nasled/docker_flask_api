from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_mongoalchemy import MongoAlchemy
import os


app = Flask(__name__)
app.config['MONGOALCHEMY_SERVER'] = os.environ.get('DOCKER_MONGO_HOSTNAME')
app.config['MONGOALCHEMY_DATABASE'] = "mongodb"

api = Api(app)
db = MongoAlchemy(app)


'''
Document Structure
'''
class Book(db.Document):
    name = db.StringField()
    title = db.StringField()
    year = db.IntField()

'''
Endpoints
'''
class ApiIndexCall(Resource):
    def get(self):
        endoints = {}
        endoints['/list'] = 'latest data list'
        endoints['/save'] = 'save data to the endpoint'
        endoints['/get/<string:id>'] = 'get unique entry by id'
        return jsonify(enpoints=endoints)

class ApiListCall(Resource):
    def get(self):
        res = []
        data = Book.query.all()
        for d in data:
           res.append(d.title)
        return jsonify(data=res)

class ApiGetCall(Resource):
    def get(self, id):
        data = Book.query.filter(Book.year == int(id)).first()
        return jsonify(data=data.title)

class ApiSaveCall(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        dive = Book(title='Dive Into Python', year=2004, name='Mark Pilgrim')
        dive.save()
        return jsonify(data=json_data)

'''
Routes
'''
api.add_resource(ApiIndexCall, '/')
api.add_resource(ApiGetCall, '/get/<string:id>')
api.add_resource(ApiListCall, '/list')
api.add_resource(ApiSaveCall, '/save')