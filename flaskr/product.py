import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from model.inventory import Inventory
import dbfuncs
from flaskr.auth import login_required

bp = Blueprint('product', __name__,url_prefix='/product')

@bp.route('/')
def index():
    dbses = dbfuncs.dbsession()
    all_products = dbses.query(Inventory).all()
    for product in all_products:
        print(product.name)
    return render_template('product/index.html', posts=product.name)

@bp.route('/create', methods=('GET','POST'))
@login_required
def add_product():
    # TODO kayar secmeli kisimlar ekle
    # TODO add preview page
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

def get_product(id):
    ses = dbfuncs.dbsession()
    product = ses.query(Inventory).filter(Inventory.id==id).first()
    if product is None:
        abort(404, f"product {product.id} does not exist")
    return product.id

@bp.route('/<int:id>/update', methods=('GET','POST'))
@login_required
def update(id):
    product_id = get_product(id)

    if request.method == 'POST':
        category = request.form['category']
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']
        size = request.form['size']
        photo_link = request.form['photo_link']
        error = None
        if product_id is None:
            error = 'product id is out of index'
        if error is not None:
            flash(error)
        if category is not None:
            dbfuncs._update_inventory_category(product_id, category)
        if name is not None:
            dbfuncs._update_inventory_name(product_id, name)
        if quantity is not None:
            dbfuncs._update_inventory_quantity(product_id, quantity)
        if price is not None:
            dbfuncs._update_inventory_price(product_id, size)
        if photo_link is not None:
            dbfuncs._update_inventory_photo_link(product_id, photo_link)

        return redirect(url_for('hello'))

    return render_template('product/update.html')




