from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_mongoalchemy import MongoAlchemy
import os


app = Flask(__name__)
app.config['MONGOALCHEMY_SERVER'] = os.environ.get('DOCKER_MONGO_HOSTNAME')
# app.config['MONGOALCHEMY_SERVER'] = "localhost"
app.config['MONGOALCHEMY_DATABASE'] = "mongodb"

api = Api(app)
db = MongoAlchemy(app)


'''
Document Structure
'''


class Car (db.Document):
    title = db.StringField()
    drive_type = db.StringField()
    transmission = db.StringField()
    engine_size = db.FloatField(min_value=0)
    year = db.IntField(min_value=0)
    cylinders = db.IntField(min_value=0)
    width = db.FloatField(min_value=0)
    height = db.FloatField(min_value=0)
    weight = db.IntField(min_value=0)


'''
Endpoints
'''


class ApiIndexCall(Resource):
    def get(self):
        return jsonify(enpoints={
            '/list': 'display a collection of records',
            '/get/<string:id>': 'display a single record that the corresponds to an ID',
            '/save': 'create a record'
        })


class ApiListCall(Resource):
    def get(self):
        result = {}
        try:
            cars = Car.query.all()
            list = []
            for car in cars:
                list.append({
                    'mongo_id': str(car.mongo_id),
                    'title': car.title,
                    'drive_type': car.drive_type,
                    'transmission': car.transmission,
                    'engine_size': car.engine_size,
                    'year': car.year,
                    'cylinders': car.cylinders,
                    'width': car.width,
                    'height': car.height,
                    'weight': car.weight
                })
            result['data'] = list
            result['error'] = False

        except Exception as e:
            result['description'] = str(e)
            result['error'] = True

        return jsonify(result)


class ApiGetCall(Resource):
    def get(self, id):
        result = {}
        try:
            car = Car.query.filter(Car.mongo_id == str(id)).first()
            result['data'] = {
                'mongo_id': str(car.mongo_id),
                'title': car.title,
                'drive_type': car.drive_type,
                'transmission': car.transmission,
                'engine_size': car.engine_size,
                'year': car.year,
                'cylinders': car.cylinders,
                'width': car.width,
                'height': car.height,
                'weight': car.weight
            }
            result['error'] = False

        except Exception as e:
            result['description'] = str(e)
            result['error'] = True

        return jsonify(result)


class ApiSaveCall(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        result = {}

        try:
            model = Car(title=json_data['title'],
                        drive_type=json_data['drive_type'],
                        transmission=json_data['transmission'],
                        engine_size=json_data['engine_size'],
                        year=json_data['year'],
                        cylinders=json_data['cylinders'],
                        width=json_data['width'],
                        height=json_data['height'],
                        weight=json_data['weight'])
            model.save()
            result['mongo_id'] = str(model.mongo_id)
            result['error'] = False

        except Exception as e:
            result['description'] = str(e)
            result['error'] = True

        return jsonify(result)


'''
Routes
'''
api.add_resource(ApiIndexCall, '/')
api.add_resource(ApiGetCall, '/get/<string:id>')
api.add_resource(ApiListCall, '/list')
api.add_resource(ApiSaveCall, '/save')