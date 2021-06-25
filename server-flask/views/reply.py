from flask import Blueprint, request, url_for
from ..service.reply_service import ReplyService
from werkzeug.utils import redirect

bp = Blueprint('reply', __name__, url_prefix='/reply')
reply_service = ReplyService()

@bp.route('/<int:post_id>/', methods=('POST',))
def create(post_id):
    content = request.form['content']
    reply_service.create(post_id=post_id, content=content)
    return redirect(url_for('post.detail', post_id=post_id))


