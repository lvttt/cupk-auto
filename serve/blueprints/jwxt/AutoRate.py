from bs4 import BeautifulSoup as bs4
from app import app
from Response import Success, Error
import re

session = app.config["SESSION"]


def getPJList():
    params = {
        'Ves632DSdyV': 'NEW_XSD_JXPJ',
    }
    try:
        response = session.get(app.config["RATE_LIST_URL"], params=params, verify=False)
        table = bs4(response.text, 'lxml').find('table', class_='Nsb_r_list Nsb_table')
        # get rows expect title then convert to dict
        rows = table.find_all('tr')[1:]
        result = []
        for row in rows:
            cols = row.find_all('td')
            result.append({
                'id': cols[0].text,
                'term': cols[1].text,
                'batch': cols[3].text,
                "url": cols[6].find('a')['href'],
                "sublist": []
            })
        return result
    except Exception as e:
        print(e)
        return []


def getRateslist(result):
    try:
        for item in result:
            pjUrl = "http://jw.cupk.edu.cn" + item["url"]
            response = session.get(pjUrl, verify=False)
            table = bs4(response.text, 'lxml').find('table', class_='Nsb_r_list Nsb_table')
            rows = table.find_all('tr')[1:]
            for row in rows:
                cols = row.find_all('td')
                url_pattern = r"openWindow\('([^']+)'"
                url = re.findall(url_pattern, cols[8].find('a')['href'])[0]
                item["sublist"].append({
                    "course": cols[2].text,
                    "teacher": cols[3].text,
                    "score": cols[5].text,
                    "finish": cols[6].text,
                    "url": url
                })
        return Success(data=result).toJson()
    except Exception as e:
        print(e)
        return Error(msg="出错了").toJson()


def rate(url):
    url = "http://jw.cupk.edu.cn" + url
    try:
        response = session.get(url, verify=False)
        form = bs4(response.text, 'lxml').find('form', id='Form1')
        data = {}
        # get params
        data["issubmit"] = '0'
        data["pj09id"] = form.find('input', {"name": 'pj09id'})['value']
        data["pj01id"] = form.find('input', {"name": 'pj01id'})['value']
        data["pj0502id"] = form.find('input', {"name": 'pj0502id'})['value']
        data["jg0101id"] = form.find('input', {"name": 'jg0101id'})['value']
        data["jx0404id"] = form.find('input', {"name": 'jx0404id'})['value']
        data["xsflid"] = form.find('input', {"name": 'xsflid'})['value']
        data["xnxq01id"] = form.find('input', {"name": 'xnxq01id'})['value']
        data["jx02id"] = form.find('input', {"name": 'jx02id'})['value']
        data["pj02id"] = form.find('input', {"name": 'pj02id'})['value']
        table = form.find('table', class_='Nsb_r_list Nsb_table')
        inputs = table.find_all('input')
        for input in inputs:
            if data.get(input['name']) is None:
                data[input['name']] = input['value']
        textarea = table.find('textarea')
        if textarea:
            data[textarea['name']] = textarea.text
        res = saveRate(data)
        if res == "保存成功":
            return Success().toJson()
        else:
            return Error(msg=res).toJson()
    except Exception as e:
        print(e)
        return Error(msg="出错了").toJson()


def saveRate(data):
    try:
        response = session.post(app.config["SAVE_RATE_URL"], data=data, verify=False)
        # use re to get msg
        msg_pattern = r"alert\('([^']+)'"
        msg = re.findall(msg_pattern, response.text)[0]
        return msg
    except Exception as e:
        print(e)
        return "出错了"
