from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

models = []

# Dummy-Daten für Modell-Items
models.append({"id": 1, "name": "Model 1", "werk": 42})
models.append({"id": 2, "name": "Model 2", "werk": 42})

class ModellList(Resource):
    def get(self):
        return jsonify({'models': models})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='ID des Modells')
        parser.add_argument('name', type=str, required=True, help='Name des Modells')
        parser.add_argument('werk', type=int, required=True, help='ID des Werks')
        args = parser.parse_args()

        new_model = {
            "id": args['id'],
            "name": args['name'],
            "werk": args['werk']
        }
        models.append(new_model)
        return jsonify({'model': new_model}), 201

class Modell(Resource):
    def get(self, mid):
        model = next((m for m in models if m['id'] == mid), None)
        if model:
            return jsonify({'model': model})
        else:
            return '', 404

    def put(self, mid):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name des Modells')
        parser.add_argument('werk', type=int, required=True, help='ID des Werks')
        args = parser.parse_args()

        for model in models:
            if model['id'] == mid:
                model.update({
                    'name': args['name'],
                    'werk': args['werk']
                })
                return jsonify({'model': model})
        return '', 404

    def delete(self, mid):
        global models
        models = [m for m in models if m['id'] != mid]
        return '', 204

api.add_resource(ModellList, '/modelle/')
api.add_resource(Modell, '/modelle/<int:mid>')

if __name__ == '__main__':
    app.run(debug=True)
