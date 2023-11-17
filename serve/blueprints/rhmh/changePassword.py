import base64
from bs4 import BeautifulSoup as bs4
from app import app
from Response import Success, Error

session = app.config["SESSION"]


def changePassword(newPassword):
    try:
        params = {
            "sid": app.config["FP_SID"],
            "cmd": app.config["FP_CMD"]+"_change_password",
        }
        data = {
            "newpassword": newPassword,
            "oldPassword": app.config["FP_PASSWORD"]
        }
        response = session.post(app.config["FP_DOMAIN"] + "/jd", params=params, data=data)
        if response.status_code != 200:
            return Error(msg="出错了").toJson()
        if response.json()["result"] == "success":
            return Success().toJson()
        """
            2023-11-17 bug
            修改密码成功返回: {"msg":"内部错误(500)","result":"error","data":{"desc":"java.lang.NullPointerException\nCaused by: edu.cupk.theme.v2.service.CUPKLdapHelper.modifyUserPassword(ThemeService.java:1964)"},"errorCode":"500","id":":RO;"}
            原密码错误返回:
            {
              "msg": "原密码不正确，请重新输入",
              "result": "error",
              "id": ":RO;"
            }
            因此除原密码错误外均返回成功
        """
        return Success().toJson()
    except Exception as e:
        print("ChangeError: ", e)
        return Error(msg="出错了").toJson()

