from flask import Flask, g


#create the app
angpy = Flask(__name__)

#Configure the app using a class found in settings.py
angpy.config.from_object('app.settings.DevConfig')

logger = minerva.config['LOGGER']
logger.info("Logger created")

#Register all of the blueprints

from views import home, METAR
angpy.register_blueprint(home.mod)
angpy.register_blueprint(METAR.mod, url_prefix='/metar')

@angpy.before_request
def config_g():
    g.logger = logger

@angpy.teardown_request
def clean_g(exception=None):
    g.logger = None
