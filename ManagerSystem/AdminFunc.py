import wx

from GlobalFunc.FileManage import Save
from GlobalFunc.Frame import TextFrame, MessageFrame, AbstractFrame
from GlobalFunc.FrameParts import setTextBox

def showAllTeacherButton(aams):
    number = len(aams.teacherList)
    teacherInfo = ''
    for i in range(number):
        teacherInfo += f"姓名:{aams.teacherList[i].mName}   "
        teacherInfo += f"性别:{aams.teacherList[i].mSex}   "
        teacherInfo += f"身份证:{aams.teacherList[i].mId}   "
        teacherInfo += f"年龄:{aams.teacherList[i].mAge}   "
        teacherInfo += f"手机号:{aams.teacherList[i].mPhoneNumber}   "
        teacherInfo += f"邀请码:{aams.teacherList[i].mCode}\n"
    TextFrame(teacherInfo)


class FindOneTeacherButton(AbstractFrame):
    def __init__(self, title, returntoback, aams, loc):
        super().__init__(title, returntoback, aams, loc)
        self.nameValue, name = setTextBox(self.panel, "用户名", '请输入用户名')
        findButton = wx.Button(self.panel, id=1, label="点击查找")
        self.vbox.Add(name, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(findButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.frame.Show()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyName = self.nameValue.GetValue()
            group, loc = self.aams.locNameRepeat(userKeyName, 2)
            if not loc == -1:
                self.findOneTeacherButton(self.aams, loc)
            else:
                MessageFrame(f"未找到该教师!")

    @classmethod
    def findOneTeacherButton(cls, aams, loc):
        teacherInfo = ''
        teacherInfo += f"姓名:{aams.teacherList[loc].mName}\n"
        teacherInfo += f"身份证:{aams.teacherList[loc].mId}\n"
        teacherInfo += f"年龄:{aams.teacherList[loc].mAge}\n"
        teacherInfo += f"手机号:{aams.teacherList[loc].mPhoneNumber}\n"
        teacherInfo += f"邀请码:{aams.teacherList[loc].mCode}\n"
        TextFrame(teacherInfo)


class DelOneTeacherButton(AbstractFrame):
    def __init__(self, title, returntoback, aams, loc):
        super().__init__(title, returntoback, aams, loc)
        self.nameValue, name = setTextBox(self.panel, "用户名", '请输入用户名')
        findButton = wx.Button(self.panel, id=1, label="点击查找并删除")
        self.vbox.Add(name, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(findButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.frame.Show()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyName = self.nameValue.GetValue()
            group, loc = self.aams.locNameRepeat(userKeyName, 2)
            if not loc == -1:
                del self.aams.teacherList[loc]
                Save(self.aams)
                MessageFrame(f"删除成功!")
            else:
                MessageFrame(f"未找到该教师!")



#----------------------------------------------
#----------------------------------------------
def showAllStudentButton(aams):
    number = len(aams.studentList)
    StudentInfo = ''
    for i in range(number):
        StudentInfo += f"姓名:{aams.studentList[i].mName}   "
        StudentInfo += f"性别:{aams.studentList[i].mSex}   "
        StudentInfo += f"身份证:{aams.studentList[i].mId}   "
        StudentInfo += f"年龄:{aams.studentList[i].mAge}   "
        StudentInfo += f"手机号:{aams.studentList[i].mPhoneNumber}   "
        StudentInfo += f"我的老师:{aams.studentList[i].mMyTeacName}\n"
    TextFrame(StudentInfo)


class FindOneStudentButton(AbstractFrame):
    def __init__(self, title, returntoback, aams, loc):
        super().__init__(title, returntoback, aams, loc)
        self.nameValue, name = setTextBox(self.panel, "用户名", '请输入用户名')
        findButton = wx.Button(self.panel, id=1, label="点击查找")
        self.vbox.Add(name, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(findButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.frame.Show()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyName = self.nameValue.GetValue()
            group, loc = self.aams.locNameRepeat(userKeyName, 3)
            if not loc == -1:
                self.findOneStudentButton(self.aams, loc)
            else:
                MessageFrame(f"未找到该学生!")

    @classmethod
    def findOneStudentButton(cls, aams, loc):
        StudentInfo = ''
        StudentInfo += f"姓名:{aams.studentList[loc].mName}\n"
        StudentInfo += f"身份证:{aams.studentList[loc].mId}\n"
        StudentInfo += f"年龄:{aams.studentList[loc].mAge}\n"
        StudentInfo += f"手机号:{aams.studentList[loc].mPhoneNumber}\n"
        StudentInfo += f"我的老师:{aams.studentList[loc].mMyTeacName}\n"
        TextFrame(StudentInfo)


class DelOneStudentButton(AbstractFrame):
    def __init__(self, title, returntoback, aams, loc):
        super().__init__(title, returntoback, aams, loc)
        self.nameValue, name = setTextBox(self.panel, "用户名", '请输入用户名')
        findButton = wx.Button(self.panel, id=1, label="点击查找并删除")
        self.vbox.Add(name, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(findButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.frame.Show()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyName = self.nameValue.GetValue()
            group, loc = self.aams.locNameRepeat(userKeyName, 3)
            if not loc == -1:
                del self.aams.studentList[loc]
                Save(self.aams)
                MessageFrame(f"删除成功!")
            else:
                MessageFrame(f"未找到该学生!")
