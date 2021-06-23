from flask import Blueprint
from ..service.answer_service import AnswerService

bp = Blueprint('answer', __name__, url_prefix='/')
answerService = AnswerService()

@bp.route('/answer/')
def _list():
    pass

@bp.route('/answer/', methods=('POST',))
def create():
    pass
