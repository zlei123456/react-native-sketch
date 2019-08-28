import math
import os

def getColorStr(color):
    fillR = color['red']
    fillG = color['green']
    fillB = color['blue']
    if (color['alpha'] == 1):
        return 'rgb(' + str(math.floor(fillR * 255)) + ', ' + str(math.floor(fillG * 255)) + ', ' + str(math.floor(fillB * 255)) + ')'
    else :
        return 'rgba(' + str(math.floor(fillR * 255)) + ', ' + str(math.floor(fillG * 255)) + ', ' + str(math.floor(fillB * 255)) + ', ' + str(color['alpha']) + ')'


def getFrameData(data):
    fData = {}
    for fId, fValue in data.items():
        fData[fId] = fValue['frame']
        fData[fId]['r'] = fData[fId]['x'] + fData[fId]['width']
        fData[fId]['b'] = fData[fId]['y'] + fData[fId]['height']

    return fData


def getJsonFile(dir):
    jsonFiles = []
    for root, dirs, files in os.walk(dir):
        jsonFiles = files

    return jsonFiles
