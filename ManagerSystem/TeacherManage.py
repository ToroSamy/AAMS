import wx

from GlobalFunc.Frame import AbstractFrame
from ManagerSystem.TeacherFunc import AddMyStudent, FindMyStudentButton, DelMyStudentButton, \
    UpdateMyStudentButton, showMyAllStudent, showTeacherInfo


class TeacherManage(AbstractFrame):
    def __init__(self, title, returntoback, aams, loc):
        super().__init__(title, returntoback, aams, loc)
        addMyStudentButton = wx.Button(self.panel, id=2, label="添加单名学生")
        showMyInfoButton = wx.Button(self.panel, id=3, label="查看我的信息")
        showMyOneStudentButton = wx.Button(self.panel, id=4, label="查找单名学生")
        delMyStudentButton = wx.Button(self.panel, id=5, label="删除单名学生")
        updateMyStudentButton = wx.Button(self.panel, id=6, label="修改单名学生")
        showMyAllStudentButton = wx.Button(self.panel, id=7, label="查看我的学生")
        self.vbox.Add(addMyStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(showMyInfoButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(showMyOneStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(delMyStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(updateMyStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(showMyAllStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.frame.Show()
    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 2:
            self.frame.Hide()
            AddMyStudent("添加单名学生",self.returnToBack,self.aams,self.loc)
        elif eventId == 3:
            showTeacherInfo(self.aams,self.loc)
        elif eventId == 4:
            self.frame.Hide()
            FindMyStudentButton("查找单名学生",self.returnToBack,self.aams,self.loc)
        elif eventId == 5:
            self.frame.Hide()
            DelMyStudentButton("删除单名学生",self.returnToBack,self.aams,self.loc)
        elif eventId == 6:
            self.frame.Hide()
            UpdateMyStudentButton("修改单名学生",self.returnToBack,self.aams,self.loc)
        elif eventId == 7:
            showMyAllStudent(self.aams,self.loc)
