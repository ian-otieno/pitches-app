from flask import Flask

# Initializing application
app = Flask(__name__)

from app.main import views