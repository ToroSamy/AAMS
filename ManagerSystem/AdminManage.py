import wx


from GlobalFunc.Frame import AbstractFrame
from ManagerSystem.AdminFunc import AddOneTeacher, DelOneTeacherButton, FindOneTeacherButton, showAllTeacherButton, \
    AddOneStudent, showAllStudentButton, FindOneStudentButton, DelOneStudentButton, AddOneAdmin


class AdminManage(AbstractFrame):
    def __init__(self, title,returntoback,aams,loc):
        super().__init__(title,returntoback,aams,loc)
        teacherManaButton = wx.Button(self.panel, id=1, label="教师管理系统")
        studentManaButton = wx.Button(self.panel, id=2, label="学生管理系统")
        addOneAdminButton = wx.Button(self.panel, id=3, label="添加单名管理")
        updateAdminInfo = wx.Button(self.panel, id=4, label="修改我的信息")
        showMyAdminInfo = wx.Button(self.panel, id=5, label="查看我的信息")

        self.vbox.Add(teacherManaButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(studentManaButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(addOneAdminButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(updateAdminInfo, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(showMyAdminInfo, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.frame.Show()
    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            self.frame.Hide()
            frm = AdminTeacherPanel("教师管理系统",self.returnToBack,self.aams,self.loc)
            frm.frame.SetSize(300, 401)
        elif eventId == 2:
            self.frame.Hide()
            frm = AdminStudentPanel("学生管理系统",self.returnToBack,self.aams,self.loc)
            frm.frame.SetSize(300, 401)
        elif eventId == 3:
            self.frame.Hide()
            frm = AddOneAdmin("添加单名管理",self.returnToBack,self.aams,self.loc)
            frm.frame.SetSize(300, 401)
        elif eventId == 4:
            self.frame.Hide()
            frm = self.aams.adminList[self.loc].UpdateMyInfo("修改我的信息",self.returnToBack,self.aams,self.loc,self.aams.adminList[self.loc])
            frm.frame.SetSize(300, 401)
        elif eventId == 5:
            self.aams.adminList[self.loc].showMyInfo()
class AdminTeacherPanel(AbstractFrame):
    def __init__(self, title,returntoback,aams, loc):
        super().__init__(title,returntoback,aams, loc)
        addOneTeacherButton = wx.Button(self.panel, id=2, label="添加单名教师")
        showAllTeacherButton = wx.Button(self.panel, id=3, label="查看所有教师")
        findOneTeacherButton = wx.Button(self.panel, id=4, label="查看单名教师")
        delOneTeacherButton = wx.Button(self.panel, id=5, label="删除单名教师")
        self.vbox.Add(addOneTeacherButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(showAllTeacherButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(findOneTeacherButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(delOneTeacherButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.frame.Show()


    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            self.frame.Hide()
            self.returntoback()
        elif eventId == 2:
            self.frame.Hide()
            frm = AddOneTeacher("添加单名教师",self.returnToBack,self.aams,self.loc)
            frm.frame.SetSize(300, 401)
        elif eventId == 3:
            showAllTeacherButton(self.aams)
        elif eventId == 4:
            self.frame.Hide()
            frm = FindOneTeacherButton("查看单名教师",self.returnToBack,self.aams,self.loc)
            frm.frame.SetSize(300, 401)
        elif eventId == 5:
            self.frame.Hide()
            frm = DelOneTeacherButton("删除单名教师",self.returnToBack,self.aams,self.loc)
            frm.frame.SetSize(300, 401)

class AdminStudentPanel(AbstractFrame):
    def __init__(self, title,returntoback,aams,loc):
        super().__init__(title,returntoback,aams,loc)
        addOneStudentButton = wx.Button(self.panel, id=2, label="添加单名学生")
        shouAllStudentButton = wx.Button(self.panel, id=3, label="查看所有学生")
        findOneStudentButton = wx.Button(self.panel, id=4, label="查看单名学生")
        delOneStudentButton = wx.Button(self.panel, id=5, label="删除单名学生")
        self.vbox.Add(addOneStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(shouAllStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(findOneStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(delOneStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.frame.Show()
    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            self.frame.Hide()
            self.returntoback()
        elif eventId == 2:
            self.frame.Hide()
            frm = AddOneStudent("添加单名学生",self.returnToBack,self.aams,self.loc)
            frm.frame.SetSize(300, 401)
        elif eventId == 3:
            showAllStudentButton(self.aams)
        elif eventId == 4:
            self.frame.Hide()
            frm = FindOneStudentButton("查看单名学生",self.returnToBack,self.aams,self.loc)
            frm.frame.SetSize(300, 401)
        elif eventId == 5:
            self.frame.Hide()
            frm = DelOneStudentButton("删除单名学生",self.returnToBack,self.aams,self.loc)
            frm.frame.SetSize(300, 401)