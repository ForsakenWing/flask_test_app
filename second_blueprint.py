from flask import Blueprint

alive = Blueprint('alive', __name__, url_prefix='/alive')


@alive.route('/start')
def alive_starter():
    return 'Alive bp started'
