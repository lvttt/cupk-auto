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