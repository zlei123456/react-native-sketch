import json
import math
import utils
import globalData

# 数据结构（解析后的）
# {
#     id: {
#         type: 'View',
#         frame: {x: x, y: y, width: width, height: height},
#         style: {},
#     }
# }

def parseSketch(filePath, outputPages):
    globalData.elemData = {}

    with open(filePath, 'r') as f:
        load_dict = json.load(f)
        print (load_dict['layers'])

        if not (load_dict['name'] in outputPages):
            return False


        globalData.setPageName(load_dict['name'])
        for layer in load_dict['layers']:
            print (layer['frame'])
            if (layer['name'] == 'iPhone 8'):
                dealScreen(layer['frame'])
                print (layer['layers'])
                for layerData in layer['layers']:
                    dealLayerData(layerData)

            elif (layer['name'] == 'root'):
                dealScreen(layer['frame'])
                # print (layer['layers'])
                for layerData in layer['layers']:
                    dealLayerData(layerData)
            else:
                dealLayerData(layer)

    return True



def dealLayerData(layerData, offPos={'x':0, 'y':0}):
    if (layerData['_class'] == 'rectangle'):
        dealRectangle(layerData, offPos)
    elif (layerData['_class'] == 'oval'):
        dealOval(layerData, offPos)
    elif (layerData['_class'] == 'bitmap'):
        dealImage(layerData, offPos)
    elif (layerData['_class'] == 'text'):
        dealText(layerData, offPos)

    elif (layerData['_class'] == 'symbolInstance'):
        dealSymbol(layerData, offPos)
    elif (layerData['_class'] == 'group'):
        frameData = dealGroup(layerData)
        off = {'x': frameData['x'] + offPos['x'], 'y': frameData['y'] + offPos['y']}
        for layerData2 in layerData['layers']:
            dealLayerData(layerData2, off)

    else:
        print('no layer')
        print(layerData['_class'])

def dealScreen(layerFrame):
    rectangleData = {}
    rectangleData['frame'] = {'x': 0, 'y': 0, 'width': layerFrame['width'], 'height': layerFrame['height']}
    print(rectangleData)

    rectangleData['type'] = 'View'

    # id = globalData.getId()
    id = 'root'
    globalData.elemData[id] = rectangleData

def dealSymbol(layerData, offPos):
    rectangleData = {}
    rectangleData['name'] = layerData['name'].replace(' ', '')
    rectangleData['frame'] = {'x': layerData['frame']['x'] + offPos['x'], 'y': layerData['frame']['y'] + offPos['y'], 'width': layerData['frame']['width'], 'height': layerData['frame']['height']}
    print(rectangleData)

    rStyle = rectangleData['frame'].copy()


    rectangleData['style'] = rStyle

    rectangleData['type'] = 'View'

    # id = globalData.getId()
    id = rectangleData['name']
    globalData.elemData[id] = rectangleData

def dealGroup(layerData):
    rectangleData = {}
    rectangleData['name'] = layerData['name'].replace(' ', '')
    rectangleData['frame'] = {'x': layerData['frame']['x'], 'y': layerData['frame']['y'], 'width': layerData['frame']['width'], 'height': layerData['frame']['height']}
    # print(rectangleData)
    #
    # rStyle = rectangleData['frame'].copy()
    #
    # # # backgroundColor
    # # fillColor = layerData['style']['fills'][0]['color']
    # rStyle['backgroundColor'] = '#f00'
    #
    #
    # # rStyle['borderWidth'] = layerData['style']['borders'][0]['thickness']
    # # borderColor = layerData['style']['borders'][0]['color']
    # # rStyle['borderColor'] = utils.getColorStr(borderColor)
    # # rStyle['borderRadius'] = layerData['fixedRadius']
    #
    #
    # rectangleData['style'] = rStyle
    #
    # rectangleData['type'] = 'View'
    #
    # # id = globalData.getId()
    # id = rectangleData['name']
    # globalData.elemData[id] = rectangleData
    return rectangleData['frame']

def dealRectangle(layerData, offPos):
    rectangleData = {}
    rectangleData['name'] = layerData['name'].replace(' ', '')
    rectangleData['frame'] = {'x': layerData['frame']['x'] + offPos['x'], 'y': layerData['frame']['y'] + offPos['y'], 'width': layerData['frame']['width'], 'height': layerData['frame']['height']}
    print(rectangleData)

    rStyle = rectangleData['frame'].copy()

    # backgroundColor
    fillColor = layerData['style']['fills'][0]['color']
    rStyle['backgroundColor'] = utils.getColorStr(fillColor);


    rStyle['borderWidth'] = layerData['style']['borders'][0]['thickness']
    borderColor = layerData['style']['borders'][0]['color']
    rStyle['borderColor'] = utils.getColorStr(borderColor)
    rStyle['borderRadius'] = layerData['fixedRadius']


    rectangleData['style'] = rStyle

    rectangleData['type'] = 'View'

    # id = globalData.getId()
    id = rectangleData['name']
    globalData.elemData[id] = rectangleData
    # return rectangleData

