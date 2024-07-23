import wx

from GlobalFunc.FileManage import Save

from GlobalFunc.Frame import TextFrame, MessageFrame, AbstractFrame
from GlobalFunc.FrameParts import setTextBox, setButtons
from GlobalFunc.Func import checkUserName, checkUserIdNumber, checkUserPhoneNumber
from Person.Student import Student


class UpdateMyInfoButton(AbstractFrame):
    def __init__(self, title,returntoback,aams,loc):
        super().__init__(title,returntoback,aams,loc)
        self.nameValue,name = setTextBox(self.panel,"用户名","请输入用户名")
        self.idValue,mid = setTextBox(self.panel,"身份证","请输入身份证")
        self.phoneValue,phone = setTextBox(self.panel,"手机号","请输入手机号")

        sexDict = {1: "男", 2: "女"}
        sexButton = setButtons(self.panel,sexDict,"性别")
        self.sexButton = sexButton.GetChildren()

        self.passwordValue1,password1 = setTextBox(self.panel,"输入密码","",1)
        self.passwordValue2,password2 = setTextBox(self.panel,"重复密码","",1)
        updateButton = wx.Button(self.panel, id=1, label="点击修改")

        self.vbox.Add(name, proportion=1, flag=wx.CENTER)
        self.vbox.Add(mid, proportion=1, flag=wx.CENTER)
        self.vbox.Add(phone, proportion=1, flag=wx.CENTER)
        self.vbox.Add(sexButton, proportion=1, flag=wx.CENTER)
        self.vbox.Add(password1, proportion=1, flag=wx.CENTER)
        self.vbox.Add(password2, proportion=1, flag=wx.CENTER)
        self.vbox.Add(updateButton, proportion=1, flag=wx.CENTER)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.CENTER)
        self.frame.Show()
    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyName = self.nameValue.GetValue()
            userKeyId = self.idValue.GetValue()
            userKeyPhone = self.phoneValue.GetValue()
            userKeyPassword1 = self.passwordValue1.GetValue()
            userKeyPassword2 = self.passwordValue2.GetValue()
            userChoiceSex = self.sexButton[1].GetWindow().GetValue()
            self.updateMyInfoButton(userKeyName, userKeyId, userKeyPhone, userKeyPassword1, userKeyPassword2, userChoiceSex)
    def updateMyInfoButton(self,name,mid,phone,password1,password2,userChoiceSex):
        messageName, booleanName = checkUserName(name)
        if not booleanName:
            MessageFrame(f"{messageName}")
            return
        group, loc = self.aams.locNameRepeat(name, 0)
        if loc != -1:
            MessageFrame(f"该用户已存在 请勿重复注册!")
            return
        messageId, booleanId = checkUserIdNumber(mid)
        if not booleanId:
            MessageFrame(f"{messageId}")
            return
        messagePhone, booleanPhone = checkUserPhoneNumber(phone)
        if not booleanPhone:
            MessageFrame(f"{messagePhone}")
            return
        if not password1 == password2:
            MessageFrame(f"密码不一致,请重新输入!")
            return

        if userChoiceSex:
            sex = "男"
        else:
            sex = "女"
        tname = self.aams.studentList[loc].mMyTeacName
        self.aams.studentList[loc] = Student(name, mid, password1, phone,sex)
        self.aams.studentList[loc].mMyTeacName = tname
        Save(self.aams)
        MessageFrame(f"修改成功!")

def findTeacherByCode(aams, code):
    number = len(aams.teacherList)
    for i in range(number):
        if aams.teacherList[i].mCode == code:
            return i
    return -1


class SetMyTeacher(AbstractFrame):
    def __init__(self, title,returntoback,aams,loc):
        super().__init__(title,returntoback,aams,loc)
        self.codeValue, code = setTextBox(self.panel, "邀请码", "请输入邀请码")
        addButton = wx.Button(self.panel, id=1, label="点击设置")
        self.vbox.Add(code, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(addButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.vbox.Add(self.returnButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        self.frame.Show()
    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyCode = self.codeValue.GetValue()
            index = findTeacherByCode(self.aams, userKeyCode)
            if not index == -1:
                if self.aams.studentList[self.loc].mMyTeacName != 'null':
                    MessageFrame(f"你已经设置过老师了")
                    return
                self.aams.studentList[self.loc].mMyTeacName = self.aams.teacherList[index].mName
                self.aams.teacherList[index].mOwnStudentList.append(self.aams.studentList[self.loc])
                Save(self.aams)
                MessageFrame(f"设置成功!")
                return
            MessageFrame(f"未匹配到相应的邀请码!")
            return


def showStudentInfoSelf(aams, loc):
    studentList = ''
    studentList += f"姓名:{aams.studentList[loc].mName}\n"
    studentList += f"性别:{aams.studentList[loc].mSex}\n"
    studentList += f"身份证:{aams.studentList[loc].mId}\n"
    studentList += f"年龄:{aams.studentList[loc].mAge}\n"
    studentList += f"手机号:{aams.studentList[loc].mPhoneNumber}\n"
    studentList += f"我的老师:{aams.studentList[loc].mMyTeacName}\n"
    TextFrame(studentList)
