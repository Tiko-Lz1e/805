# -*- coding: utf-8 -*-
# filename: alloter.py
import os


def ContentMaker(recmsg):
    if recmsg.MsgType == 'text':
        message = recmsg.content
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
        if message == '作业3':
            content = ''
            hw_file = open('contents/homework3.txt')
            content += hw_file.read()
        return content
    else:
        return "I cannot do it."
