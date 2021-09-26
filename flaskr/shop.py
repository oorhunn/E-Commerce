import datetime
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify,session, send_from_directory, app
)
from werkzeug.exceptions import abort
from model.products import Products
import dbfuncs
from flaskr.auth import login_required


bp = Blueprint('shop', __name__, url_prefix='/shop')



@bp.route('/')
@login_required
def index():
    temp = dbfuncs.dbsession().query(Products).all()
    values = []
    i = 0
    while i < len(temp):
        values.append(temp[i].product_id)
        i = i + 1

    return render_template('shop/index.html', keys= values)
