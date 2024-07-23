import wx

from ManagerSystem.TeacherFunc import AddMyStudent, FindMyStudentButton, DelMyStudentButton, \
    UpdateMyStudentButton, showMyAllStudent, showTeacherInfo


class TeacherManage(wx.Frame):
    def __init__(self, globalpanel, loc: int, returntoback):
        super().__init__(None, title=f"欢迎教师" + globalpanel.teacherList[loc].mName + "进入管理系统!",
                         size=(300, 350), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)

        exitLoginButton = wx.Button(parent=panel, id=1, label="退出登录界面", pos=(50, 10))
        addMyStudentButton = wx.Button(parent=panel, id=2, label="添加单名学生", pos=(50, 10))
        showMyInfoButton = wx.Button(parent=panel, id=3, label="查看我的信息", pos=(50, 10))
        showMyOneStudentButton = wx.Button(parent=panel, id=4, label="查找单名学生", pos=(50, 10))
        delMyStudentButton = wx.Button(parent=panel, id=5, label="删除单名学生", pos=(50, 10))
        updateMyStudentButton = wx.Button(parent=panel, id=6, label="修改单名学生", pos=(50, 10))
        showMyAllStudentButton = wx.Button(parent=panel, id=7, label="查看我的学生", pos=(50, 10))


        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(exitLoginButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(addMyStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(showMyInfoButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(showMyOneStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(delMyStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(updateMyStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(showMyAllStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.onClick, id=1, id2=7)
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
            addMyStudent = AddMyStudent(self.gp, self.lo, self.returnToBack)
            addMyStudent.Show()
        elif eventId == 3:
            showTeacherInfo(self.gp,self.lo)
        elif eventId == 4:
            self.Hide()
            findMyStudentButton = FindMyStudentButton(self.gp, self.lo, self.returnToBack)
            findMyStudentButton.Show()
        elif eventId == 5:
            self.Hide()
            delMyStudentButton = DelMyStudentButton(self.gp, self.lo, self.returnToBack)
            delMyStudentButton.Show()
        elif eventId == 6:
            self.Hide()
            updateMyStudentButton = UpdateMyStudentButton(self.gp, self.lo, self.returnToBack)
            updateMyStudentButton.Show()
        elif eventId == 7:
            showMyAllStudent(self.gp,self.lo)

    def returnToBack(self):
        self.Show()
