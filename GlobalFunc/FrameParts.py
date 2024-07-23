import wx

from GlobalFunc.Func import outCode
def setTextBox(panel, label, initVault, choice=0):
        setTextMesaage = wx.StaticText(parent=panel, label=label)
        if choice != 0:
            setTextTextCtrl = wx.TextCtrl(panel,style=wx.TE_PASSWORD)
        else:
            setTextTextCtrl = wx.TextCtrl(panel)
            setTextTextCtrl.SetValue(f"{initVault}")
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(setTextMesaage, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE)
        box.Add(setTextTextCtrl, proportion=5, flag=wx.CENTER | wx.ALL | wx.FIXED_MINSIZE)
        return setTextTextCtrl,box


def setButtons(panel, myDict, label,choice=0):
    message = wx.StaticText(parent=panel, label=label)
    number = len(myDict)
    keys = myDict.keys()
    keyList = []
    valueList = []
    box = wx.BoxSizer(wx.HORIZONTAL)
    box.Add(message, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE)
    for key in keys:
        keyList.append(key)
        valueList.append(myDict[key])
    if choice != 0:
        button = wx.RadioButton(panel, id=keyList[0], label=valueList[0],style=wx.RB_GROUP)
        box.Add(button, proportion=1, flag=wx.EXPAND)
        for i in range(number):
            if i+1 == number:
                return box
            button1 = wx.RadioButton(panel, id=keyList[i+1], label=valueList[i+1])
            box.Add(button1, proportion=1, flag=wx.EXPAND)
    else:
        for i in range(number):
            button = wx.CheckBox(panel, id=keyList[i], label=valueList[i])
            box.Add(button, proportion=1, flag=wx.EXPAND)
    return box


