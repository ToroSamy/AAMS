import wx

from Frame.FindPasswordFrame import FindPasswordFrame
from Frame.LoginFrame import LoginFrame
from Frame.RegisterFrame import RegisterFrame


class StartFrame(wx.Frame):
    def __init__(self, globalpanel):
        super().__init__(None, title="开始菜单", size=(300, 250), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)
        self.gp = globalpanel

        loginButton = wx.Button(parent=panel, id=1, label="登录系统", pos=(50, 10))
        registerButton = wx.Button(parent=panel, id=2, label="注册系统", pos=(50, 10))
        findPasswordFrame = wx.Button(parent=panel, id=3, label="找回密码", pos=(50, 10))

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(loginButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(registerButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(findPasswordFrame, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.onClick, id=1, id2=3)

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            self.Hide()
            loginFrame = LoginFrame(self.gp, self.returnToBack)
            loginFrame.Show()

            # 具体内容后面实现
        elif eventId == 2:
            self.Hide()
            registerFrame = RegisterFrame(self.gp, self.returnToBack)
            registerFrame.Show()

        elif eventId == 3:
            self.Hide()
            findPasswordFrame = FindPasswordFrame(self.gp, self.returnToBack)
            findPasswordFrame.Show()

    def returnToBack(self):
        self.Show()
