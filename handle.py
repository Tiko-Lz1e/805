# -*- coding:utf-8 -*-
# filename: handle.py

import web
import config
import contents.alloter as alloter
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy import parse_message
from wechatpy.replies import TextReply


class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData
            # write log
            recMsg = parse_message(webData)
            reply = TextReply(alloter.ContentMaker(recMsg), message=recMsg)
            xml = reply.render()
            return xml.send()
        except Exception, Argument:
            return Argument

    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "Hello, this is handle view."
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = config.configs['Token']

            try:
                check_signature(token, signature, timestamp, nonce)
            except InvalidSignatureException:
                print "Something wrong with signature checking."

        except Exception, Argument:
            return Argument
