# by lei
# coding: utf-8

import os
import parseSketch
import globalData
import utils
import parseConfig
import layout.autoLayout
import layout.checkFlex
import layout.getCode
import layout.initConfig

# sketchFile = './res/storyInfo.sketch'
# unzipDir = './res/storyInfo'

sketchFile = './res/' + parseConfig.getConfig('fileName') + '.sketch'
unzipDir = './res/' + parseConfig.getConfig('fileName')

os.system('unzip -o ' + sketchFile + ' -d ' + unzipDir)

jsonFiles = utils.getJsonFile(unzipDir + '/pages/')
print(jsonFiles)

# 配置
layout.initConfig.init(parseConfig.getConfig('screenScale'))
outputPagesStr = parseConfig.getConfig('outputPage', 'output')
outputPages = outputPagesStr.split(',')


def dealJson(jsonFile):
    res = parseSketch.parseSketch(unzipDir + '/pages/' + jsonFile, outputPages)
    if (not res):
        return
    print(globalData.elemData)
    # 得到ID to frame 结构的数据
    elemData = utils.getFrameData(globalData.elemData)

    # 布局有关的
    layoutTree = layout.autoLayout.autoLayout(elemData)
    layout.autoLayout.addElemData(layoutTree, globalData.elemData)
    layoutElemData = layout.autoLayout.getLayoutElemData()


    flexData = layout.checkFlex.getFlexData(layoutTree, layoutElemData)

    print(flexData)
    print(globalData.elemData)

    pageName = globalData.getPageName()[:1].upper() + globalData.getPageName()[1:]
    layout.getCode.getCode(layoutTree, globalData.elemData, flexData, {'name': pageName})

    print('finish ' + globalData.getPageName())
    print(jsonFile)

for jsonFile in jsonFiles:
    dealJson(jsonFile)

# dealJson('ECE8E072-7784-4777-9443-3D8DE8467CFC.json')
# dealJson('717DCAB4-B4A1-4AEC-B14B-4453D1FB51F9.json')

