import os

from first_blueprint import v1_bp
from second_blueprint import alive
from flask import Flask
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1_bp)
    app.register_blueprint(alive)
    return app


if __name__ == '__main__':
    load_dotenv('.flaskenv')
    flask_app = create_app()
    if os.getenv('FLASK_ENV') != 'development':
        flask_app.run(use_reloader=False, host='0.0.0.0', port=5000)
