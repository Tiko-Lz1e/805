# -*- coding:utf-8 -*-
# filename: reply.py

from wechatpy.replies import TextReply
from wechatpy.replies import ImageReply
import contents.alloter as alloter


def textReply(recmsg):
    msgReply = TextReply(alloter.ContentMaker(recmsg), message=recmsg)
    xml = msgReply.render()
    return xml.send()


def ReplyType(msg):
    if msg.Content in open('contents/textCmd.txt').read():
        return textReply(msg)
    elif msg.Content in open('contents/imageCmd.txt').read():
        return imageReply(msg)
    else:
        return 'success'


def imageReply(recmsg):
    msgReply = ImageReply(alloter.ContentMaker(recmsg), message=recmsg)
    xml = msgReply.render()
    return xml.send()
