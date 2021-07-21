from urllib.request import *
from bs4 import *
import matplotlib.pyplot as plt


def get_PN(DN):
    PN = DN // 20
    if DN > PN * 20: PN += 1

    return PN


def inputCompanyAndDays():
    company_code = to_code[int(input("회사를 고르세요 : "))]
    DN = int(input("종가 추출 기간을 입력하세요(20의 배수가 되도록 상향 조정합니다) : "))
    if DN <= 0:
        raise Exception()
    PN = get_PN(DN)

    return company_code, PN


def to_request_obj(url):
    req = Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0')
    return req


def to_intval(string_with_comma):
    return int(string_with_comma.replace(',', ''))


def extractLastPrice(company_code, PN):
    webUrl = "https://finance.naver.com/item/frgn.nhn?code=" + company_code + "&page="
    for page_num in range(1, PN + 1):
        wPage = to_request_obj(webUrl + str(page_num))
        wp = urlopen(wPage)
        soup = BeautifulSoup(wp, 'html.parser')
        trList = soup.find_all('tr', {"onmouseover": "mouseOver(this)"})
        for tr in trList:
            tdList = tr.find_all('td')
            closing_price = to_intval(tdList[1].get_text())
            pList.append(closing_price)


def makeMA():
    for scale in MA_scales:
        MA_list = []
        p = pList[0]
        mSum = p * scale
        que = [p for _ in range(scale)]

        for price in pList:
            mSum -= que.pop(0)
            mSum += price
            MA_list.append(mSum / scale)
            que.append(price)

        MA_lists.append(MA_list)


def drawGraph(company_code):
    min_val = -PN * 20
    x = [i for i in range(min_val + 1, 1)]
    plt.plot(x, pList, 'r', label=to_name[company_code])
    plt.plot(x, MA_lists[0], 'b', label=MA_name[MA_scales[0]])
    plt.plot(x, MA_lists[1], 'g', label=MA_name[MA_scales[1]])
    plt.plot(x, MA_lists[2], 'y', label=MA_name[MA_scales[2]])
    if len(MA_lists) >= 4:
        for i in range(3, len(MA_lists)):
            plt.plot(x, MA_lists[i], label=MA_name[MA_scales[i]])

    plt.xlabel('Day')
    plt.legend(loc="upper left")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    to_code = {1: "005930", 2: "066570", 3: "005380"}
    to_name = {"005930": "samsung", "066570": "lge", "005380": "hyun_car"}
    MA_scales = [5, 20, 60] + []  # 자유롭게 추가할 수 있음 (5, 20, 60 중 하나를 삭제하는 것은 안됨)
    MA_name = dict()
    for scale in MA_scales:
        MA_name[scale] = str(scale) + "MA"
    MA_lists = list()
    pList = list()  # 종가 저장 리스트

    print("1:samsung, 2:lge, 3:hyun_car")
    while True:
        try:
            company_code, PN = inputCompanyAndDays()
            break
        except:
            print("잘못된 입력입니다.")

    extractLastPrice(company_code, PN)
    pList.reverse()
    makeMA()
    drawGraph(company_code)
