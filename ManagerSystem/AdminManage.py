import wx

from GlobalFunc.Frame import AbstractFrame
from ManagerSystem.AdminFunc import AdminTeacherPanel, AdminStudentPanel

class AdminManage(AbstractFrame):
    def __init__(self, title,returntoback,aams,loc):
        super().__init__(title,returntoback,aams,loc)
        teacherManaButton = wx.Button(self.panel, id=1, label="教师管理")
        studentManaButton = wx.Button(self.panel, id=2, label="学生管理")
        self.vbox.Add(teacherManaButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(studentManaButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
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