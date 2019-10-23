from flask import render_template, url_for, flash, redirect, request, Blueprint
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

from flaskblog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)

from flaskblog.users.utils import save_picture, send_rest_email


users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    # if we login then redirect to home
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # generate a hash for the password entred
        hasshed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        # stor the data in the database
        user = User(username=form.username.data,
                    email=form.email.data, password=hasshed_password)
        # add the user to db
        db.session.add(user)
        # commit change
        db.session.commit()
        # notification the user that the account is created successfully
        flash(f'Your Account has been created ! You are now able to log in ', 'success')
        # sent the user to the login page to log in
        return redirect(url_for('users.login'))

    return render_template('register.html', title='Register', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    # if the user is logged in the /login url should be desabled
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        # check if the email exist
        user = User.query.filter_by(email=form.email.data).first()
        # check if the email and password is valid
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # if we are trying to access account and redirect to login this well redirect us to account after login
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash(f'Login Unsuccessful. Please check your Email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    # if we submit the form request.method == 'POST':
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f'Your Account is Updated', 'success')
        return redirect(url_for('users.account'))
    # if we just access normally the account page
    elif request.method == 'GET':

        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='image/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)


@users.route('/user/<string:username>')
def user_posts(username):
    # get the 'page' with default=1 and accept only int
    page = request.args.get('page', 1, type=int)
    # grab the post by user
    user = User.query.filter_by(username=username).first_or_404()
    # filter post by username if one is found
    # paginare 5 post per page
    posts = Post.query\
        .filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)


@users.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    # if we login then redirect to home
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    # if we submit the form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_rest_email(user)
        flash("An Email has been sent with instruction to Reset password! check ypur spam if the message don't show up is the indox!", 'info')
        return redirect(url_for('users.login'))

    return render_template('reset_request.html', title='Request Reset Password', form=form)


@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
     # if we login then redirect to home
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)  # user =user.id
    if user is None:
        flash('that is an invalid or expired token!', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # generate a hash for the password entred
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user.password = hashed_password
        # commit change
        db.session.commit()
        # notification the user that the account is created successfully
        flash(f'Your Password has been Updated ! You are now able to log in ', 'success')
        # sent the user to the login page to log in
        return redirect(url_for('users.login'))
    return render_template('reset_password.html', title='Reset Password', form=form)
