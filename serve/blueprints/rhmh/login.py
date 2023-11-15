import base64
from bs4 import BeautifulSoup as bs4
from app import app
from Response import Success, Error
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

session = app.config["SESSION"]

def getCaptcha():
    try:
        # base64 encrypt account and password
        account = app.config["FP_ACCOUNT"]
        password = app.config["FP_PASSWORD"]
        session.cookies.clear()
        response = session.get(app.config["FP_URL"])
        form = bs4(response.text, 'lxml').find('form', {'id': 'fm1'})
        data = {}
        for input in form.find_all('input'):
            if input.get('name') is not None:
                data[input.get('name')] = input.get('value', '')
        data['username'] = account
        data['password'] = encrypt(password)
        data['enableCaptcha'] = 'Y'
        cookies = {
            'loginWay': 'username'
        }

        # get captcha
        response = session.get(app.config["CAPTCHA_URL"], cookies=cookies)
        data['captcha'] = "data:image/jpg;base64,"+base64.b64encode(response.content).decode('utf-8')

        return Success(data=data).toJson()
    except Exception as e:
        print(e)
        return Error(msg="出错了").toJson()

def login(data):
    try:
        headers = {
            'authority': 'cas.cupk.edu.cn',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'max-age=0',
            'origin': 'https://cas.cupk.edu.cn',
            'referer': 'https://cas.cupk.edu.cn/cas/login?service=https%3A%2F%2Fportal.cupk.edu.cn%2Fportal%2Findex_sso.jsp',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
        }
        response = session.post(app.config["FP_LOGIN_URL"],
                                headers = headers, data=data, allow_redirects=True)
        error_msg = bs4(response.text, 'lxml').find('td', {'id': 'msg'})
        if error_msg is not None:
            return Error(msg=error_msg.find('span').text).toJson()
        return Success().toJson()
    except Exception as e:
        print(e)
        return Error(msg="出错了").toJson()

def encrypt(password):
    """
    加密密码
    """
    pub_str = f"-----BEGIN RSA PUBLIC KEY-----\n{app.config['PUBLIC_KEY']}\n-----END RSA PUBLIC KEY-----"
    # 生成公钥
    pub_key = RSA.importKey(pub_str)
    # 生成加密器
    cipher = PKCS1_v1_5.new(pub_key)
    # 加密
    cipher_text = base64.b64encode(cipher.encrypt(bytes(password.encode("utf-8"))))
    return cipher_text.decode('utf-8')