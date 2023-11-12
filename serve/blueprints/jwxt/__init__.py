from flask import Blueprint


jwxt_bp = Blueprint('jwxt', __name__)

@jwxt_bp.route('/login')
def Login():
    from . import login
    return login.login()

@jwxt_bp.route('/xk/login')
def LoginXK():
    from . import loginXK
    return loginXK.loginXK()

@jwxt_bp.route('/xk/getReadyScore')
def GetReadyScore():
    from . import selectCourse
    return selectCourse.getReadyScore()