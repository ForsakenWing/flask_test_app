from flask import Blueprint, request, abort
from json import dumps

v1_bp = Blueprint('v1', __name__, url_prefix='/v1')
tag = None


def handler(request):
    path = request.raw_path
    method = request.method

    reply = {
        'method': method,
        'path': path
    }

    ip = request.headers.get('X-Forwarded-For')
    if ip:
        reply['ip'] = ip

    host = request.headers.get('Host')
    if host is None:
        request.headers.get('X-Forwarded-Host')
    if host:
        reply['host'] = host

    if tag:
        reply['tag'] = tag

    headers = dict()
    for header in ['X-Forwarded-Port',
                   'X-Forwarded-Proto',
                   'X-Forwarded-Agent',
                   'X-Forwarded-Request',
                   'X-Amzn-Trace-Id']:
        result = request.headers.get(header, None)
        if result:
            headers[header] = result

    if len(headers) != 0:
        reply['headers'] = headers

    return dumps(reply, indent=4)


@v1_bp.route('/')
def app_start():
    return 'Server was successfully started', 200


@v1_bp.route('/get')
def get_request():  # put application's code here
    return f'Hello, you successfully sent the get request!', 200


@v1_bp.route('/post', methods=['GET', 'POST'])
def post_request():
    if request.method == 'POST':
        return f'Hello, you successfully sent the post request', 202
    return abort(405)


@v1_bp.route('/patch', methods=['GET', 'PATCH'])
def patch_request():
    if request.method == 'PATCH':
        return f'Hello, you successfully sent the patch request', 202
    return abort(405)


@v1_bp.route('/put', methods=['GET', 'PUT'])
def put_request():
    if request.method == 'PUT':
        return f'Hello, you successfully sent the put request', 202
    return abort(405)


@v1_bp.errorhandler(405)
def method_not_allowed(error):
    return f"OWN RESPONSE This method: '{request.method}' is not allowed", 405
