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
    app = selectCourse.app
    courseData = None
    if mode == 0 or mode == 3:
        # 已查询过不再查询
        if app.config[f"COURSE_DATA_0{mode+1}"] is None:
            app.config[f"COURSE_DATA_0{mode+1}"] = selectCourse.queryCourseList(params,mode)
        courseData = app.config[f"COURSE_DATA_0{mode+1}"]
    else:
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
            "mode": '',
            "ready": 0
        })
        data_json = json.loads(data.to_json(orient="records"))
    except Exception as e:
        print(e)
        return Error(msg="出错了").toJson()
    return Success(data_json).toJson()

@jwxt_bp.route('/pj/getlist')
def GetPJList():
    """
    获取评教列表
    """
    from . import AutoRate
    result = AutoRate.getPJList()
    return AutoRate.getRateslist(result)

@jwxt_bp.route('/pj/rate', methods=['POST'])
def Rate():
    """
    评教
    """
    from . import AutoRate
    try:
        request_data = request.get_json()
        url = request_data['url']
        return AutoRate.rate(url)
    except Exception as e:
        print(e)
        return Error(msg="参数错误").toJson()

@jwxt_bp.route('/cj/getlist')
def GetGradeList():
    """
    获取成绩列表
    """
    from . import Grade
    return Grade.getGradeList()

@jwxt_bp.route('/cj/getrank')
def GetGradeRank():
    """
    获取成绩排名
    """
    from . import Grade
    return Grade.getGradeRank()
