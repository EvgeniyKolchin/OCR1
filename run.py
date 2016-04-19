from flask import Flask, url_for,  render_template, flash, redirect, session, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    AppConfig(app)
    Bootstrap(app)
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    
    return app

    
