import wx


from GlobalFunc.Frame import AbstractFrame, TextFrame
from ManagerSystem.TeacherFunc import AddMyStudent, FindMyStudentButton, DelMyStudentButton, \
    UpdateMyStudentButton, showMyAllStudent


class TeacherManage(AbstractFrame):
    def __init__(self, title, returntoback, aams, loc):
        super().__init__(title, returntoback, aams, loc)
        addMyStudentButton = wx.Button(self.panel, id=2, label="添加单名学生")
        showMyInfoButton = wx.Button(self.panel, id=3, label="查看我的信息")
        showMyOneStudentButton = wx.Button(self.panel, id=4, label="查找单名学生")
        delMyStudentButton = wx.Button(self.panel, id=5, label="删除单名学生")
        updateMyStudentButton = wx.Button(self.panel, id=6, label="修改单名学生")
        showMyAllStudentButton = wx.Button(self.panel, id=7, label="查看我的学生")
        updateMyInfoButton = wx.Button(self.panel, id=8, label="修改我的信息")
        self.vbox.Add(addMyStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(showMyInfoButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(showMyOneStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(delMyStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(updateMyStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(showMyAllStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(updateMyInfoButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.frame.Show()
    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 2:
            self.frame.Hide()
            frm = AddMyStudent("添加单名学生",self.returnToBack,self.aams,self.loc)
            frm.frame.SetSize(300, 401)
        elif eventId == 3:
            TextFrame(self.aams.teacherList[self.loc].showMyInfo())
        elif eventId == 4:
            self.frame.Hide()
            frm = FindMyStudentButton("查找单名学生",self.returnToBack,self.aams,self.loc)
            frm.frame.SetSize(300, 401)
        elif eventId == 5:
            self.frame.Hide()
            frm = DelMyStudentButton("删除单名学生",self.returnToBack,self.aams,self.loc)
            frm.frame.SetSize(300, 401)
        elif eventId == 6:
            self.frame.Hide()
            frm = UpdateMyStudentButton("修改单名学生",self.returnToBack,self.aams,self.loc)
            frm.frame.SetSize(300, 401)
        elif eventId == 7:
            showMyAllStudent(self.aams,self.loc)
        elif eventId == 8:
            self.frame.Hide()
            frm = self.aams.teacherList[self.loc].UpdateMyInfo("修改我的信息",self.returnToBack,self.aams,self.loc,self.aams.teacherList[self.loc])
            frm.frame.SetSize(300, 401)