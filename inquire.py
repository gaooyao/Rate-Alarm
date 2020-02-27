# coding=utf-8
import requests
from bs4 import BeautifulSoup


def inquire():
    url = "http://www.icbc.com.cn/ICBCDynamicSite/Optimize/Quotation/QuotationListIframe.aspx"
    headers = {}
    data = {}
    res = requests.post(url=url, data=data, headers=headers)
    bs = BeautifulSoup(res.text, "html.parser")
    for x in bs.find_all("td", class_='tdCommonTableData'):
        if x.text == '英镑(GBP)':
            return x.find_next().text
