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

@rhmh_bp.route('/login/changeCaptcha')
def ChangeCaptcha():
    """
    更换验证码
    """
    from . import login
    return login.changeCaptcha()


@rhmh_bp.route('/login', methods=['POST'])
def Login():
    """
    登录融合门户
    """
    from . import login
    try:
        data = request.get_json()
        res = login.login(data)
        login.getFPInfo()
        return res
    except Exception as e:
        print(e)
        return Error(msg="出错了").toJson()

@rhmh_bp.route('/changePwd', methods=['POST'])
def changePwd():
    """
    修改密码
    """
    from . import changePassword
    try:
        data = request.get_json()
        newPassword = data["newPassword"]
        return changePassword.changePassword(newPassword)
    except Exception as e:
        print(e)
        return Error(msg="出错了").toJson()