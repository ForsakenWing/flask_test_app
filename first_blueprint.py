from flask import Blueprint, request, abort

v1_bp = Blueprint('v1', __name__, url_prefix='/v1')


@v1_bp.route('/')
def app_start():
    return 'Server was successfully started'


@v1_bp.route('/get')
def get_request():  # put application's code here
    return f'Hello, you successfully sent the get request!'


@v1_bp.route('/post', methods=['GET', 'POST'])
def post_request():
    if request.method == 'POST':
        return f'Hello, you successfully sent the post request'
    return abort(405)


@v1_bp.route('/patch', methods=['GET', 'PATCH'])
def patch_request():
    if request.method == 'PATCH':
        return f'Hello, you successfully sent the patch request'
    return abort(405)


@v1_bp.route('/put', methods=['GET', 'PUT'])
def put_request():
    if request.method == 'PUT':
        return f'Hello, you successfully sent the put request'
    return abort(405)


@v1_bp.errorhandler(405)
def method_not_allowed(error):
    return f"OWN RESPONSE This method: '{request.method}' is not allowed", 405
