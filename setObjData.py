import rhinoscriptsyntax as rs
import trkRhinoPy as trp

objs = rs.GetObjects('select objects', preselect=True)

rs.EnableRedraw(False)

keys = 'usage func type'

def Func(x):
    trp.valuesFromLayer(x)
    trp.setValueByLayer(x,keys)
    trp.setObjAreaValue(x)
    trp.setBrepHeight(x)
    

def setClass(obj):
    classKeys = 'units public'
    try:
        func = rs.GetUserText(obj, "func")
        if func in classKeys:
            classValue = func
        else:
            classValue = "na"
        rs.SetUserText(obj, "class", classValue)
    except:
        return

def applyFunc(objs):
    map(Func, objs)
    map(setClass, objs)

if objs:
    applyFunc(objs)


'''class data'''




rs.EnableRedraw(True)