import click
from flask import current_app, g
from flask.cli import with_appcontext
import connect

def get_db():
    if 'db' not in g:
        g.db = connect.connect_dc('connect')

    return g.db

def close_db():
    db = g.pop('db', None)

    if db is not None:
        connect.connect_dc('close')

