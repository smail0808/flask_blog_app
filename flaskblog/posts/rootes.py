from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flaskblog import db
from flaskblog.models import Post
from flask_login import current_user, login_required
from flaskblog.posts.forms import PostForm


posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data,
                        content=form.content.data, author=current_user)
        # add the user to db
        db.session.add(new_post)
        # commit change
        db.session.commit()
        flash('Your Post has been created', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', legend='New Post', form=form)


@posts.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    # get the post with id= post_id or 404 page
    post = Post.query.get_or_404(post_id)
    # if the author of the post != the current user
    if post.author != current_user:
        # forbieden page
        abort(403)
    form = PostForm()
    if form.validate():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your Post has been Updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', legend='Update Post', form=form)


@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
     # get the post with id= post_id or 404 page
    post = Post.query.get_or_404(post_id)
    # if the author of the post != the current user
    if post.author != current_user:
        # forbieden page
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your Post has been Deleted!', 'warning')
    return redirect(url_for('main.home'))
