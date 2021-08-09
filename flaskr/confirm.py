# from flask import Flask, request, Blueprint, flash, redirect, render_template, request, session, url_for
# from itsdangerous import URLSafeSerializer, SignatureExpired
# from flask_mail import Mail
#
#
# bp = Blueprint('confirm', __name__, url_prefix='/confirm')
#
# s = URLSafeSerializer('anan')
#
#
# @bp.route('/', methods=('GET', 'POST'))
# def index():
#     if request.method == 'GET':
#         return '<form action="/" method="POST"><input name="email"><input type="submit"></form>'
#
#     email = request.form['email']
#     token = s.dumps(email, salt='baban')
#     print(token)
#     print(email)
#     return 'the email is {} token is {}'.format(email, token)





