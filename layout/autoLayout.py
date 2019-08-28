# by lei
# coding: utf-8

import os, sys
import globalData
import functools

# 导入的elemData
# {id: {x: x, y: y, width: width, height: height, r: 右边坐标, b: 下面的坐标} }

layoutElemData = {}
sortListH = []   # 水平轴的排序列表
sortListV = []   # 垂直轴的排序列表

def setElemData(data):
    global layoutElemData
    layoutElemData = data


def getLayoutElemData():
    global layoutElemData
    return layoutElemData

def autoLayout(elemsData):
    global layoutElemData
    global sortListH
    global sortListV

    setElemData(elemsData)

    # 横竖屏排序
    sortListV = sortLayoutV(layoutElemData)
    sortListH = sortLayoutH(layoutElemData)

    tree = checkIn(sortListV, sortListH)
    print(tree)

    return tree



def checkIn(sortElemV, sortElemH):
    if (len(sortElemV) <= 0):
        return {}

    firstElemV = sortElemV[0]
    firstElemH = sortElemH[0]
    sArr = firstElemV[0].split('*')
    uId = sArr[0]

    if (firstElemV[0] == firstElemH[0]):
        lastElemV = sortElemV[len(sortElemV) - 1]
        lastElemH = sortElemH[len(sortElemH) - 1]
        if (lastElemV[0] == uId + '*1' and lastElemH[0] == uId + '*1'):
            print('in')
            sElemV = sortElemV[1: len(sortElemV) - 1]
            sElemH = sortElemH[1: len(sortElemH) - 1]
            print(sElemV)

            childElem = checkIn(sElemV, sElemH)
            if childElem == None:
                childElem = {}
                return {}
            elif len(childElem) == 0:
                res = {}
                res[uId] = {}
                return res
            else:
                print(uId)
                print(childElem)
                res = {}
                # res[uId] = {
                #     'type': 'in',
                #     'children': childElem
                # }
                res[uId] = childElem
                return res

    return checkVertical(sortElemV, sortElemH)

def checkVertical(sortElemV, sortElemH):

    print('aaaaa')
    print(sortElemV)
    splitArr = splitElems(sortElemV)

    if (len(splitArr) > 1):
        print('checkVertical 可以分割')

        children = {}
        ChildrenOrder = []
        # children = collections.OrderedDict()
        print(splitArr)
        for elems in splitArr:
            if (len(elems) == 2):
                eId = getElemId(elems[0])
                children[eId] = {}
                ChildrenOrder.append(eId)
            else:
                print('*****')
                elemH = getElems(elems, sortElemH)
                childElem = checkIn(elems, elemH)
                print(childElem)
                if childElem:
                    if 'type' in childElem:
                        k = globalData.getId() # 'm_' + str(mIndex)
                        children[k] = childElem
                        ChildrenOrder.append(k)

                    else:
                        for k in childElem:
                            children[k] = childElem[k]
                            ChildrenOrder.append(k)


        # children = sortChildrenV(children)
        return {
            'type': 'v',
            'children': children,
            'order': ChildrenOrder,
        }

    else:
        print('垂直不能分割')
        return checkHorizontal(sortElemV, sortElemH)

def checkHorizontal(sortElemV, sortElemH):

    print('bbbbb')
    splitArr = splitElems(sortElemH)
    if (len(splitArr) > 1):
        print('checkHorizontal 可以分割')
        print(splitArr)

        elemsJson = {type: 'h'}
        children = {}
        ChildrenOrder = []
        # children = collections.OrderedDict()
        for elems in splitArr:
            if (len(elems) == 2):
                eId = getElemId(elems[0])
                children[eId] = {}
                ChildrenOrder.append(eId)
            else:
                print('*****')
                elemV = getElems(elems, sortElemV)
                childElem = checkIn(elemV, elems)
                print(childElem)
                if childElem:
                    if 'type' in childElem:
                        k = globalData.getId() # 'm_' + str(mIndex)
                        children[k] = childElem
                        ChildrenOrder.append(k)

                    else:
                        for k in childElem:
                            children[k] = childElem[k]
                            ChildrenOrder.append(k)

        print(children)
        # children = sortChildrenH(children)
        return {
            'type': 'h',
            'children': children,
            'order': ChildrenOrder,
        }

    else:
        # print sortElemV
        print('水平不能分割')
        return checkAbsolute(sortElemV, sortElemH)


