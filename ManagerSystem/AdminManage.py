import wx

from ManagerSystem.AdminFunc import AdminTeacherPanel, AdminStudentPanel


class AdminManage(wx.Frame):
    def __init__(self, globalpanel, loc: int, returntoback):
        super().__init__(None, title=f"欢迎管理员" + globalpanel.adminList[loc].mName + "进入管理系统!",
                         size=(300, 250), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)

        teacherManaButton = wx.Button(parent=panel, id=1, label="教师管理", pos=(50, 10))
        studentManaButton = wx.Button(parent=panel, id=2, label="学生管理", pos=(50, 10))
        exitLoginButton = wx.Button(parent=panel, id=3, label="退出登录", pos=(50, 10))

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(teacherManaButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(studentManaButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(exitLoginButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.onClick, id=1, id2=3)
        self.gp = globalpanel
        self.lo = loc
        self.returntoback = returntoback
        self.Show()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            self.Hide()
            adminTeacherPanel = AdminTeacherPanel(self.gp, self.lo, self.returnToBack)
            adminTeacherPanel.Show()
        elif eventId == 2:
            self.Hide()
            adminStudentPanel = AdminStudentPanel(self.gp, self.lo, self.returnToBack)
            adminStudentPanel.Show()
        elif eventId == 3:
            self.Hide()
            self.returntoback()

    def returnToBack(self):
        self.Show()


