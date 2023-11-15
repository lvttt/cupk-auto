import base64
from bs4 import BeautifulSoup as bs4
from app import app
from Response import Success, Error


def login():
    try:
        # base64 encrypt account and password
        account = base64.b64encode(app.config["SIS_ACCOUNT"].encode('utf-8')).decode('utf-8')
        password = base64.b64encode(app.config["SIS_PASSWORD"].encode('utf-8')).decode('utf-8')
        encoded = account + "%%%" + password

        data = {
            'encoded': encoded,
        }

        response = app.config["SESSION"].post(app.config["LOGIN_URL"], data=data, verify=False)

        # get error msg
        error_msg = bs4(response.text, 'lxml').find('font', {'class': 'dlmi1'})
        if error_msg:
            # login failed
            return Error(msg=error_msg.text).toJson()
        else:
            return Success().toJson()
    except Exception as e:
        print(e)
        return Error(msg="出错了").toJson()
