from LoginService import login
import json
from bs4 import BeautifulSoup as bs4

class CourseService:
    def __init__(self, session):
        self.session = session

    def _getCourseUrl(self):
        try:
            # get url of course selection
            url = 'http://jw.cupk.edu.cn/jsxsd/xsxk/xklc_list?Ves632DSdyV=NEW_XSD_PYGL'
            response = self.session.get(url, verify=False)
            jx0502zbid = bs4(response.text, 'lxml').find('table', {'id': 'tbKxkc'}).find('a')['href'].split('=')[1]
            return jx0502zbid
        except Exception as e:
            print(e)

    def loginSelectCourse(self):
        # login select course page
        url = 'http://jw.cupk.edu.cn/jsxsd/xsxk/xsxk_index?jx0502zbid=' + self._getCourseUrl()
        self.session.get(url, verify=False)

    def getReadyScore(self):
        url = 'http://jw.cupk.edu.cn/jsxsd/xsxk/xsxk_tzsm'
        response = self.session.get(url, verify=False)
        return response.text

if __name__ == '__main__':
    # import account and password from config.json
    user = json.loads(open('../config.json', 'r').read())
    account = user['account']
    password = user['password']
    session = login(account, password)
    courseService = CourseService(session)
    courseService.loginSelectCourse()
    res = courseService.getReadyScore()
    print(res)