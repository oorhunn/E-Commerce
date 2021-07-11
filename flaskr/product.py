import datetime
import json
from dataclasses import dataclass
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify,session
)
from werkzeug.exceptions import abort
from model.product_inv import ProductInv
from model.users import Users
import dbfuncs
from flaskr.auth import login_required

bp = Blueprint('product', __name__,url_prefix='/product')

@bp.route('/')
def index():
    # TODO limit count of query
    id = session.get('user_id')
    admin_name = dbfuncs.dbsession().query(Users).filter(Users.id==id).first()
    # TODO add some privilege for admin users
    temp = dbfuncs.dbsession().query(Products).all()

    return jsonify(temp)


@bp.route('/create', methods=('GET','POST'))
@login_required
def add_product():
    if request.method == 'POST':
        category = request.form['category']
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']
        size = request.form['size']
        register_date = datetime.datetime.utcnow()
        photo_link = request.form['photo_link']
        error = None
        if error is not None:
            flash(error)
        else:
            ses = dbfuncs.dbsession()
            body = {
                'category': category,
                'name': name,
                'quantity': quantity,
                'price': price,
                'size': size,
                'register_date': register_date,
                'photo_link': photo_link
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
def  delete(id):
    dbfuncs.inventorydelete(id)
    return redirect(url_for('hello'))
