from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from model.inventory import Inventory
import dbfuncs
from flaskr.auth import login_required

bp = Blueprint('product', __name__)

