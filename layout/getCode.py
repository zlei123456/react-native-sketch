# by lei
# coding: utf-8

import os, sys
import re
import math
import layout.template
absPath=os.path.abspath('.')
sys.path.append(absPath + '/ex')
import layout.ex.ex
import layout.initConfig

# reload(sys)
# sys.setdefaultencoding('utf8')

def getCode(layoutTree, elemsData, flexData, exData):
    print('getcode')

 # 样式文件
    fileBuf = getStyleFileBuf(layoutTree, elemsData, flexData, exData)
    writeFile = open('tmp/Style{0}.ts'.format(exData['name']), "w")
    writeFile.write(fileBuf)
    writeFile.close()

    # 组件文件
    cfileBuf = getComponentFileBuf(layoutTree, elemsData, flexData, exData)
    cwriteFile = open('tmp/{0}.tsx'.format(exData['name']), "w")
    cwriteFile.write(cfileBuf)
    cwriteFile.close()

# 组件有关的
def getComponentFileBuf(layoutTree, elemsData, flexData, exData):
    cFileBuf = getComponents(layoutTree, elemsData, flexData, exData, '      ')
    # print cFileBuf

    return layout.template.getComponentFile(exData['name'], cFileBuf)


def getComponents(layoutTree, elemsData, flexData, exData, space):
    res = {'var': '', 'render': ''}

    if 'type' in layoutTree:
        for elemKey in layoutTree['order']:
            if elemKey in layoutTree['children']:
                childTree = layoutTree['children'][elemKey]
                childCode = getComponents(childTree, elemsData, flexData, exData, space + '  ')
                code = getComponentCode(elemKey, childCode['render'], exData, space, elemsData)

                res['var'] += code['var']
                res['var'] += childCode['var']
                res['render'] += code['render']

    else:
        for elemKey in layoutTree:
            childTree = layoutTree[elemKey]
            childCode = getComponents(childTree, elemsData, flexData, exData, space + '  ')
            code = getComponentCode(elemKey, childCode['render'], exData, space, elemsData)

            res['var'] += code['var']
            res['var'] += childCode['var']
            res['render'] += code['render']

    return res


def getComponentCode(elemKey, childrenCode, exData, space, elemsData):
    res = {'var': '', 'render': ''}

    if elemKey in elemsData:
        if elemsData[elemKey]['type'] == 'View':
            res['render'] = layout.template.getView(getElemName(elemKey), exData['name'], childrenCode, space + '  ')

            elemAttrs = elemKey.split('-')
            if('touch' in elemAttrs):
                res['render'] = layout.template.getButton(getElemName(elemKey + 'T'), res['render'], space)

        elif elemsData[elemKey]['type'] == 'Image':
            imgName = ''
            imgCode = ''

            varName = getVarName(elemKey)
            if getattr(layout.ex.ex, 'getImageValue', None):
                res['var'] += '    let {0}Img = {1};\n'.format(varName, layout.ex.ex.getImageValue(elemsData[elemKey]['source']))
            else:
                res['var'] += '    let {0}Img = require(\'./{1}\');\n'.format(varName, elemsData[elemKey]['source'])

            if childrenCode == '':
                imgCode = layout.template.getImage(getElemName(elemKey), exData['name'], childrenCode, 'Image', varName + 'Img', space)
            else:
                imgCode = layout.template.getImage(getElemName(elemKey), exData['name'], childrenCode, 'ImageBackground', varName + 'Img', space)

            res['render'] = imgCode

            elemAttrs = elemKey.split('-')
            if('touch' in elemAttrs):
                res['render'] = layout.template.getButton(getElemName(elemKey + 'T'), res['render'], space)

        elif elemsData[elemKey]['type'] == 'Text':
            str = elemsData[elemKey]['value']

            varName = getVarName(elemKey)
            res['var'] += '    let {0}Text = \'{1}\';\n'.format(varName, str)

            elemAttrs = elemKey.split('-')
            if('touch' in elemAttrs):
                res['render'] = layout.template.getTouchText(getElemName(elemKey), exData['name'], varName + 'Text', space)
            else:
                res['render'] = layout.template.getText(getElemName(elemKey), exData['name'], varName + 'Text', space)


    return res


ignoreKey = [
    'x', 'y'
]
# 样式有关的
# exData name
# style lei
def getStyleFileBuf(layoutTree, elemsData, flexData, exData):
    styleItems = ''

    for uId in elemsData:
        lineStr = ''
        style = {}
        if 'style' in elemsData[uId]:
            style = elemsData[uId]['style']
        if 'frame' in elemsData[uId]:
            style['width'] = elemsData[uId]['frame']['width']
            style['height'] = elemsData[uId]['frame']['height']
            if (elemsData[uId]['type'] == 'Text'):
                style['height'] += 1

        if uId in flexData:
            for k1 in flexData[uId]:
                style[k1] = flexData[uId][k1]


        for styleKey in style:
            if styleKey in ignoreKey:
                continue
            v = style[styleKey]
            vStr = getStyleLine(styleKey, v)
            lineStr += '    {0}: {1},\n'.format(styleKey, vStr)

        if (elemsData[uId]['type'] == 'Text'):
            lineStr += '    {0}: {1},\n'.format('includeFontPadding', 'false')

        styleItems += '  {0}: {{\n{1}  }},\n'.format(getElemName(uId), lineStr)

    if getattr(layout.ex.ex, 'getImportex', None):
        return layout.template.getStyleFile(exData['name'], styleItems, layout.ex.ex.getImportex())
    else:
        return layout.template.getStyleFile(exData['name'], styleItems, '')

sizeTypeArr = [
    'width', 'height', 'marginLeft', 'marginRight', 'marginTop', 'marginBottom', 'fontSize', 'left', 'top', 'lineHeight'
]

def getStyleLine(key, value):
    sScale = int(layout.initConfig.getScreenSacle())

    if type(value) == type('a'):
        value = '\'{0}\''.format(value)
    if type(value) == type(False) and value == False:
        value = 'false'

    if key in sizeTypeArr:
        value = (int)(math.floor(value / sScale))

    if getattr(layout.ex.ex, 'getStyleLine', None):
        # print 'getStyleLine 1'
        return layout.ex.ex.getStyleLine(key, value)
    else:
        # print 'getStyleLine 2'
        return value


def upString(str):
    return str[:1].upper() + str[1:]

def getVarName(imageName):
    a = imageName.split('.');
    b = re.split('_|-', a[0])
    ret = ''
    for i in range(len(b)):
        ret += upString(b[i])

    return ret

def getElemName(elemName):
    return elemName.replace('-', '_')