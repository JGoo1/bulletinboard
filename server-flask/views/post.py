from flask import Blueprint, render_template, url_for, request
from ..service.post_service import PostService
from ..service.reply_service import ReplyService
from werkzeug.utils import redirect
from  ..form.post import PostForm

bp = Blueprint('post', __name__, url_prefix='/post')
post_service = PostService()
reply_service = ReplyService()

@bp.route('/', methods=('GET',))
def _list():
    post_list = post_service.get_post_list()
    return render_template('post_list.html', post_list=post_list)

@bp.route('/create/', methods=('GET','POST',))
def create():
    form = PostForm()
    if request.method == 'GET':
        return render_template('post_create.html', form=form)

    elif request.method == 'POST':
        post_service.create(subject=form.subject.data, content=form.content.data)
        return redirect(url_for('post._list'))
    else:
        return redirect(url_for('post._list'))


@bp.route('/<int:post_id>/')
def detail(post_id):
    post_detail = post_service.get_post(id=post_id)
    reply_list = reply_service.get_reply_list(post_id=post_id)
    return render_template('post_detail.html', post_detail=post_detail, reply_list=reply_list)

