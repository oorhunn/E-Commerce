import os
from flask import Flask, render_template, send_from_directory, request

import dbfuncs
from config import Config
from werkzeug.utils import secure_filename
import imghdr
from model.products import Products


def create_app(config=Config):
    # create and configure the app
    app = Flask(__name__)

    if config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        # app.config.from_mapping(test_config)

        app.config.from_object(config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    def validate_image(stream):
        header = stream.read(512)
        stream.seek(0)
        format = imghdr.what(None, header)
        if not format:
            return None
        return '.' + (format if format != 'jpeg' else 'jpg')

    @app.errorhandler(413)
    def too_large(e):
        return "File is too large", 413

    @app.route('/product/fileupload')
    def file_upl():
        files = os.listdir(app.config['UPLOAD_PATH'])
        return render_template('product/upload.html', files=files)

    @app.route('/product/fileupload', methods=['POST'])
    def upload_files():
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        ses = dbfuncs.dbsession()
        pro_id = dbfuncs.product_id_founder()
        product_to_photo = ses.query(Products).filter(Products.product_id==pro_id).first()
        if product_to_photo.photo_link is None:
            newstr = filename
        else:
            newstr = filename + ',' +product_to_photo.photo_link
        body = {
            'photo_link': newstr
        }
        product_to_photo.update(body)
        ses.commit()
        ses.close()

        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext != validate_image(uploaded_file.stream):
                return "Invalid image", 400

            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        return '', 204

    @app.route('/product_images/<filename>')
    def upload(filename):
        return send_from_directory(app.config['UPLOAD_PATH'], filename)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import product
    app.register_blueprint(product.bp)
    # app.add_url_rule('/', endpoint='index')

    from . import order
    app.register_blueprint(order.bp)

    from . import confirm
    app.register_blueprint(confirm.bp)

    return app