def dealOval(layerData, offPos):
    rectangleData = {}
    rectangleData['name'] = layerData['name'].replace(' ', '')
    rectangleData['frame'] = {'x': layerData['frame']['x'] + offPos['x'], 'y': layerData['frame']['y'] + offPos['y'], 'width': layerData['frame']['width'], 'height': layerData['frame']['height']}
    print(rectangleData)

    rStyle = rectangleData['frame'].copy()

    # backgroundColor
    fillColor = layerData['style']['fills'][0]['color']
    rStyle['backgroundColor'] = utils.getColorStr(fillColor);


    rStyle['borderWidth'] = layerData['style']['borders'][0]['thickness']
    borderColor = layerData['style']['borders'][0]['color']
    rStyle['borderColor'] = utils.getColorStr(borderColor)
    if layerData['frame']['width'] == layerData['frame']['height']:
        rStyle['borderRadius'] = layerData['frame']['width'] / 2
    else:
        if layerData['frame']['width'] > layerData['frame']['height']:
            rStyle['borderRadius'] = layerData['frame']['width'] / 2
        else:
            rStyle['borderRadius'] = layerData['frame']['height'] / 2


    rectangleData['style'] = rStyle

    rectangleData['type'] = 'View'

    # id = globalData.getId()
    id = rectangleData['name']
    globalData.elemData[id] = rectangleData

def dealImage(layerData, offPos):
    imgData = {}
    imgData['name'] = layerData['name'].replace(' ', '')
    imgData['frame'] = {'x': layerData['frame']['x'] + offPos['x'], 'y': layerData['frame']['y'] + offPos['y'], 'width': layerData['frame']['width'], 'height': layerData['frame']['height']}
    print(imgData)

    rStyle = imgData['frame'].copy()

    imgData['style'] = rStyle

    # source
    if (layerData['exportOptions'] and layerData['exportOptions']['exportFormats'] and layerData['exportOptions']['exportFormats'][0]):
        imgData['source'] = layerData['exportOptions']['exportFormats'][0]['name'] + '.' + layerData['exportOptions']['exportFormats'][0]['fileFormat']

    imgData['type'] = 'Image'

    # id = globalData.getId()
    id = imgData['name']
    globalData.elemData[id] = imgData

def dealText(layerData, offPos):
    textData = {}
    textData['name'] = layerData['name'].replace(' ', '')
    textData['frame'] = {'x': layerData['frame']['x'] + offPos['x'], 'y': layerData['frame']['y'] + offPos['y'], 'width': layerData['frame']['width'], 'height': layerData['frame']['height']}
    print(textData)

    rStyle = textData['frame'].copy()

    if (layerData['attributedString']):
        textData['value'] = layerData['attributedString']['string']
        if(len(layerData['attributedString']['attributes']) == 1):
            rStyle['color'] = utils.getColorStr(layerData['attributedString']['attributes'][0]['attributes']['MSAttributedStringColorAttribute'])
            rStyle['fontSize'] = layerData['attributedString']['attributes'][0]['attributes']['MSAttributedStringFontAttribute']['attributes']['size']
            fontFa = layerData['attributedString']['attributes'][0]['attributes']['MSAttributedStringFontAttribute']['attributes']['name']

            fontF = fontFa.split('-')
            # rStyle['fontFamily'] = fontFa
            if (len(fontF) > 1):
                if(fontF[1] == 'Medium' or fontF[1] == 'Semibold'):
                    rStyle['fontWeight'] = 'bold'


            # 计算新的行高
            sLineHeight = math.floor(rStyle['fontSize'] * 1.4 + 0.5)
            lineNum = math.floor(rStyle['height'] / sLineHeight + 0.5)
            lineHeight = math.floor(rStyle['height'] / lineNum)
            rStyle['lineHeight'] = lineHeight

        else:
            rStyle['color'] = []
            rStyle['fontSize'] = []
            rStyle['fontWeight'] = []
            rStyle['fontLength'] = []
            maxLineHeight = 0
            for attr in layerData['attributedString']['attributes']:
                rStyle['color'].append(utils.getColorStr(attr['attributes']['MSAttributedStringColorAttribute']))
                rStyle['fontSize'].append(attr['attributes']['MSAttributedStringFontAttribute']['attributes']['size'])
                fontFa = attr['attributes']['MSAttributedStringFontAttribute']['attributes']['name']
                fontF = fontFa.split('-')
                if (len(fontF) > 1 and (fontF[1] == 'Medium' or fontF[1] == 'Semibold')):
                    rStyle['fontWeight'].append('blod')
                else:
                    rStyle['fontWeight'].append('normal')

                # # 计算新的行高
                # sLineHeight = math.floor(rStyle['fontSize'] * 1.4 + 0.5)
                # lineNum = math.floor(rStyle['height'] / sLineHeight + 0.5)
                # lineHeight = math.floor(rStyle['height'] / lineNum)
                # if (maxLineHeight < lineHeight):
                #     maxLineHeight = lineHeight

                rStyle['fontLength'].append(attr['length'])


    textData['style'] = rStyle
    textData['type'] = 'Text'

    # id = globalData.getId()
    id = textData['name']
    globalData.elemData[id] = textData

# parseSketch('./demo0.json')
# print(globalData.elemData)