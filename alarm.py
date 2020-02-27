# coding=utf-8
import requests
import time
import datetime
import random

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from main import *

from config import PHONE_NUMBER, ACCESS_KEY_ID, ACCESS_SECRET


def alarm(message):
    message = message.replace('.', '')
    print(message)
    """
    阿里云发送
    """
    client = AcsClient(ACCESS_KEY_ID, ACCESS_SECRET, 'cn-hangzhou')
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', PHONE_NUMBER)
    request.add_query_param('SignName', "KisPig网")
    request.add_query_param('TemplateCode', "SMS_184215625")
    request.add_query_param('TemplateParam', "{\"message\": \"" + message + "\"}")

    response = client.do_action_with_exception(request)
    print("通知短信已发送%s", response)
