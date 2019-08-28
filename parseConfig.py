# -*- coding: utf-8 -*

import os
import configparser

#获取config配置文件
def getPath():
    return os.path.split(os.path.realpath(__file__))[0] + '/config/config.conf'


def getConfig(key, section = 'sketch'):
    config = configparser.ConfigParser()
    path = getPath()
    config.read(path)
    return config.get(section, key)

# print(getConfig('screenScale'))