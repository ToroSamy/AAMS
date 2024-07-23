import wx

def setTextBox(panel, label, initValue, isPassword=0):
    setTextMessage = wx.StaticText(parent=panel, label=label)
    if isPassword != 0:
        setTextTextCtrl = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER | wx.TE_PASSWORD, value=initValue)
    else:
        setTextTextCtrl = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, value=initValue)
    setTextTextCtrl.Bind(wx.EVT_SET_FOCUS, lambda event: onSetFocus(event,setTextTextCtrl, initValue))
    setTextTextCtrl.Bind(wx.EVT_KILL_FOCUS, lambda event: onKillFocus(event,setTextTextCtrl, initValue))
    box = wx.BoxSizer(wx.HORIZONTAL)
    box.Add(setTextMessage, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE)
    box.Add(setTextTextCtrl, proportion=5, flag=wx.CENTER | wx.ALL | wx.FIXED_MINSIZE)
    return setTextTextCtrl, box
def onKillFocus(event,textCtrl, initValue):
    if textCtrl.GetValue() == "":
        textCtrl.SetValue(initValue)
    event.Skip()
def onSetFocus(event,textCtrl, initValue):
    if textCtrl.GetValue() == initValue:
        textCtrl.SetValue("")
    event.Skip()

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
    if choice == 0:
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


