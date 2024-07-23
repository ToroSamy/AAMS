import wx


from GlobalPanel import outCode


class RegisterFrame(wx.Frame):
    def __init__(self, globalpanel,returntoback):
        super().__init__(None, title="注册界面", size=(300, 400), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)
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

        # 密码
        passwordMessage1 = wx.StaticText(parent=panel, label="输入密码")
        self.passwordTextCtrl1 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)

        passwordMessage2 = wx.StaticText(parent=panel, label="重复密码")
        self.passwordTextCtrl2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)

        # 验证码
        self.code = outCode()
        self.codeTextCtrl = wx.TextCtrl(panel)
        self.codeTextCtrl.SetValue('请输入验证码')
        self.codeButton = wx.Button(parent=panel, id=2, label=f"{self.code}", pos=(100, 50))

        registerButton = wx.Button(parent=panel, id=1, label="点击注册", pos=(100, 50))
        returnButton = wx.Button(parent=panel, id=3, label="点击返回", pos=(100, 50))

        hboxName = wx.BoxSizer(wx.HORIZONTAL)
        hboxName.Add(userNameMesaage, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxName.Add(self.userNameTextCtrl, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        hboxId = wx.BoxSizer(wx.HORIZONTAL)
        hboxId.Add(userIdMesaage, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxId.Add(self.userIdTextCtrl, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        hboxPhone = wx.BoxSizer(wx.HORIZONTAL)
        hboxPhone.Add(userPhoneMesaage, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxPhone.Add(self.userPhoneTextCtrl, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        hboxPassword1 = wx.BoxSizer(wx.HORIZONTAL)
        hboxPassword1.Add(passwordMessage1, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxPassword1.Add(self.passwordTextCtrl1, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        hboxPassword2 = wx.BoxSizer(wx.HORIZONTAL)
        hboxPassword2.Add(passwordMessage2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxPassword2.Add(self.passwordTextCtrl2, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        hboxCode = wx.BoxSizer(wx.HORIZONTAL)
        hboxCode.Add(self.codeTextCtrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxCode.Add(self.codeButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # 创建垂直方向的盒子布局管理器对象vbox
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(hboxName, proportion=1, flag=wx.CENTER)
        vbox1.Add(hboxId, proportion=1, flag=wx.CENTER)
        vbox1.Add(hboxPhone, proportion=1, flag=wx.CENTER)

        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox2.Add(hboxPassword1, proportion=1, flag=wx.CENTER)
        vbox2.Add(hboxPassword2, proportion=1, flag=wx.CENTER)

        vbox3 = wx.BoxSizer(wx.VERTICAL)
        vbox3.Add(hboxCode, proportion=1, flag=wx.CENTER)
        vbox3.Add(registerButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox3.Add(returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(vbox1, proportion=1, flag=wx.CENTER)
        vbox.Add(vbox2, proportion=1, flag=wx.CENTER)
        vbox.Add(vbox3, proportion=1, flag=wx.CENTER)
        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.onClick, id=1, id2=3)

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyName = self.userNameTextCtrl.GetValue()
            userKeyId = self.userIdTextCtrl.GetValue()
            userKeyPhone = self.userPhoneTextCtrl.GetValue()
            userKeyPassword1 = self.passwordTextCtrl1.GetValue()
            userKeyPassword2 = self.passwordTextCtrl2.GetValue()
            userKeyCode = self.codeTextCtrl.GetValue()

            self.gp.registerUser(userKeyName,userKeyId,userKeyPhone,userKeyPassword1,userKeyPassword2,userKeyCode,self.code)
        elif eventId == 2:
            self.code = outCode()
            self.codeButton.SetLabel(f"{self.code}")
        elif eventId == 3:
            self.Hide()
            self.returntoback()