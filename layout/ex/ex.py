import re

styleSize = [
    'width', 'height', 'borderRadius', 'paddingLeft', 'paddingRight', 'paddingTop', 'paddingBottom',
    'marginLeft', 'marginTop', 'left', 'top', 'lineHeight'
]

def getStyleLine(key, value):
    if key in styleSize:
        return 'getWidthOfPt({0})'.format(value)
    elif key == 'fontSize':
        return 'getFontSizeOfPt({0})'.format(value)
    else:
        return value

def getImportex():
    return 'import { getFontSizeOfPt, getWidthOfPt } from \'../../../utils/utils\';'


def getImageValue(imageName):
    return 'resMap.' + exGetVarName(imageName)

def exUpString(str):
    return str[:1].upper() + str[1:]

def exGetVarName(imageName):
    a = imageName.split('.');
    b = re.split('_|-', a[0])
    ret = ''
    for i in range(len(b)):
        ret += exUpString(b[i])

    return ret
