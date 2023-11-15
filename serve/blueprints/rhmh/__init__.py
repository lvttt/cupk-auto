from flask import Blueprint, request
from Response import Success, Error

import json

rhmh_bp = Blueprint('rhmh', __name__)