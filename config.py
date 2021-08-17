import os 

basedir = os.path.abspath(os.path.dirname(__name__))

# Create a super class
class Config(object):
    UPLOAD_PATH = './flaskr/product_images/'
    UPLOAD_EXTENSIONS = ['.jpg', '.png']
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    SECRET_KEY = 'dev'


