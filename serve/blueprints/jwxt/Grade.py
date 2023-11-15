from bs4 import BeautifulSoup as bs4
from app import app
from Response import Success, Error
import xlrd

session = app.config["SESSION"]

def getGradeList():
    params = {
        'Ves632DSdyV': 'NEW_XSD_XJCJ',
    }
    try:
        respone = session.get(app.config["GRADE_LIST_URL"], params=params, verify=False)
        table = bs4(respone.text, 'lxml').find_all('table', class_='Nsb_r_list Nsb_table')

        rows1 = []
        for child in table[0].children:
            if child.name == 'tr':
                rows1.append(child)
        rows2 = table[1].find_all('tr')
        result = []
        term = ''
        for row in rows1[1:]:
            cols = row.find_all('td')
            if term != cols[1].text:
                term = cols[1].text
                result.append({
                    'term': term,
                    'sublist': []
                })
            result[-1]['sublist'].append({
                "course": cols[3].text,
                "score": cols[4].find('span').text,
                "credit": cols[5].text,
                "time": cols[6].text,
                "type": cols[9].text,
                "status": cols[10].text,
            })
        result.append({
            'term': '形势与政策',
            'sublist': []
        })
        for row in rows2[1:]:
            cols = row.find_all('td')
            result[-1]['sublist'].append({
                "time": cols[1].text,
                "course": cols[2].text,
                "score": cols[3].text,
                "platform": cols[4].text
            })
        return Success(data=result).toJson()
    except Exception as e:
        print(e)
        return []

def getGradeRank():
    try:
        response = session.get(app.config["DOWNLOAD_GRADE_URL"], verify=False)
        # use xlrd read .xls file
        workbook = xlrd.open_workbook(file_contents=response.content)
        sheet = workbook.sheet_by_index(0)
        # get rank cell
        rank = sheet.cell_value(2, 0).split(' '*8)[:2]
        return Success(data=rank).toJson()
    except Exception as e:
        print(e)
        return Error(msg="出错了").toJson()