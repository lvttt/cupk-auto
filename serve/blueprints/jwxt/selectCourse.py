from bs4 import BeautifulSoup as bs4
from app import app
from Response import Success, Error

session = app.config["SESSION"]

def _getReadyScore():
    response = session.get(app.config["READY_SCORE_URL"], verify=False)
    return response.text


def getReadyScore():
    try:
        res = _getReadyScore()
        return Success(data=res).toJson()
    except Exception as e:
        print(e)
        return Error(msg="出错了").toJson()

def queryCourseList(params,mode=0):
    # params = {
    #     'kcxx': '',
    #     'skls': '',
    #     'skxq': '',
    #     'skjc': '',
    #     'sfym': 'false',
    #     'sfct': 'false',
    #     'sfxx': 'false',
    # }
    data = {
        'sEcho': '1',
        'iColumns': '13',
        'sColumns': '',
        'iDisplayStart': '0',
        'iDisplayLength': '999',
        'mDataProp_0': 'kch',
        'mDataProp_1': 'kckxh',
        'mDataProp_2': 'kcmc',
        'mDataProp_3': 'xf',
        'mDataProp_4': 'skls',
        'mDataProp_5': 'sksj',
        'mDataProp_6': 'skdd',
        'mDataProp_7': 'ktmc',
        'mDataProp_8': 'xkrs',
        'mDataProp_9': 'syrs',
        'mDataProp_10': 'ctsm',
        'mDataProp_11': 'xkyq',
        'mDataProp_12': 'czOper',
    }
    url = app.config["QUERY_COURSE_URL"][mode]

    if mode == 3:
        # 公选课选课
        data["mDataProp_7"] = "xkrs"
        data["mDataProp_8"] = "syrs"
        data["mDataProp_9"] = "ctsm"
        data["mDataProp_10"] = "szkcflmc"

    try:
        response = session.post(url, params=params, data=data,
             verify=False)
        return Success(data=response.json()).toJson()
    except Exception as e:
        print(e)
        return Error(msg="出错了").toJson()

def selectCourse(courselist, mode=0):
    try:
        res = []
        url = app.config["SELECT_COURSE_URL"][mode]
        for courseId in courselist:
            params = {
                'jx0404id': courseId,
                'xkzy': '',
                'trjf': '',
            }
            response = session.get(url, params=params,
                        verify=False)
            # get respone.success
            res.append(response.json())
        return Success(data=res).toJson()
    except Exception as e:
        print(e)
        return Error(msg="出错了").toJson()