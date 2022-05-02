from flask import Blueprint

version = Blueprint('version', __name__, url_prefix='/version')


@version.route('/')
def alive_starter():
    return 'version returned'
