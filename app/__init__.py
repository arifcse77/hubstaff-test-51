""" Initialize flask server and all configuration """
from flask import Flask, jsonify
from . import views

def create_app(credentials):
    """ create and configure the app """
    app = Flask(__name__)

    app.auth_token = credentials['AUTH_TOKEN']
    app.app_token = credentials['APP_TOKEN']

    app.register_blueprint(views.bp)
    return app