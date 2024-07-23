import wx

from FileManage import Save
from Frame.ErrorFrame import ErrorFrame, MessageFrame
from GlobalPanel import checkUserName, checkUserIdNumber, checkUserPhoneNumber
from Person.Student import Student


class AddMyStudent(wx.Frame):
    def __init__(self, globalpanel, loc, returntoback):
        super().__init__(None, title=f"欢迎教师" + globalpanel.teacherList[loc].mName + "进入管理系统!",
                         size=(300, 150), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)
        userNameMesaage = wx.StaticText(parent=panel, label="用户名")
        self.userNameTextCtrl = wx.TextCtrl(panel)
        self.userNameTextCtrl.SetValue('请输入用户名')

        addButton = wx.Button(parent=panel, id=1, label="点击添加", pos=(100, 50))
        returnButton = wx.Button(parent=panel, id=2, label="点击返回", pos=(100, 50))

        hboxName = wx.BoxSizer(wx.HORIZONTAL)
        hboxName.Add(userNameMesaage, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxName.Add(self.userNameTextCtrl, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hboxName, proportion=1, flag=wx.CENTER)
        vbox.Add(addButton, proportion=1, flag=wx.CENTER)
        vbox.Add(returnButton, proportion=1, flag=wx.CENTER)
        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.onClick, id=1, id2=3)
        self.gp = globalpanel
        self.lo = loc
        self.returntoback = returntoback
        self.Show()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyName = self.userNameTextCtrl.GetValue()
            self.addMyStudent(userKeyName)
        elif eventId == 2:
            self.Hide()
            self.returntoback()

    def addMyStudent(self, userKeyName):
        messageName, booleanName = checkUserName(userKeyName)
        if not booleanName:
            errorFrame = ErrorFrame(f"{messageName}")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return

        group, loc = self.gp.locNameRepeat(userKeyName, 3)
        if loc == -1:
            errorFrame = ErrorFrame(f"该学生不存在!请检查输入!")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return

        if userKeyName.mMyTeacName != 'null':
            errorFrame = ErrorFrame(f"该学生已经有老师了")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return

        self.gp.studentList[loc].mMyTeacName = self.gp.teacherList[self.lo].mName
        self.gp.teacherList[self.lo].mOwnStudentList.append(self.gp.studentList[loc])
        Save(self.gp)
        errorFrame = ErrorFrame(f"添加成功!")
        errorFrame.ShowModal()
        errorFrame.Destroy()

def findMyStudent(gp,name,loc):
    number = len(gp.teacherList[loc].mOwnStudentList)
    for i in range(number):
        if name == gp.teacherList[loc].mOwnStudentList[i].mName:
            return i
    return -1
def showMyAllStudent(gp,loc):
    number = len(gp.teacherList[loc].mOwnStudentList)
    StudentInfo = ''
    for i in range(number):
        StudentInfo += f"姓名:{gp.teacherList[loc].mOwnStudentList[i].mName}   "
        StudentInfo += f"身份证:{gp.teacherList[loc].mOwnStudentList[i].mId}   "
        StudentInfo += f"年龄:{gp.teacherList[loc].mOwnStudentList[i].mAge}   "
        StudentInfo += f"手机号:{gp.teacherList[loc].mOwnStudentList[i].mPhoneNumber}\n"
    messageFrame = MessageFrame(StudentInfo)
def showTeacherInfo(gp, loc):
    teacherList = ''
    teacherList += f"姓名:{gp.teacherList[loc].mName}\n"
    teacherList += f"身份证:{gp.teacherList[loc].mId}\n"
    teacherList += f"年龄:{gp.teacherList[loc].mAge}\n"
    teacherList += f"手机号:{gp.teacherList[loc].mPhoneNumber}\n"
    teacherList += f"邀请码:{gp.teacherList[loc].mCode}\n"
    messageFrame = MessageFrame(teacherList)


