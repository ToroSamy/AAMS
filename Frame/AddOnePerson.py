import wx

from GlobalFunc.Frame import AbstractFrame
from GlobalFunc.FrameParts import setTextBox, setButtons

class AddOnePerson(AbstractFrame):
    def __init__(self, title,returntoback,aams,choice="has"):
        super().__init__(title,returntoback,aams,choice)
        self.nameValue,name = setTextBox(self.panel,"用户名","请输入用户名")
        self.idValue,mid = setTextBox(self.panel,"身份证","请输入身份证")
        self.phoneValue,phone = setTextBox(self.panel,"手机号","请输入手机号")

        sexDict = {1: "男", 2: "女"}
        sexButton = setButtons(self.panel,sexDict,"性别")
        self.sexButton = sexButton.GetChildren()
        self.choice = choice
        self.passwordValue1,password1 = setTextBox(self.panel,"输入密码","",1)
        self.passwordValue2,password2 = setTextBox(self.panel,"重复密码","",1)
        registerButton = wx.Button(self.panel, id=1, label="点击注册")
        self.vbox.Add(name, proportion=1, flag=wx.CENTER)
        self.vbox.Add(mid, proportion=1, flag=wx.CENTER)
        self.vbox.Add(phone, proportion=1, flag=wx.CENTER)
        self.vbox.Add(sexButton, proportion=1, flag=wx.CENTER)
        self.vbox.Add(password1, proportion=1, flag=wx.CENTER)
        self.vbox.Add(password2, proportion=1, flag=wx.CENTER)
        if choice == "has":
            self.vbox.Add(self.codeBox, proportion=1, flag=wx.CENTER)
        self.vbox.Add(registerButton, proportion=1, flag=wx.CENTER)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.CENTER)
        self.frame.Show()
    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyName = self.nameValue.GetValue()
            userKeyId = self.idValue.GetValue()
            userKeyPhone = self.phoneValue.GetValue()
            userKeyPassword1 = self.passwordValue1.GetValue()
            userKeyPassword2 = self.passwordValue2.GetValue()
            userChoiceSex = self.sexButton[1].GetWindow().GetValue()
            if self.choice == "has":
                userKeyCode = self.keyCode.GetValue()
                self.aams.addOnePerson(userKeyName, userKeyId, userKeyPhone, userKeyPassword1, userKeyPassword2,
                                       userChoiceSex, self.choice, userKeyCode, self.code)
                self.reloadCode(event)
            else:
                self.aams.addOnePerson(userKeyName, userKeyId, userKeyPhone, userKeyPassword1, userKeyPassword2,
                                       userChoiceSex, self.choice)