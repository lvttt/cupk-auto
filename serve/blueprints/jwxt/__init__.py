from flask import Blueprint, request
from Response import Success, Error
import json

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


@jwxt_bp.route('/xk/upload', methods=['POST'])
def uploadCourseList():
    """
    上传课程列表
    """
    try:
        import pandas as pd
        uploaded_file = request.files['file']
        df = pd.read_excel(uploaded_file)
        df["教学班"] = df["教学班"].apply(lambda x: str(x).zfill(2))
        data = pd.DataFrame({
            "courseId": df["课程代码"],
            "classId": df["教学班"],
            "courseName": df["课程名"],
            "teacher": df["上课教师"],
            "time": df["上课时间"],
            "class": df["上课班级"],
            "type": df["课程属性"],
            "mode": ''
        })
        data_json = json.loads(data.to_json(orient="records"))
    except Exception as e:
        print(e)
        return Error(msg="出错了").toJson()
    return Success(data_json).toJson()