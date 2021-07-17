
import json
from dataclasses import dataclass
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify,session
)
from werkzeug.exceptions import abort
from model.users import Users
import dbfuncs
from flaskr.auth import login_required
from model.orders import Orders
from model.products import Products
import dbfuncs

bp = Blueprint('order', __name__, url_prefix='/order')


@bp.route('/')
@login_required
def show_order():
    temp = dbfuncs.dbsession().query(Orders).all()

    return jsonify(temp)


@bp.route('/<int:pro_id>/addorder', methods=('POST','GET'))
@login_required
def addproduct(pro_id):
    try:
        user = session.get('user_id')
        print(type(user))
        dbfuncs.add_order(pro_id, user)
        return redirect(url_for('hello'))
    except:
        abort(400, 'ERRROOOOORRR')

    return render_template('order/index.html')


@bp.route('/<int:order_id>/deleteorder')
@login_required
def delete_order(order_id):
    dbfuncs.delete_order(order_id)

    return redirect(url_for('hello'))


@bp.route('/mustaf')
@login_required
def mustaf():
    temp = dbfuncs.dbsession().query(Products).all()
    values = []
    i = 0
    while i < len(temp):
        values.append(temp[i].product_id)
        i = i + 1

    return render_template('order/index.html', keys= values)