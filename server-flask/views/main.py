from flask import Blueprint, url_for
from ..service.post_service import PostService
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')
postService = PostService()

@bp.route('/')
def index():
    return redirect(url_for('post._list'))


