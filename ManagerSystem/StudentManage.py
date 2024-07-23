import wx


from GlobalFunc.Frame import AbstractFrame, TextFrame
from ManagerSystem.StudentFunc import SetMyTeacher


class StudentManage(AbstractFrame):
    def __init__(self, title,returntoback,aams,loc):
        super().__init__(title,returntoback,aams,loc)

        setMyTeacherButton = wx.Button(self.panel, id=2, label="设置我的老师")
        showMyInfoButton = wx.Button(self.panel, id=3, label="查看我的信息")
        updateMyInfoButton = wx.Button(self.panel, id=4, label="修改我的信息")

        self.vbox.Add(setMyTeacherButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(showMyInfoButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(updateMyInfoButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.frame.Show()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 2:
            self.frame.Hide()
            frm = SetMyTeacher("设置我的老师",self.returnToBack,self.aams,self.loc)
            frm.frame.SetSize(300, 401)
        elif eventId == 3:
            TextFrame(self.aams.studentList[self.loc].showMyInfo())
        elif eventId == 4:
            self.frame.Hide()
            frm = self.aams.studentList[self.loc].UpdateMyInfo("修改我的信息",self.returnToBack,self.aams,self.loc,self.aams.studentList[self.loc])
            frm.frame.SetSize(300, 401)