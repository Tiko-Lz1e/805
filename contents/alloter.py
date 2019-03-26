# -*- coding: utf-8 -*-
# filename: alloter.py
import os


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
    return content
