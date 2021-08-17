import datetime
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify,session, send_from_directory, app
)
from werkzeug.exceptions import abort
from model.products import Products
import dbfuncs
from flaskr.auth import login_required
import imghdr
import os
from werkzeug.utils import secure_filename
from config import Config


bp = Blueprint('product', __name__, url_prefix='/product')

UPLOAD_PATH = './product_images/'
UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif']
MAX_CONTENT_LENGTH = 2 * 1024 * 1024

@bp.route('/')
def index():
    # TODO limit count of query
    # TODO add some privilege for admin users
    temp = dbfuncs.dbsession().query(Products).all()

    return jsonify(temp)



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
        warehouse = 1
        error = None
        if error is not None:
            flash(error)
        else:
            dbfuncs.inventoryinserter(product_name, size, price, register_date, photo_link, category, product_quantity, warehouse)
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
            product_to_update = ses.query(Products).filter(Products.product_id == id).first()
            product_to_update.update(request.form.to_dict())
            ses.commit()
            ses.close()

            return redirect(url_for('hello'))
        except:
            abort(400, 'product yok')

    return render_template('product/update.html')


@bp.route('/<int:id>/delete',methods=('POST','GET'))
@login_required
def delete(id):
    dbfuncs.inventorydelete(id)
    return redirect(url_for('hello'))