def getAbsElems(sortElemV, sortElemH):
    elemHOrder = {}
    index = 0
    for v in sortElemH:
        sArr = v[0].split('*')
        eId = sArr[0]
        b = sArr[1]

        if (b == '0'):
            elemHOrder[eId] = []
            elemHOrder[eId].append(index)
        else:
            elemHOrder[eId].append(index)

        index += 1


    absMap = {}
    elemsLen = {}
    elemsInvalid = {}
    for v in sortElemV:
        sArr = v[0].split('*')
        eId = sArr[0]
        b = sArr[1]

        # 把之前的都加一
        for e in elemsLen:
            elemsLen[e] += 1
        for e in elemsInvalid:
            elemsInvalid[e] += 1

        if (b == '0'):
            elemsLen[eId] = 0
        else:
            elemsInvalid[eId] = 0

            absMap[eId] = []
            for e2 in list(elemsInvalid):
                if elemsLen[e2] < elemsLen[eId]:
                    # 垂直方向在范围中
                    if (elemHOrder[eId][0] < elemHOrder[e2][0] and elemHOrder[eId][1] > elemHOrder[e2][1]):
                        if (e2 in absMap):
                            for child in absMap[e2]:
                                absMap[eId].append(child)
                            del absMap[e2]
                        absMap[eId].append(e2)
                        del elemsInvalid[e2]

    return absMap


# 因为没有布局，需要用绝对布局，从底层一个一个提出来
def checkAbsolute(sortElemV, sortElemH):

    print(sortElemV)
    print(sortElemH)

    # 先把包含的先剔除掉
    absElems = getAbsElems(sortElemV, sortElemH)
    # absElemsH = getAbsElems(sortElemH)

    absOrder = []
    childrenTree = {}
    for eId in absElems:
        childElem = absElems[eId]
        childElemH = []
        childElemV = []
        childrenTree[eId] = {}
        absOrder.append(eId)

        if len(childElem) > 0:
            # 把子类的排序放一起排序
            for e in sortElemH:
                cId  = getElemId(e)
                if cId in childElem:
                    childElemH.append(e)

            for e in sortElemV:
                cId  = getElemId(e)
                if cId in childElem:
                    childElemV.append(e)

            childElemCode = checkIn(childElemV, childElemH)

            childrenTree[eId] = childElemCode


    res = {}
    k = globalData.getId()
    res[k] = {
        'type': 'abs',
        'children': childrenTree,
        'order': absOrder,
        'absChildren': childrenTree,
    }
    # ChildrenOrder.append(k)

    return res

def sortElem(a, b):
    if (a[0].endswith('*1') and b[0].endswith('*1')):
        if (a[1] == b[1]):
            return -1

    return a[1] - b[1]

# 竖屏排序
def sortLayoutV(elems):
    elemVs = {}

    for uId in elems:
        elemVs[uId + '*0'] = elems[uId]['y']
        elemVs[uId + '*1'] = elems[uId]['b']

    # sortElems = sorted(elemVs.items(), key=lambda x:x[1])
    sortElems = sorted(elemVs.items(), key=functools.cmp_to_key(sortElem))

    print(sortElems)
    return sortElems

# 横屏排序
def sortLayoutH(elems):
    elemHs = {}

    for uId in elems:
        elemHs[uId + '*0'] = elems[uId]['x']
        elemHs[uId + '*1'] = elems[uId]['r']

    # sortElems = sorted(elemHs.items(), key=lambda x:x[1])
    sortElems = sorted(elemHs.items(), key=functools.cmp_to_key(sortElem))
    print(sortElems)
    return sortElems




