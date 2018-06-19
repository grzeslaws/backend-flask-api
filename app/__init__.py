from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_pyfile("config.cfg")

api = Api(app)
db = SQLAlchemy(app)

from app.endpoints import post, user
