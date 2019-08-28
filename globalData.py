

elemData = {}
idBaseIndex = 0
pageName = ''

def getId():
    global idBaseIndex
    idBaseIndex += 1
    return 'id_' + str(idBaseIndex)

def setPageName(name):
    global pageName
    pageName = name

def getPageName():
    global pageName
    return pageName