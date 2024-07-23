import wx

from GlobalFunc.Frame import MessageFrame, AbstractFrame
from GlobalFunc.FrameParts import setTextBox


from ManagerSystem.AdminManage import AdminManage
from ManagerSystem.StudentManage import StudentManage
from ManagerSystem.TeacherManage import TeacherManage


class LoginFrame(AbstractFrame):
    def __init__(self, title, returntoback, aams):
        super().__init__(title, returntoback, aams)
        self.nameValue, name = setTextBox(self.panel, '用户名', '请输入用户名')
        self.passwordValue1, password1 = setTextBox(self.panel, '输入密码', '', 1)
        self.loginButton = wx.Button(self.panel, id=3, label='点击登录')
        self.vbox.Add(name, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(password1, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.codeBox, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.loginButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.times = 3
        self.frame.Show()
    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 3:
            userKeyName = self.nameValue.GetValue()
            userKeyPassword = self.passwordValue1.GetValue()
            userKeyCode = self.keyCode.GetValue()
            #先检查验证码是否正确 再检查用户名是否符合格式 再检查用户名是否存在 最终返回 是否通过 用户名所在组 以及位置
            ifCodeRight, group, loc = self.aams.loginCheckCode(userKeyName, userKeyCode, self.code)
            if ifCodeRight:
                self.times -= 1
                if not self.aams.loginSystem(userKeyPassword, group, loc):
                    MessageFrame(f"密码错误，您还有 " + str(self.times) + " 次机会!")
                else:
                    self.times = 3
                    if group == 1:
                        self.frame.Hide()
                        frm = AdminManage("欢迎管理员 "+f"{self.aams.adminList[loc].mName} 进入管理系统!",self.returnToBack,self.aams,loc)
                        frm.frame.SetSize(300, 401)
                    elif group == 2:
                        self.frame.Hide()
                        frm = TeacherManage("欢迎教师 "+f"{self.aams.teacherList[loc].mName} 进入管理系统!",self.returnToBack,self.aams,loc)
                        frm.frame.SetSize(300, 501)
                    elif group == 3:
                        self.frame.Hide()
                        frm = StudentManage("欢迎学生 "+f"{self.aams.studentList[loc].mName} 进入管理系统!",self.returnToBack,self.aams,loc)
                        frm.frame.SetSize(300, 401)
                    self.reloadCode(self)
                if self.times == 0:
                    self.times = 3
                    self.reloadCode(self)
