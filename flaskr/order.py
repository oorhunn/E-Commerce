
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
    user = session.get('user_id')
    # getting orders according to the user
    orders = dbfuncs.dbsession().query(Orders).filter(Orders.order_giver_id==user, Orders.activeness==True).all()
    totalPrice = 0
    i = 0
    while i < len(orders):
        totalPrice = totalPrice + orders[i].total_price
        i = i + 1



    return jsonify(orders)


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

@bp.route('/checkout', methods=('GET','POST'))
@login_required
def checkout():
    if request.method == 'POST':




    return 0