import wx

from GlobalPanel import outCode


class FindPasswordFrame(wx.Frame):

    def __init__(self, globalpanel, returntoback):
        super().__init__(None, title="找回密码", size=(300, 270), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)
        # 用户名

        self.gp = globalpanel
        self.returntoback = returntoback
        userNameMesaage = wx.StaticText(parent=panel, label="用户名")
        self.userNameTextCtrl = wx.TextCtrl(panel)
        self.userNameTextCtrl.SetValue('请输入用户名')

        userIdMesaage = wx.StaticText(parent=panel, label="身份证")
        self.userIdTextCtrl = wx.TextCtrl(panel)
        self.userIdTextCtrl.SetValue('请输入身份证')

        userPhoneMesaage = wx.StaticText(parent=panel, label="手机号")
        self.userPhoneTextCtrl = wx.TextCtrl(panel)
        self.userPhoneTextCtrl.SetValue('请输入手机号')

        self.findPasswordButton = wx.Button(parent=panel, id=1, label="点击验证", pos=(100, 50))
        self.returnButton = wx.Button(parent=panel, id=2, label="点击返回", pos=(100, 50))

        hboxName = wx.BoxSizer(wx.HORIZONTAL)
        hboxName.Add(userNameMesaage, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxName.Add(self.userNameTextCtrl, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        hboxId = wx.BoxSizer(wx.HORIZONTAL)
        hboxId.Add(userIdMesaage, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxId.Add(self.userIdTextCtrl, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        hboxPhone = wx.BoxSizer(wx.HORIZONTAL)
        hboxPhone.Add(userPhoneMesaage, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxPhone.Add(self.userPhoneTextCtrl, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hboxName, proportion=1, flag=wx.CENTER)
        vbox.Add(hboxId, proportion=1, flag=wx.CENTER)
        vbox.Add(hboxPhone, proportion=1, flag=wx.CENTER)
        vbox.Add(self.findPasswordButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(self.returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.onClick, id=1, id2=3)

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyName = self.userNameTextCtrl.GetValue()
            userKeyId = self.userIdTextCtrl.GetValue()
            userKeyPhone = self.userPhoneTextCtrl.GetValue()

            flag, group, loc = self.gp.findPassword(userKeyName, userKeyId, userKeyPhone)
            if flag:
                self.Hide()
                changePasswordFrame = ChangePasswordFrame(self.gp, group, loc, self.returnToBack)
                changePasswordFrame.Show()
        elif eventId == 2:
            self.Hide()
            self.returntoback()

    def returnToBack(self):
        self.Show()


class ChangePasswordFrame(wx.Frame):
    def __init__(self, globalpanel, group, loc, returntoback):
        super().__init__(None, title="修改密码", size=(300, 180), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)
        self.gp = globalpanel
        self.returntoback = returntoback
        self.group = group
        self.loc = loc
        passwordMessage1 = wx.StaticText(parent=panel, label="输入密码")
        self.passwordTextCtrl1 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)

        passwordMessage2 = wx.StaticText(parent=panel, label="重复密码")
        self.passwordTextCtrl2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)

        self.changePasswordButton = wx.Button(parent=panel, id=1, label="点击修改", pos=(100, 50))

        hboxPassword1 = wx.BoxSizer(wx.HORIZONTAL)
        hboxPassword1.Add(passwordMessage1, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxPassword1.Add(self.passwordTextCtrl1, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        hboxPassword2 = wx.BoxSizer(wx.HORIZONTAL)
        hboxPassword2.Add(passwordMessage2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxPassword2.Add(self.passwordTextCtrl2, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hboxPassword1, proportion=1, flag=wx.CENTER)
        vbox.Add(hboxPassword2, proportion=1, flag=wx.CENTER)
        vbox.Add(self.changePasswordButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.onClick, id=1, id2=3)

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyPassword1 = self.passwordTextCtrl1.GetValue()
            userKeyPassword2 = self.passwordTextCtrl2.GetValue()
            if self.gp.changePassword(userKeyPassword1, userKeyPassword2, self.group, self.loc):
                self.Hide()
                self.returntoback()
