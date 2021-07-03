import datetime
import json
from dataclasses import dataclass
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify,session
)
from werkzeug.exceptions import abort
from model.inventory import Inventory
from model.users import Users
import dbfuncs
from flaskr.auth import login_required

bp = Blueprint('order', __name__, url_prefix='/order')

@bp.route('/')
def index():


    return None