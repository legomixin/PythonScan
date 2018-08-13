#!/usr/bin/python
# -*- coding: UTF-8 -*- 

'''
Author: stone
Time: 2018-08-09 15:30
Describe: 用户认证模块
'''

#官方库文件
import urllib2
import json

#自己编写的库文件
import Config

def print_func( par ) :
    userInfo = json.loads(http_userinfo())
    print userInfo['nickname'] #打印用户信息
    return

#http请求
def http_userinfo() :
    result =  Config.get_config_values('userinfo', 'url')
    response = urllib2.urlopen(result)
    print response.read()

    return response.read()
