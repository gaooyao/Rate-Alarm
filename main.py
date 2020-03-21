# coding=utf-8
import requests
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

from inquire import icbcInquire,cmbInquire
from alarm import alarm

if __name__ == "__main__":
    alarm(cmbInquire())
