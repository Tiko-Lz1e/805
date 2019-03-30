# -*- coding:utf-8 -*-
# filename: reply.py

import web
from wechatpy.replies import TextReply
from wechatpy import create_reply
from wechatpy.replies import ImageReply
import contents.alloter as alloter


def textReply(recmsg):
    content = alloter.ContentMaker(recmsg.content.encode('utf-8'))
    msgReply = create_reply(content, message=recmsg)
    xml = msgReply.render()
    web.header('Content-Type', 'text/xml')
    return xml


def ReplyType(msg):
    if msg.content.encode('utf-8') in open('contents/textCmd.txt').read():
        return textReply(msg)
#    elif msg.Content in open('contents/imageCmd.txt').read():
#        return imageReply(msg)
    else:
        return textReply(msg)


def imageReply(recmsg):
    msgReply = ImageReply(message=recmsg)
    msgReply.media_id = alloter.ContentMaker(recmsg.content.encode('utf-8'))
    xml = msgReply.render()
    return xml.send()
