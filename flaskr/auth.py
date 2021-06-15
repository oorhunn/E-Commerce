import functools
from datetime import datetime
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
import dbfuncs
from model.users import Users

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        date = datetime.utcnow()
        body = {'username': username,
                'password': generate_password_hash(password),
                'register_date': date}
        error = None
        # mustaf you should do the regex shit in these lines
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        ses = dbfuncs.dbsession()
        data = ses.query(Users).all()
        for us in data:
            if f'{us.username}' == username:
                error = 'this user already registered'
        if error is None:
            dbfuncs.inster(body)
            return redirect(url_for('auth.login'))
        flash(error)
    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        ses = dbfuncs.dbsession()
        condname = ses.query(Users).filter(Users.username==username).first()
        condpass = ses.query(Users).filter(Users.password==password).first()
        if condname is None:
            error = 'Incorrect username.'
        elif condpass is None:
            error = 'Incorrect password.'
        if error is None:
            usid = ses.query(Users).filter(Users.username==username).first()
            session.clear()
            session['user_id'] = usid.id
            return redirect(url_for('hello'))
        flash(error)
    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')



@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('hello'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('user_id') is None:
            print('anan')
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view