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
from payment import paymentfuncs

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
    buyer = {
        'id': 'BY789',
        'name': 'John',
        'surname': 'Doe',
        'gsmNumber': '+905350000000',
        'email': 'email@email.com',
        'identityNumber': '74300864791',
        'lastLoginDate': '2015-10-05 12:43:35',
        'registrationDate': '2013-04-21 15:12:09',
        'registrationAddress': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'ip': '85.34.78.112',
        'city': 'Istanbul',
        'country': 'Turkey',
        'zipCode': '34732'
    }
    basket_items = [
        {
            'id': 'BI101',
            'name': 'Binocular',
            'category1': 'Collectibles',
            'category2': 'Accessories',
            'itemType': 'PHYSICAL',
            'price': '0.3'
        },
        {
            'id': 'BI102',
            'name': 'Game code',
            'category1': 'Game',
            'category2': 'Online Game Items',
            'itemType': 'VIRTUAL',
            'price': '0.5'
        },
        {
            'id': 'BI103',
            'name': 'Usb',
            'category1': 'Electronics',
            'category2': 'Usb / Cable',
            'itemType': 'PHYSICAL',
            'price': '0.2'
        }
    ]
    address = {
        'contactName': 'Jane Doe',
        'city': 'Istanbul',
        'country': 'Turkey',
        'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'zipCode': '34732'
    }
    if request.method == 'POST':
        # TODO regex shit for card info
        cardHolderName = request.form['cardHolderName']
        cardNumber = request.form['cardNumber']
        expireMonth = request.form['expireMonth']
        expireYear = request.form['expireYear']
        cvc = request.form['cvc']
        # turning payment_card to json
        payment_card = {
            'cardHolderName': cardHolderName,
            'cardNumber': cardNumber,
            'expireMonth': expireMonth,
            'expireYear': expireYear,
            'cvc': cvc
        }
        payment = paymentfuncs.create_payment(payment_card,buyer,address,basket_items)
        return payment
        # TODO regex shit for address info
    return render_template('order/checkout.html')




