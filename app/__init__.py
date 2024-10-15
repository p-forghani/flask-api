from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

# The bottom import is a well known workaround that avoids circular imports
# We need to import app variable in the routes.py
from app import routes