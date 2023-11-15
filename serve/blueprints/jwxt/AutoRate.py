from bs4 import BeautifulSoup as bs4
from app import app
from Response import Success, Error

session = app.config["SESSION"]

def getPJList():

    params = {
        'Ves632DSdyV': 'NEW_XSD_JXPJ',
    }
    try:
        response = session.get(app.config["RATE_LIST_URL"], params=params, verify=False)
        table = bs4(response.text, 'lxml').find('table', class_='Nsb_r_list Nsb_table')
        # get rows expect title then convert to dict
        rows = table.find_all('tr')[1: ]
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
                item["sublist"].append({
                    "course": cols[2].text,
                    "teacher": cols[3].text,
                    "score": cols[5].text,
                    "finish": cols[6].text
                })
        return Success(data=result).toJson()
    except Exception as e:
        print(e)
        return Error(msg="出错了").toJson()
