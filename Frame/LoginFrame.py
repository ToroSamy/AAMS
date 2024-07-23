import wx

from Frame.ErrorFrame import ErrorFrame
from GlobalPanel import outCode
# LoginFrame.py
from ManagerSystem.AdminManage import AdminManage
from ManagerSystem.StudentManage import StudentManage
from ManagerSystem.TeacherManage import TeacherManage


class LoginFrame(wx.Frame):

    def __init__(self, globalpanel, returntoback):
        super().__init__(None, title="登录界面", size=(300, 270), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)
        # 用户名

        self.gp = globalpanel
        self.returntoback = returntoback

        userNameMesaage = wx.StaticText(parent=panel, label="用户名")
        self.userNameTextCtrl = wx.TextCtrl(panel)
        self.userNameTextCtrl.SetValue('请输入用户名')
        # 密码
        passwordMessage = wx.StaticText(parent=panel, label="密码")
        self.passwordTextCtrl = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        # 验证码
        self.code = outCode()
        self.codeTextCtrl = wx.TextCtrl(panel)
        self.codeTextCtrl.SetValue('请输入验证码')
        self.codeButton = wx.Button(parent=panel, id=11, label=f"{self.code}", pos=(100, 50))

        loginButton = wx.Button(parent=panel, id=10, label="点击登录", pos=(100, 50))
        returnButton = wx.Button(parent=panel, id=12, label="点击返回", pos=(100, 50))

        hboxName = wx.BoxSizer(wx.HORIZONTAL)
        hboxName.Add(userNameMesaage, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxName.Add(self.userNameTextCtrl, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        hboxPassword = wx.BoxSizer(wx.HORIZONTAL)
        hboxPassword.Add(passwordMessage, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxPassword.Add(self.passwordTextCtrl, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        hboxCode = wx.BoxSizer(wx.HORIZONTAL)
        hboxCode.Add(self.codeTextCtrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxCode.Add(self.codeButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # 创建垂直方向的盒子布局管理器对象vbox
        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(hboxName, proportion=1, flag=wx.CENTER)
        vbox.Add(hboxPassword, proportion=1, flag=wx.CENTER)
        vbox.Add(hboxCode, proportion=1, flag=wx.CENTER)
        vbox.Add(loginButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.onClick, id=10, id2=20)
        self.Show()
        self.times = 3

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 10:
            userKeyName = self.userNameTextCtrl.GetValue()
            userKeyPassword = self.passwordTextCtrl.GetValue()
            userKeyCode = self.codeTextCtrl.GetValue()

            ifCodeRight, group, loc = self.gp.loginCheckCode(userKeyName, userKeyCode, self.code)

            if ifCodeRight:
                self.times -= 1
                if not self.gp.loginSystem(userKeyPassword, group, loc):
                    errorFrame = ErrorFrame(f"密码错误，您还有 " + str(self.times) + " 次机会!")
                    errorFrame.ShowModal()
                    errorFrame.Destroy()
                else:
                    self.times = 3
                    if group == 1:
                        self.Hide()
                        adminManage = AdminManage(self.gp, loc, self.returnToBack)
                        adminManage.Show()
                    elif group == 2:
                        self.Hide()
                        teacherManage = TeacherManage(self.gp, loc, self.returnToBack)
                        teacherManage.Show()
                    elif group == 3:
                        self.Hide()
                        studentManage = StudentManage(self.gp, loc, self.returnToBack)
                        studentManage.Show()
                if self.times == 0:
                    self.times = 3
                    self.code = outCode()
                    self.codeButton.SetLabel(f"{self.code}")
        elif eventId == 11:
            self.code = outCode()
            self.codeButton.SetLabel(f"{self.code}")
        elif eventId == 12:
            self.Hide()
            self.returntoback()
    def returnToBack(self):
        self.Show()


