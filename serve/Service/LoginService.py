import requests
import base64
from bs4 import BeautifulSoup as bs4
import json
def login(account, password):
    try:
        session = requests.Session()
        # base64 encrypt account and password
        account = base64.b64encode(account.encode('utf-8')).decode('utf-8')
        password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
        encoded = account + "%%%" + password

        data = {
            'encoded': encoded,
        }

        response = session.post('http://jw.cupk.edu.cn/jsxsd/xk/LoginToXk', data=data, verify=False)

        # get error msg
        error_msg = bs4(response.text, 'lxml').find('font', {'class': 'dlmi1'})
        if error_msg:
            # login failed
            return error_msg
    except Exception as e:
        print(e)
        return None

    # login success
    return session

if __name__ == '__main__':
    # import account and password from config.json
    user = json.loads(open('../config.json', 'r').read())
    account = user['account']
    password = user['password']
    # login
    login(account, password)