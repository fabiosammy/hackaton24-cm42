import os

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# FLASK_ENV="development"
DEBUG=True
TESTING=False
SERVER_NAME="0.0.0.0"