# 切割元素列表 看看能不能分割
def splitElems(elems):
    uId = getElemId(elems[0])

    splitArr = [[]]
    elemList = []

    for i in range(0, len(elems)):
        curElemId = getElemId(elems[i])
        # pos = elemList.index(curElemId)
        if curElemId in elemList:
            elemList.remove(curElemId)
        else:
            elemList.append(curElemId)

        splitArr[len(splitArr) - 1].append(elems[i])

        if len(elemList) == 0 and len(elems)-1 != i:
            # 没有元素
            splitArr.append([])

        # if (uId == curElemId):
        #     if elems[i][0].endswith('_0'):
        #         splitArr.append([])
        #         splitArr[len(splitArr) - 1].append(elems[i])
        #     else:
        #         splitArr[len(splitArr) - 1].append(elems[i])
        #         if not (i == len(elems) - 1):
        #             splitArr.append([])
        #     continue
        #
        # if (len(splitArr[len(splitArr) - 1]) == 0):
        #     uId = getElemId(elems[i])
        #
        # splitArr[len(splitArr) - 1].append(elems[i])

    print(splitArr)
    return splitArr

def getElemId(elem):
    sArr = elem[0].split('*')
    return sArr[0]

def getElems(src, dist):
    res = []
    for elem in dist:
        for elem1 in src:
            if elem[0] == elem1[0]:
                res.append(elem)

    return res

def addElemData(tree, elemsData):
    addNewElemData(tree, elemsData)
    addFlex(tree, '')

# 最后把新添加的元素frame加上
def addNewElemData(tree, elemsData):
    global layoutElemData

    if 'type' in tree:
        for elemKey in tree['children']:
            if 'children' in tree['children'][elemKey]:
                addNewElemData(tree['children'][elemKey]['children'], elemsData)
            else:
                addNewElemData(tree['children'][elemKey], elemsData)

            if not elemKey in layoutElemData:
                mElemData = getMElemData(tree['children'][elemKey]['children'])
                layoutElemData[elemKey] = mElemData
                elemsData[elemKey] = {'frame': mElemData, 'type': 'View'}
                elemsData[elemKey] = {'frame': mElemData, 'type': 'View'}


    else:
        for elemKey in tree:
            if 'children' in tree[elemKey]:
                addNewElemData(tree[elemKey]['children'], elemsData)
            else:
                addNewElemData(tree[elemKey], elemsData)

            if not elemKey in layoutElemData:
                mElemData = {}
                if 'children' in tree[elemKey]:
                    mElemData = getMElemData(tree[elemKey]['children'])
                else:
                    mElemData = getMElemData(tree[elemKey])
                layoutElemData[elemKey] = mElemData
                elemsData[elemKey] = {'frame': mElemData, 'type': 'View'}


def getMElemData(children):
    global layoutElemData

    print('a')
    x = []
    y = []
    for elemKey in children:
        x.append(layoutElemData[elemKey]['x'])
        x.append(layoutElemData[elemKey]['r'])
        y.append(layoutElemData[elemKey]['y'])
        y.append(layoutElemData[elemKey]['b'])


    x.sort()
    y.sort()
    print(x)
    print(y)
    return {
        'x': x[0],
        'y': y[0],
        'r': x[len(x) - 1],
        'b': y[len(y) - 1],
        'width': x[len(x) - 1] - x[0],
        'height': y[len(y) - 1] - y[0],
    }

def addFlex(tree, parentId):
    global layoutElemData

    parentX = 0
    parentY = 0
    if (parentId != ''):
        parentX = layoutElemData[parentId]['x']
        parentY = layoutElemData[parentId]['y']

    if 'type' in tree:
        for elemKey in tree['children']:
            elemData = tree['children'][elemKey]
            if 'children' in elemData:
                addFlex(elemData['children'], elemKey)

            layoutElemData[elemKey]['left'] = layoutElemData[elemKey]['x'] - parentX
            layoutElemData[elemKey]['top'] = layoutElemData[elemKey]['y'] - parentY


    else:
        for elemKey in tree:
            if 'children' in tree[elemKey]:
                addFlex(tree[elemKey]['children'], elemKey)
            else:
                addFlex(tree[elemKey], elemKey)

            layoutElemData[elemKey]['left'] = layoutElemData[elemKey]['x'] - parentX
            layoutElemData[elemKey]['top'] = layoutElemData[elemKey]['y'] - parentY




