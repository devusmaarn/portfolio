from flask import Blueprint

from . import views


bp = Blueprint(__name__)


@bp.route('/'):
