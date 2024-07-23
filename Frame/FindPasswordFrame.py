import wx

from GlobalFunc.Frame import AbstractFrameC, AbstractFrame
from GlobalFunc.FrameParts import setTextBox


class FindPasswordFrame(AbstractFrameC):
    def __init__(self, title,returntoback,aams):
        super().__init__(title,returntoback,aams)
        self.nameValue,name = setTextBox(self.panel,"用户名","请输入用户名")
        self.idValue,mid = setTextBox(self.panel,"身份证","请输入身份证")
        self.phoneValue,phone = setTextBox(self.panel,"手机号","请输入手机")
        findButton = wx.Button(self.panel, id=1, label="点击验证")
        self.vbox.Add(name, proportion=1, flag=wx.CENTER)
        self.vbox.Add(mid, proportion=1, flag=wx.CENTER)
        self.vbox.Add(phone, proportion=1, flag=wx.CENTER)
        self.vbox.Add(self.codeBox, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(findButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.frame.Show()
    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyName = self.nameValue.GetValue()
            userKeyId = self.idValue.GetValue()
            userKeyPhone = self.phoneValue.GetValue()
            flag, group, loc = self.aams.findPassword(userKeyName, userKeyId, userKeyPhone)
            if flag:
                self.frame.Hide()
                ChangePasswordFrame('修改密码', self.returnToBack, self.aams, loc,group)

class ChangePasswordFrame(AbstractFrame):
    def __init__(self, title,returntoback,aams,loc,group):
        super().__init__(title,returntoback,aams,loc)
        self.group = group
        self.passwordValue1, password1 = setTextBox(self.panel, '输入密码', '', 1)
        self.passwordValue2, password2 = setTextBox(self.panel, '重复密码', '', 1)
        self.changePasswordButton = wx.Button(self.panel, id=1, label="点击修改")
        self.vbox.Add(password1, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(password2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.changePasswordButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.frame.Show()
    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyPassword1 = self.passwordValue1.GetValue()
            userKeyPassword2 = self.passwordValue2.GetValue()
            if self.aams.changePassword(userKeyPassword1, userKeyPassword2, self.group, self.loc):
                self.frame.Hide()
                self.returntoback()