class FindMyStudentButton(wx.Frame):
    def __init__(self, globalpanel, loc, returntoback):
        super().__init__(None, title=f"欢迎教师" + globalpanel.adminList[loc].mName + "进入管理系统!",
                         size=(300, 140), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)
        userNameMesaage = wx.StaticText(parent=panel, label="用户名")
        self.userNameTextCtrl = wx.TextCtrl(panel)
        self.userNameTextCtrl.SetValue('请输入用户名')

        hboxName = wx.BoxSizer(wx.HORIZONTAL)
        hboxName.Add(userNameMesaage, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxName.Add(self.userNameTextCtrl, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        findButton = wx.Button(parent=panel, id=1, label="点击查找", pos=(100, 50))
        returnButton = wx.Button(parent=panel, id=2, label="点击返回", pos=(100, 50))

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hboxName, proportion=1, flag=wx.CENTER)
        vbox.Add(findButton, proportion=1, flag=wx.CENTER)
        vbox.Add(returnButton, proportion=1, flag=wx.CENTER)
        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.onClick, id=1, id2=3)
        self.gp = globalpanel
        self.lo = loc
        self.returntoback = returntoback
        self.Show()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyName = self.userNameTextCtrl.GetValue()
            group, loc = self.gp.locNameRepeat(userKeyName, 3)
            if not loc == -1:
                index = findMyStudent(self.gp, userKeyName,self.lo)
                if index == -1:
                    errorFrame = ErrorFrame(f"未找到该学生!")
                    errorFrame.ShowModal()
                    errorFrame.Destroy()
                else:
                    StudentInfo = ''
                    StudentInfo += f"姓名:{self.gp.teacherList[self.lo].mOwnStudentList[index].mName}\n"
                    StudentInfo += f"身份证:{self.gp.teacherList[self.lo].mOwnStudentList[index].mId}\n"
                    StudentInfo += f"年龄:{self.gp.teacherList[self.lo].mOwnStudentList[index].mAge}\n"
                    StudentInfo += f"手机号:{self.gp.teacherList[self.lo].mOwnStudentList[index].mPhoneNumber}\n"
                    messageFrame = MessageFrame(StudentInfo)
            else:
                errorFrame = ErrorFrame(f"该学生不存在!")
                errorFrame.ShowModal()
                errorFrame.Destroy()
        elif eventId == 2:
            self.Hide()
            self.returntoback()


class DelMyStudentButton(wx.Frame):
    def __init__(self, globalpanel, loc, returntoback):
        super().__init__(None, title=f"欢迎教师" + globalpanel.adminList[loc].mName + "进入管理系统!",
                         size=(300, 140), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)
        userNameMesaage = wx.StaticText(parent=panel, label="用户名")
        self.userNameTextCtrl = wx.TextCtrl(panel)
        self.userNameTextCtrl.SetValue('请输入用户名')

        hboxName = wx.BoxSizer(wx.HORIZONTAL)
        hboxName.Add(userNameMesaage, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxName.Add(self.userNameTextCtrl, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        findButton = wx.Button(parent=panel, id=1, label="点击查找并删除", pos=(100, 50))
        returnButton = wx.Button(parent=panel, id=2, label="点击返回", pos=(100, 50))

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hboxName, proportion=1, flag=wx.CENTER)
        vbox.Add(findButton, proportion=1, flag=wx.CENTER)
        vbox.Add(returnButton, proportion=1, flag=wx.CENTER)
        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.onClick, id=1, id2=3)
        self.gp = globalpanel
        self.lo = loc
        self.returntoback = returntoback
        self.Show()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyName = self.userNameTextCtrl.GetValue()
            group, loc = self.gp.locNameRepeat(userKeyName, 3)
            if not loc == -1:
                index = findMyStudent(self.gp, userKeyName,self.lo)
                if index == -1:
                    errorFrame = ErrorFrame(f"未找到该学生!")
                    errorFrame.ShowModal()
                    errorFrame.Destroy()
                else:
                    del self.gp.teacherList[self.lo].mOwnStudentList[index]
                    Save(self.gp)
                    errorFrame = ErrorFrame(f"删除成功!")
                    errorFrame.ShowModal()
                    errorFrame.Destroy()
            else:
                errorFrame = ErrorFrame(f"该学生不存在!")
                errorFrame.ShowModal()
                errorFrame.Destroy()
        elif eventId == 2:
            self.Hide()
            self.returntoback()

