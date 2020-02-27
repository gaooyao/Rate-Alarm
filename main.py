# coding=utf-8
import requests
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

from inquire import *
from alarm import *
import time


if __name__ == "__main__":
    while True:
        alarm(inquire())
        time.sleep(43200)
