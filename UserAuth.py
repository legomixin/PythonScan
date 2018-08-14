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
    #userInfo = json.loads(http_userinfo())
    #print userInfo['nickname'] #打印用户信息
    return http_userinfo( par )

#http请求
def http_userinfo( token ) :
    #获取认证url信息
    result =  Config.get_config_values('usertoken', 'url')
    res = urllib2.Request(url=result, data=token)
    response = urllib2.urlopen(res)
    return response.read()
