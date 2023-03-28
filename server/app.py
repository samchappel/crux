from flask import Flask, request, make_response, jsonify, abort
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Climber, Location, Route, Review

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

class Climbers(Resource):
    def get(self):
        climbers = [climber.to_dict() for climber in Climber.query.all()]
        response = make_response(
            climbers,
            200
        )
        return response

api.add_resource(Climbers, '/climbers')

if __name__ == "__main__":
    app.run(port="5555", debug=True)