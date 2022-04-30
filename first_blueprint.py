from flask import Blueprint

v1_bp = Blueprint('v1', __name__, url_prefix='/v1')


@v1_bp.route('/')
def app_start():
    return 'Server was successfully started'


@v1_bp.route('/get')
def get_request():  # put application's code here
    return f'Hello, you successfully sent the get request!'


@v1_bp.route('/post')
def post_request():
    return f'Hello, you successfully sent the post request'
