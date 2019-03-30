# -*- coding: utf-8 -*-
# filename: alloter.py
import os
from wechatpy.utils import json
from wechatpy.client.api.base import BaseWeChatAPI

Path = {
    '作业':       'contents/homework.txt',
    '作业1':      'contents/homework1.txt',
    '作业2':      'contents/homework2.txt',
    '作业3':      'contents/homework3.txt',
    '帮助':       'contents/help.txt',
    '后端代码':    'contents/code.txt'
}


def ContentMaker(message):
    content = message
    if message == '作业':
        content = '【' + message + '】\n'
        hw_file = open('contents/homework.txt')
        content += hw_file.read()
    if message == '帮助':
        content = ''
        hw_file = open('contents/help.txt')
        content += hw_file.read()
    if message == '后端代码':
        content = 'https://github.com/Twx1213/805'
    if message == '作业1':
        content = ''
        hw_file = open('contents/homework1.txt')
        content += hw_file.read()
#    if message == '课表':
#        content = 'Du0cncQvn_h-zkuhRXqsIPjYbj0oUK44enQOea8WFLJa3DQa74uIT1CWSHsX_vqf'

    return content
