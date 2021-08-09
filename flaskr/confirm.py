from flask import Flask, request, Blueprint, flash, redirect, render_template, request, session, url_for
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import mailfuncs

bp = Blueprint('confirm', __name__, url_prefix='/confirm')

s = URLSafeTimedSerializer('anan')


@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        email = request.form['email']
        token = s.dumps(email, salt='salt')
        mailfuncs.mailer(email,'anan', token)
        return redirect(url_for('hello'))
    return render_template('confirm/index.html')

@bp.route('/confirm_email/<token>')
def confirm_email(token):
    email = s.loads(token, salt='salt')
    return 'Token Works!'

