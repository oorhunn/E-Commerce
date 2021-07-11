import datetime
import json
from dataclasses import dataclass
from model.warehouses import Warehouses
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify,session
)
from werkzeug.exceptions import abort
from model.products import Products
from model.users import Users
import dbfuncs
from flaskr.auth import login_required

bp = Blueprint('product', __name__,url_prefix='/product')

@bp.route('/')
def index():
    # TODO limit count of query
    id = session.get('user_id')
    admin_name = dbfuncs.dbsession().query(Users).filter(Users.user_id==id).first()
    # TODO add some privilege for admin users
    temp = dbfuncs.dbsession().query(Products).all()
    aa = [{"photo_link": "ananbaban", "price": 50.0, "product_name": "ayakkabi",
           "register_date": "2021-07-11 10:33:31.596816", "size": "45"}]
    return jsonify(temp)

@bp.route('/anan')
def anan():
    return render_template('product/try.html')

@bp.route('/baban')
def baban():
    temp = dbfuncs.dbsession().query(Products).all()
    tempp = jsonify(temp)
    i = 0
    while i < len(tempp):
        keys, values = zip(*tempp[i].items())
        i = i + 1

    out = {
        'aaData':
            [values]
    }
    print(out)
    return tempp

@bp.route('/create', methods=('GET','POST'))
@login_required
def add_product():
    if request.method == 'POST':
        category = request.form['category']
        product_name = request.form['name']
        product_quantity = request.form['quantity']
        price = request.form['price']
        size = request.form['size']
        register_date = datetime.datetime.utcnow()
        photo_link = request.form['photo_link']
        warehouse = dbfuncs.warehouserr()
        error = None
        if error is not None:
            flash(error)
        else:
            ses = dbfuncs.dbsession()
            body = {
                'product_name': product_name,
                'warehouse': warehouse,
                'size': size,
                'price': price,
                'register_date': register_date,
                'photo_link': photo_link,
                'category': category,
                'product_quantity': product_quantity
            }
            dbfuncs.inventoryinserter(body)
            return redirect(url_for('hello'))
    return render_template('product/create.html')

@bp.route('/<int:id>/update', methods=('POST','GET'))
@login_required
def update(id):

    if request.method == 'POST':
        try:
            category = request.form['category']
            name = request.form['name']
            quantity = request.form['quantity']
            price = request.form['price']
            size = request.form['size']
            photo_link = request.form['photo_link']
            ses = dbfuncs.dbsession()
            product_to_update = ses.query(ProductInv).filter(ProductInv.id == id).first()
            product_to_update.update(request.form.to_dict())
            ses.commit()
            ses.close()

            return redirect(url_for('hello'))
        except:
            abort(400, 'product yok')

    return render_template('product/update.html')

@bp.route('/<int:id>/delete',methods=('POST',))
@login_required
def delete(id):
    dbfuncs.inventorydelete(id)
    return redirect(url_for('hello'))
