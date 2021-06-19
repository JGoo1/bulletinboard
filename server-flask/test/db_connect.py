from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myweb2" #
mongo = PyMongo(app)

board = mongo.db.board
test = {
    "name": "test"
}

board.insert_one(test)