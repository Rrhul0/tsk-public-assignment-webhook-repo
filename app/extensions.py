from flask_pymongo import PyMongo
from flask import Flask
from dotenv import load_dotenv
import os

# Setup MongoDB here
app = Flask(__name__)
load_dotenv()
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)