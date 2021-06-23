from flask import Blueprint, render_template
from ..service.post_service import PostService
from ..service.answer_service import AnswerService

bp = Blueprint('post', __name__, url_prefix='/')
post_service = PostService()
answer_service = AnswerService()

@bp.route('/list')
def _list():
    post_list = post_service.get_post_list()
    return render_template('post_list.html', post_list=post_list)


@bp.route('/post/<int:post_id>/')
def detail(post_id):
    post_detail = post_service.get_post(id=post_id)
    answer_list = answer_service.get_answer_list(post_id=post_id)
    return render_template('post_detail.html', post_detail=post_detail, answer_list=answer_list)