class UpdateMyStudentButton(wx.Frame):
    def __init__(self, globalpanel, loc, returntoback):
        super().__init__(None, title=f"欢迎教师" + globalpanel.teacherList[loc].mName + "进入管理系统!",
                         size=(300, 310), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)
        userNameMesaage = wx.StaticText(parent=panel, label="用户名")
        self.userNameTextCtrl = wx.TextCtrl(panel)
        self.userNameTextCtrl.SetValue('请输入用户名')

        userIdMesaage = wx.StaticText(parent=panel, label="身份证")
        self.userIdTextCtrl = wx.TextCtrl(panel)
        self.userIdTextCtrl.SetValue('请输入身份证')

        userPhoneMesaage = wx.StaticText(parent=panel, label="手机号")
        self.userPhoneTextCtrl = wx.TextCtrl(panel)
        self.userPhoneTextCtrl.SetValue('请输入手机号')

        # 密码
        passwordMessage1 = wx.StaticText(parent=panel, label="输入密码")
        self.passwordTextCtrl1 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)

        passwordMessage2 = wx.StaticText(parent=panel, label="重复密码")
        self.passwordTextCtrl2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)

        addButton = wx.Button(parent=panel, id=1, label="点击修改", pos=(100, 50))
        returnButton = wx.Button(parent=panel, id=2, label="点击返回", pos=(100, 50))

        hboxName = wx.BoxSizer(wx.HORIZONTAL)
        hboxName.Add(userNameMesaage, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxName.Add(self.userNameTextCtrl, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        hboxId = wx.BoxSizer(wx.HORIZONTAL)
        hboxId.Add(userIdMesaage, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxId.Add(self.userIdTextCtrl, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        hboxPhone = wx.BoxSizer(wx.HORIZONTAL)
        hboxPhone.Add(userPhoneMesaage, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxPhone.Add(self.userPhoneTextCtrl, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        hboxPassword1 = wx.BoxSizer(wx.HORIZONTAL)
        hboxPassword1.Add(passwordMessage1, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxPassword1.Add(self.passwordTextCtrl1, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        hboxPassword2 = wx.BoxSizer(wx.HORIZONTAL)
        hboxPassword2.Add(passwordMessage2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxPassword2.Add(self.passwordTextCtrl2, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)

        # 创建垂直方向的盒子布局管理器对象vbox
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(hboxName, proportion=1, flag=wx.CENTER)
        vbox1.Add(hboxId, proportion=1, flag=wx.CENTER)
        vbox1.Add(hboxPhone, proportion=1, flag=wx.CENTER)

        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox2.Add(hboxPassword1, proportion=1, flag=wx.CENTER)
        vbox2.Add(hboxPassword2, proportion=1, flag=wx.CENTER)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(vbox1, proportion=1, flag=wx.CENTER)
        vbox.Add(vbox2, proportion=1, flag=wx.CENTER)
        vbox.Add(addButton, proportion=1, flag=wx.CENTER)
        vbox.Add(returnButton, proportion=1, flag=wx.CENTER)
        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.onClick, id=1, id2=3)
        self.gp = globalpanel
        self.lo = loc
        self.returntoback = returntoback
        self.Show()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyName = self.userNameTextCtrl.GetValue()
            userKeyId = self.userIdTextCtrl.GetValue()
            userKeyPhone = self.userPhoneTextCtrl.GetValue()
            userKeyPassword1 = self.passwordTextCtrl1.GetValue()
            userKeyPassword2 = self.passwordTextCtrl2.GetValue()
            self.updateMyStudentButton(userKeyName, userKeyId, userKeyPhone, userKeyPassword1, userKeyPassword2)
        elif eventId == 2:
            self.Hide()
            self.returntoback()

    def updateMyStudentButton(self, userKeyName, userKeyId, userKeyPhone, userKeyPassword1, userKeyPassword2):
        messageName, booleanName = checkUserName(userKeyName)
        if not booleanName:
            errorFrame = ErrorFrame(f"{messageName}")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return

        group, loc = self.gp.locNameRepeat(userKeyName, 0)
        if loc == -1:
            errorFrame = ErrorFrame(f"该学生不存在! 无法修改!")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return

        index = findMyStudent(self.gp,userKeyName,self.lo)
        if index == -1:
            errorFrame = ErrorFrame(f"未找到该学生! 无法修改!")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return



        messageId, booleanId = checkUserIdNumber(userKeyId)
        if not booleanId:
            errorFrame = ErrorFrame(f"{messageId}")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return

        messagePhone, booleanPhone = checkUserPhoneNumber(userKeyPhone)
        if not booleanPhone:
            errorFrame = ErrorFrame(f"{messagePhone}")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return

        if not userKeyPassword1 == userKeyPassword2:
            errorFrame = ErrorFrame(f"密码不一致,请重新输入!")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return
        self.gp.studentList[loc] = Student(userKeyName, userKeyId, userKeyPassword1, userKeyPhone)

        self.gp.teacherList[self.lo].mOwnStudentList[index] = self.gp.studentList[loc]
        Save(self.gp)
        errorFrame = ErrorFrame(f"修改成功!")
        errorFrame.ShowModal()
        errorFrame.Destroy()


