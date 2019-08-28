# by lei
# coding: utf-8

import os, sys
import re

flexBoxData = {}

def checkSpaceBetween(childrenOrder, children, dir, elemFrameData):
    dirKey = 'top'
    if dir == 'h':
        dirKey = 'left'

    if len(childrenOrder) > 2:
        isSpaceBetween = True
        off = elemFrameData[childrenOrder[1]][dirKey]
        # off = children[childrenOrder[1]]['pos'][dirKey]
        for i in range(2, len(childrenOrder)):
            # curOff = children[childrenOrder[i]]['pos'][dirKey]
            curOff = elemFrameData[childrenOrder[i]][dirKey]
            if off == curOff:
                continue
            else:
                isSpaceBetween = False
                break

        if isSpaceBetween:
            return True

    else:
        return False

def checkAlignCenter(childrenOrder, children, dir, elemFrameData):
    alignDir = 'left'
    alignSize = 'width'
    if dir == 'h':
        alignDir = 'top'
        alignSize = 'height'

    if len(childrenOrder) > 1:
        isCenter = True
        firstPos = elemFrameData[childrenOrder[0]]
        centerPos = firstPos[alignDir] + firstPos[alignSize] / 2
        for elemKey in childrenOrder:
            # elemData = children[elemKey]
            elemPos = elemFrameData[elemKey]  # elemData['pos']
            cPos = elemPos[alignDir] + elemPos[alignSize] / 2
            if abs(cPos - centerPos) > 2:
                isCenter = False
                break

        return isCenter
    else:
        return False


def getJustifyRelativeStyle(childrenOrder, children, dir, elemFrameData):
    st = {}

    justifyDir = 'top'
    if dir == 'h':
        justifyDir = 'left'

    for elemKey in childrenOrder:
        # elemData = children[elemKey]
        elemPos = elemFrameData[elemKey]   # elemData['pos']

        st[elemKey] = {}
        st[elemKey][justifyDir] = elemPos[justifyDir]

    return st


def getAlignRelativeStyle(childrenOrder, children, dir, elemFrameData):
    st = {}

    alignDir = 'left'
    if dir == 'h':
        alignDir = 'top'

    for elemKey in childrenOrder:
        # elemData = elemFrameData[elemKey]
        elemPos = elemFrameData[elemKey]

        st[elemKey] = {}
        st[elemKey][alignDir] = elemPos[alignDir]

    return st


def checkCenter(parentPos, childPos):
    c0 = childPos['left'] + childPos['width'] / 2
    c1 = childPos['top'] + childPos['height'] / 2

    if c0 == parentPos['width'] / 2 and c1 == parentPos['height']:
        return True
    else:
        return False



def checkFlex(layoutTree, elemFrameData, parentId):
    global flexBoxData

    if not parentId in flexBoxData:
        flexBoxData[parentId] = {}

    if 'type' in layoutTree:
        if layoutTree['type'] == 'h':
            flexBoxData[parentId]['flexDirection'] = 'row'

        if checkSpaceBetween(layoutTree['order'], layoutTree['children'], layoutTree['type'], elemFrameData):
            flexBoxData[parentId]['justifyContent'] = 'space-between'
        else:
            st = getJustifyRelativeStyle(layoutTree['order'], layoutTree['children'], layoutTree['type'], elemFrameData)
            preItem = ''
            for k in st:
                if not k in flexBoxData:
                    flexBoxData[k] = {}

                if layoutTree['type'] == 'abs' and layoutTree['absChildren'] == k:
                    flexBoxData[k]['position'] = 'absolute'

                    for k1 in st[k]:
                        flexBoxData[k][k1] = st[k][k1]
                else :

                    justifyDir = 'top'
                    justifyDirM = 'marginTop'
                    justifySize = 'height'
                    if layoutTree['type'] == 'h':
                        justifyDir = 'left'
                        justifySize = 'width'
                        justifyDirM = 'marginLeft'

                    print(preItem)
                    print(k)
                    for k1 in st[k]:
                        if (k1 == justifyDir):
                            if not (preItem == ''):
                                flexBoxData[k][justifyDirM] = elemFrameData[k][justifyDir] - elemFrameData[preItem][
                                    justifyDir] - elemFrameData[preItem][justifySize]
                            else:
                                flexBoxData[k][justifyDirM] = st[k][k1]
                        else:
                            flexBoxData[k][k1] = st[k][k1]


                preItem = k

        if checkAlignCenter(layoutTree['order'], layoutTree['children'], layoutTree['type'], elemFrameData):
            flexBoxData[parentId]['alignItems'] = 'center'
        else:
            st = getAlignRelativeStyle(layoutTree['order'], layoutTree['children'], layoutTree['type'], elemFrameData)
            for k in st:
                if not k in flexBoxData:
                    flexBoxData[k] = {}
                for k1 in st[k]:
                    flexBoxData[k][k1] = st[k][k1]

        for elemKey in layoutTree['order']:
            nextElem = layoutTree['children'][elemKey]
            checkFlex(nextElem, elemFrameData, elemKey)

    else:

        if (len(layoutTree) == 1):
            tKeys = list(layoutTree.keys())
            k = tKeys[0]

            if not k in flexBoxData:
                flexBoxData[k] = {}
            if (parentId != '' and checkCenter(elemFrameData[k], elemFrameData[parentId])):

                flexBoxData[k]['justifyContent'] = 'center'
                flexBoxData[k]['alignItems'] = 'center'

            else :
                flexBoxData[k]['left'] = elemFrameData[k]['left'] or 0
                flexBoxData[k]['top'] = elemFrameData[k]['top'] or 0

            checkFlex(layoutTree[k], elemFrameData, k)
        else:
            for k in layoutTree:
                print(layoutTree[k])


                # if (checkCenter(elemFrameData[k]))

                checkFlex(layoutTree[k], elemFrameData, k)
                # if 'children' in layoutTree[k]:
                #     checkFlex(layoutTree[k]['children'], elemFrameData, k)
                # else :
                #     checkFlex(layoutTree[k], elemFrameData, k)




def getFlexData(layoutTree, elemFrameData):
    global flexBoxData
    flexBoxData = {}

    checkFlex(layoutTree, elemFrameData, '')

    return flexBoxData