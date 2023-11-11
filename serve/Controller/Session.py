from Service.LoginService import login
import json
# import account and password from config.json
user = json.loads(open('../config.json', 'r').read())
account = user['account']
password = user['password']

# login
session = login(account, password)