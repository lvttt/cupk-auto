from flask import Blueprint, request
from Response import Success, Error

import json

rhmh_bp = Blueprint('rhmh', __name__)

@rhmh_bp.route('/login/getCaptcha')
def getCaptcha():
    """
    获取验证码地址
    """
    from . import login
    return login.getCaptcha()

@rhmh_bp.route('/login', methods=['POST'])
def Login():
    """
    登录融合门户
    """
    from . import login
    try:
        data = request.get_json()
        return login.login(data)
    except Exception as e:
        print(e)
        return Error(msg="出错了").toJson()