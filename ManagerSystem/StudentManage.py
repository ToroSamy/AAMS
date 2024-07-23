import wx

from ManagerSystem.StudentFunc import SetMyTeacher, showStudentInfoSelf


class StudentManage(wx.Frame):
    def __init__(self, globalpanel, loc: int, returntoback):
        super().__init__(None, title=f"欢迎学生" + globalpanel.studentList[loc].mName + "进入管理系统!",
                         size=(300, 300), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)

        exitLoginButton = wx.Button(parent=panel, id=1, label="退出登录界面", pos=(50, 10))
        setMyTeacherButton = wx.Button(parent=panel, id=2, label="设置我的老师", pos=(50, 10))
        showMyInfoButton = wx.Button(parent=panel, id=3, label="查看我的信息", pos=(50, 10))



        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(exitLoginButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(setMyTeacherButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(showMyInfoButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)


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
            self.returntoback()
        elif eventId == 2:
            self.Hide()
            setMyTeacher = SetMyTeacher(self.gp, self.lo, self.returnToBack)
            setMyTeacher.Show()
        elif eventId == 3:
            showStudentInfoSelf(self.gp,self.lo)


    def returnToBack(self):
        self.Show()
