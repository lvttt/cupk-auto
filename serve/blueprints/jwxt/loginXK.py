from bs4 import BeautifulSoup as bs4
from app import app
from Response import Success, Error

session = app.config["SESSION"]

def getCourseUrl():
    # get url of course selection
    url = app.config["XK_URL"]
    response = session.get(url, verify=False)
    jx0502zbid = bs4(response.text, 'lxml').find('table', {'id': 'tbKxkc'}).find('a')['href'].split('=')[1]
    return jx0502zbid

def loginSelectCourse(jx0502zbid):
    # login select course page
    url = app.config["LOGIN_XK_URL"] + jx0502zbid
    return session.get(url, verify=False)


def loginXK():
    try:
        jx0502zbid = getCourseUrl()
        response = loginSelectCourse(jx0502zbid)
        if response.status_code == 200:
            return Success().toJson()
        else:
            return Error(msg="进入选课失败").toJson()
    except Exception as e:
        print(e)
        return Error(msg="出错了").toJson()
