import wx

from Frame.AddOnePerson import AddOnePerson
from Frame.FindPasswordFrame import FindPasswordFrame
from Frame.LoginFrame import LoginFrame

from GlobalFunc.FileManage import Save

from GlobalFunc.Frame import MessageFrame
from GlobalFunc.Func import checkUserName, checkUserPhoneNumber, checkUserIdNumber, outCode
from GlobalFunc.InitManage import initList
from Person.Admin import Admin

from Person.Student import Student
from Person.Teacher import Teacher


class AcademicAffairsManagementSystemPython:
    studentList = []
    teacherList = []
    adminList = []
    updateLog = ''

    @classmethod
    def findAdmin(cls, name):
        number = len(cls.adminList)
        for i in range(number):
            if cls.adminList[i].mName == name:
                return 1, i
        return 0, -1

    @classmethod
    def findTeacher(cls, name: str):
        number = len(cls.teacherList)
        for i in range(number):
            if cls.teacherList[i].mName == name:
                return 2, i
        return 0, -1

    @classmethod
    def findStudent(cls, name):
        number = len(cls.studentList)
        for i in range(number):
            if cls.studentList[i].mName == name:
                return 3, i
        return 3, -1

    @classmethod
    def locNameRepeat(cls, name: str, choice: int):
        if choice == 0:
            group, loc = cls.findAdmin(name)
            if group == 0:
                group, loc = cls.findTeacher(name)
            if group == 0:
                return cls.findStudent(name)
            return group, loc
        elif choice == 1:
            return cls.findAdmin(name)
        elif choice == 2:
            return cls.findTeacher(name)
        return cls.findStudent(name)

    @classmethod
    def loginCheckCode(cls, name, code, rightcode):
        if not code == rightcode:
            MessageFrame(f"验证码输入有误!")
            return False, 0, -1
        message, boolean = checkUserName(name)
        if not boolean:
            MessageFrame(f"{message}")
            return False, 0, -1
        group, loc = cls.locNameRepeat(name, 0)
        if loc == -1:
            MessageFrame(f"该用户不存在请先注册!")
            return False, 0, -1
        return True, group, loc

    @classmethod
    def loginSystem(cls, password, group, loc):
        if group == 1:
            if password == cls.adminList[loc].mPassWord:
                return True
        elif group == 2:
            if password == cls.teacherList[loc].mPassWord:
                return True
        elif group == 3:
            if password == cls.studentList[loc].mPassWord:
                return True
        return False

    @classmethod
    def addOnePerson(cls, name, mid, phone, password1, password2,ifSex, choice,userkeycode="0", code="0"):
        messageName, booleanName = checkUserName(name)
        if choice == "has":
            if not code == userkeycode:
                MessageFrame(f"验证码输入有误!")
                return
        if not booleanName:
            MessageFrame(f"{messageName}")
            return
        if name == "admin12138":
            MessageFrame(f"用户名与默认管理员用户名一致")
            return
        group, loc = cls.locNameRepeat(name, 0)
        if loc != -1:
            MessageFrame(f"该用户名已被使用!")
            return
        messageId, booleanId = checkUserIdNumber(mid)
        if not booleanId:
            MessageFrame(f"{messageId}")
            return
        messagePhone, booleanPhone = checkUserPhoneNumber(phone)
        if not booleanPhone:
            MessageFrame(f"{messagePhone}")
            return
        if password1 == "":
            MessageFrame(f"密码不能留空!")
            return
        if not password1 == password2:
            MessageFrame(f"密码不一致,请重新输入!")
            return
        if ifSex:
            sex = "男"
        else:
            sex = "女"
        if choice == "1":
            person = Admin(name, mid, password1, phone,sex)
            cls.adminList.append(person)
            MessageFrame(f"添加成功!")
        elif choice == "2":
            person = Teacher(name, mid, password1, phone, sex,outCode())
            cls.teacherList.append(person)
            MessageFrame(f"添加成功!")
        elif choice == "3":
            person = Student(name, mid, password1, phone, sex)
            cls.studentList.append(person)
            MessageFrame(f"添加成功!")
        elif choice == "has":
            person = Student(name, mid, password1, phone, sex)
            cls.studentList.append(person)
            MessageFrame(f"注册成功!")
        Save(cls)
    @classmethod
    def findPassword(cls, name, mid, phone):
        message, boolean = checkUserName(name)
        if not boolean:
            MessageFrame(f"{message}")

            return False, 0, -1
        group, loc = cls.locNameRepeat(name, 0)
        if loc == -1:
            MessageFrame(f"该用户不存在请先注册!")

            return False, 0, -1
        if group == 1:
            flag1 = not (cls.adminList[loc].mPhoneNumber == phone)
            flag2 = not (cls.adminList[loc].mId == mid)
            if flag1 or flag2:
                MessageFrame(f"身份验证失败!")

                return False, 1, loc
            else:
                return True, 1, loc
        elif group == 2:
            flag1 = not (cls.teacherList[loc].mPhoneNumber == phone)
            flag2 = not (cls.teacherList[loc].mId == mid)
            if flag1 or flag2:
                MessageFrame(f"身份验证失败!")
                return False, 2, loc
            else:
                return True, 2, loc
        elif group == 3:
            flag1 = not (cls.studentList[loc].mPhoneNumber == phone)
            flag2 = not (cls.studentList[loc].mId == mid)
            if flag1 or flag2:
                MessageFrame(f"身份验证失败!")
                return False, 3, loc
            else:
                return True, 3, loc

    @classmethod
    def changePassword(cls, password1, password2, group, loc):
        if password1 == password2:
            if group == 1:
                cls.adminList[loc].mPassWord = password1
            if group == 2:
                cls.teacherList[loc].mPassWord = password1
            if group == 3:
                cls.studentList[loc].mPassWord = password1
            Save(cls)
            MessageFrame(f"修改成功!")
            return True
        MessageFrame(f"修改失败!密码不一致!")
        return False


class StartFrame(wx.Frame):
    def __init__(self, aams):
        super().__init__(None, title="开始菜单", size=(300, 250), style=wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER)
        panel = wx.Panel(self)
        self.aams = aams
        loginButton = wx.Button(parent=panel, id=1, label="登录系统")
        registerButton = wx.Button(parent=panel, id=2, label="注册系统")
        findPasswordFrame = wx.Button(parent=panel, id=3, label="找回密码")
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(loginButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(registerButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(findPasswordFrame, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.onClick, id=1, id2=3)
        self.Center()

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            self.Hide()
            frm = LoginFrame('登录界面', self.returnToBack, self.aams)
            frm.frame.SetSize(300, 401)
        elif eventId == 2:
            self.Hide()
            frm = AddOnePerson('注册界面', self.returnToBack, self.aams)
            frm.frame.SetSize(300, 401)
        elif eventId == 3:
            self.Hide()
            frm = FindPasswordFrame('找回密码', self.returnToBack, self.aams)
            frm.frame.SetSize(300, 401)
    def returnToBack(self):
        self.Show()


aams = AcademicAffairsManagementSystemPython()



aams.updateLog += "Version:1.5.1\n"
aams.updateLog += "1.文本框快捷输入\n"

initList(aams)
app = wx.App()
frame = StartFrame(aams)
frame.Show()

app.MainLoop()
