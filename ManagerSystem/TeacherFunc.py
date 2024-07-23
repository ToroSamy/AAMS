import wx

from GlobalFunc.FileManage import Save

from GlobalFunc.Frame import TextFrame, MessageFrame, AbstractFrame
from GlobalFunc.FrameParts import setTextBox
from GlobalFunc.Func import checkUserName, checkUserIdNumber, checkUserPhoneNumber

from Person.Student import Student


class AddMyStudent(AbstractFrame):
    def __init__(self, title, returntoback, aams, loc):
        super().__init__(title, returntoback, aams, loc)

        self.nameValue, name = setTextBox(self.panel, "用户名", '请输入用户名')

        addButton = wx.Button(self.panel, id=1, label="点击添加")

        self.vbox.Add(name, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(addButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.frame.Show()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyName = self.nameValue.GetValue()
            self.addMyStudent(userKeyName)

    def addMyStudent(self, userKeyName):
        messageName, booleanName = checkUserName(userKeyName)
        if not booleanName:
            MessageFrame(f"{messageName}")
            return
        group, loc = self.aams.locNameRepeat(userKeyName, 3)
        if loc == -1:
            MessageFrame(f"该学生不存在!请检查输入!")
            return

        if self.aams.studentList[loc].mMyTeacName != 'null':
            MessageFrame(f"该学生已经有老师了")
            return

        self.aams.studentList[loc].mMyTeacName = self.aams.teacherList[self.loc].mName
        self.aams.teacherList[self.loc].mOwnStudentList.append(self.aams.studentList[loc])
        Save(self.aams)
        MessageFrame(f"添加成功!")


def findMyStudent(aams, name, loc):
    number = len(aams.teacherList[loc].mOwnStudentList)
    for i in range(number):
        if name == aams.teacherList[loc].mOwnStudentList[i].mName:
            return i
    return -1


def showMyAllStudent(aams, loc):
    number = len(aams.teacherList[loc].mOwnStudentList)
    StudentInfo = ''
    for i in range(number):
        StudentInfo += f"姓名:{aams.teacherList[loc].mOwnStudentList[i].mName}   "
        StudentInfo += f"身份证:{aams.teacherList[loc].mOwnStudentList[i].mId}   "
        StudentInfo += f"年龄:{aams.teacherList[loc].mOwnStudentList[i].mAge}   "
        StudentInfo += f"手机号:{aams.teacherList[loc].mOwnStudentList[i].mPhoneNumber}\n"
    TextFrame(StudentInfo)


def showTeacherInfo(aams, loc):
    teacherList = ''
    teacherList += f"姓名:{aams.teacherList[loc].mName}\n"
    teacherList += f"身份证:{aams.teacherList[loc].mId}\n"
    teacherList += f"年龄:{aams.teacherList[loc].mAge}\n"
    teacherList += f"手机号:{aams.teacherList[loc].mPhoneNumber}\n"
    teacherList += f"邀请码:{aams.teacherList[loc].mCode}\n"
    TextFrame(teacherList)


class FindMyStudentButton(AbstractFrame):
    def __init__(self, title,returntoback,aams,loc):
        super().__init__(title,returntoback,aams,loc)

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
                index = findMyStudent(self.aams, userKeyName, self.loc)
                if index == -1:
                    MessageFrame(f"未找到该学生!")
                else:
                    StudentInfo = ''
                    StudentInfo += f"姓名:{self.aams.teacherList[self.loc].mOwnStudentList[index].mName}\n"
                    StudentInfo += f"身份证:{self.aams.teacherList[self.loc].mOwnStudentList[index].mId}\n"
                    StudentInfo += f"年龄:{self.aams.teacherList[self.loc].mOwnStudentList[index].mAge}\n"
                    StudentInfo += f"手机号:{self.aams.teacherList[self.loc].mOwnStudentList[index].mPhoneNumber}\n"
                    TextFrame(StudentInfo)
            else:
                MessageFrame(f"该学生不存在!")


class DelMyStudentButton(AbstractFrame):
    def __init__(self, title,returntoback,aams,loc):
        super().__init__(title,returntoback,aams,loc)

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
                index = findMyStudent(self.aams, userKeyName, self.loc)
                if index == -1:
                    MessageFrame(f"未找到该学生!")
                else:
                    del self.aams.teacherList[self.loc].mOwnStudentList[index]
                    Save(self.aams)
                    MessageFrame(f"删除成功!")
            else:
                MessageFrame(f"该学生不存在!")



class UpdateMyStudentButton(AbstractFrame):
    def __init__(self, title,returntoback,aams,loc):
        super().__init__(title,returntoback,aams,loc)

        self.nameValue,name = setTextBox(self.panel,"用户名","请输入用户名")
        self.idValue,mid = setTextBox(self.panel,"身份证","请输入身份证")
        self.phoneValue,phone = setTextBox(self.panel,"手机号","请输入手机号")
        self.passwordValue1,password1 = setTextBox(self.panel,"输入密码","",1)
        self.passwordValue2,password2 = setTextBox(self.panel,"重复密码","",1)


        updateButton = wx.Button(self.panel, id=1, label="点击修改")


        self.vbox.Add(name, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(mid, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(phone, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(password1, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(password2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(updateButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        self.frame.Show()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyName = self.nameValue.GetValue()
            userKeyId = self.idValue.GetValue()
            userKeyPhone = self.phoneValue.GetValue()
            userKeyPassword1 = self.passwordValue1.GetValue()
            userKeyPassword2 = self.passwordValue2.GetValue()
            self.updateMyStudentButton(userKeyName, userKeyId, userKeyPhone, userKeyPassword1, userKeyPassword2)

    def updateMyStudentButton(self, userKeyName, userKeyId, userKeyPhone, userKeyPassword1, userKeyPassword2):
        messageName, booleanName = checkUserName(userKeyName)
        if not booleanName:
            MessageFrame(f"{messageName}")
            return
        group, loc = self.aams.locNameRepeat(userKeyName, 0)
        if loc == -1:
            MessageFrame(f"该学生不存在! 无法修改!")
            return
        index = findMyStudent(self.aams, userKeyName, self.loc)
        if index == -1:
            MessageFrame(f"未找到该学生! 无法修改!")
            return
        messageId, booleanId = checkUserIdNumber(userKeyId)
        if not booleanId:
            MessageFrame(f"{messageId}")
            return
        messagePhone, booleanPhone = checkUserPhoneNumber(userKeyPhone)
        if not booleanPhone:
            MessageFrame(f"{messagePhone}")
            return
        if not userKeyPassword1 == userKeyPassword2:
            MessageFrame(f"密码不一致,请重新输入!")
            return
        self.aams.studentList[loc] = Student(userKeyName, userKeyId, userKeyPassword1, userKeyPhone)
        self.aams.teacherList[self.loc].mOwnStudentList[index] = self.aams.studentList[loc]
        Save(self.aams)
        MessageFrame(f"修改成功!")
