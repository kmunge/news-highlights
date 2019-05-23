from flask import Flask

#initializing application
def create_app(config_name):
    app = Flask(__name__)

    return app