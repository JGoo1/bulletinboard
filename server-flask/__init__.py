from flask import Flask
from .views import main, post, reply
from flask_migrate import Migrate
from flask_pymongo import PyMongo

import config

app = Flask(__name__)
db = PyMongo()
migrate = Migrate()

app.config.from_object(config)

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(main.bp)
app.register_blueprint(post.bp)
app.register_blueprint(reply.bp)
