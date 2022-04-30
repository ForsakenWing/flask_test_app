from first_blueprint import v1_bp
from second_blueprint import alive
from flask import Flask


def run_app():
    app = Flask(__name__)
    app.register_blueprint(v1_bp)
    app.register_blueprint(alive)
    app.run(debug=True)


if __name__ == '__main__':
    run_app()
