# coding=utf-8
import requests
import re
from bs4 import BeautifulSoup


def icbcInquire():
    url = "http://www.icbc.com.cn/ICBCDynamicSite/Optimize/Quotation/QuotationListIframe.aspx"
    headers = {}
    data = {}
    res = requests.post(url=url, data=data, headers=headers)
    bs = BeautifulSoup(res.text, "html.parser")
    for x in bs.find_all("td", class_='tdCommonTableData'):
        if x.text == '英镑(GBP)':
            return x.find_next().text


def cmbInquire():
    url = "http://fx.cmbchina.com/Hq/"
    headers = {}
    data = {}
    res = requests.post(url=url, data=data, headers=headers)
    bs = BeautifulSoup(res.text, "html.parser")
    for x in bs.find_all("td", class_='fontbold'):
        b = x.text.find('英镑')
        if x.text.find('英镑') != -1:
            return re.findall(r'-?\d+\.?\d*e?-?\d*?', x.find_next().find_next().find_next().text)[0]
