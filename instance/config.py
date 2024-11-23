import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# FLASK_ENV="development"
DEBUG=True
TESTING=False
SERVER_NAME="0.0.0.0"
SQLALCHEMY_TRACK_MODIFICATIONS=True
