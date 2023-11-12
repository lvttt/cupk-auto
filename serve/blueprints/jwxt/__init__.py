from flask import Blueprint, request
from Response import Success, Error

jwxt_bp = Blueprint('jwxt', __name__)


@jwxt_bp.route('/login')
def Login():
    """
    登录教务系统
    """
    from . import login
    return login.login()


@jwxt_bp.route('/xk/login')
def LoginXK():
    """
    登录选课系统
    """
    from . import loginXK
    return loginXK.loginXK()


@jwxt_bp.route('/xk/getReadyScore')
def GetReadyScore():
    """
    获取已选课的学分
    """
    from . import selectCourse
    return selectCourse.getReadyScore()


@jwxt_bp.route('/xk/selectCourse', methods=['POST'])
def SelectCourse():
    """
    选课
    """
    # get flask request.args then convert to json and get courselist
    try:
        request_data = request.get_json()
        courselist = request_data['courselist'] # 课程id列表
        mode = request_data['mode'] # 选课模式
        params = request_data['params']  # 查询参数
    except:
        return Error(msg="参数错误").toJson()
    from . import selectCourse
    courseData = selectCourse.queryCourseList(params,mode)
    coursemp = selectCourse.getCourseId(courseData)
    return selectCourse.selectCourse(courselist, coursemp, mode)


