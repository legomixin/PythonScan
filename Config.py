#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import configparser

#项目路径
rootdir = os.path.split(os.path.realpath(__file__))[0]

#config.ini 文件路径
configFilePath = os.path.join(rootdir, 'config.ini')

def get_config_values(section, option):
    '''
    根据传入的section获取对应的value
    :param section: ini配置文件中用[]标识的内容
    :return:
    '''
    config = configparser.ConfigParser()
    config.read(configFilePath)
    return config.get(section=section, option=option)

if __name__ == '__main__':
    result = get_config_values('userinfo', 'url')
    print(result)
