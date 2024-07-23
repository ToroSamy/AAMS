import wx

from GlobalFunc.FileManage import Save

from GlobalFunc.Frame import TextFrame, MessageFrame, AbstractFrame
from GlobalFunc.FrameParts import setTextBox, setButtons
from GlobalFunc.Func import checkUserName, checkUserIdNumber, checkUserPhoneNumber, outCode
from Person.Teacher import Teacher
from Person.Student import Student


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
            frm = self.AddOneTeacher("添加单名教师",self.returntoback,self.aams,"1")
            frm.frame.SetSize(300, 501)
        elif eventId == 3:
            self.showAllTeacherButton(self.aams)
        elif eventId == 4:
            self.frame.Hide()
            self.FindOneTeacherButton("查看单名教师",self.returntoback,self.aams,"1")
        elif eventId == 5:
            self.frame.Hide()
            self.DelOneTeacherButton("删除单名教师",self.returntoback,self.aams,"1")

    class AddOneTeacher(AbstractFrame):
        def __init__(self, title, returntoback, aams,loc):
            super().__init__(title, returntoback, aams,loc)
            self.nameValue, name = setTextBox(self.panel, "用户名", '请输入用户名')
            self.idValue, mid = setTextBox(self.panel, "身份证", '请输入身份证')
            self.phoneValue, phone = setTextBox(self.panel, "手机号", '请输入手机号')

            sexDict = {1: "男", 2: "女"}
            sexButton = setButtons(self.panel, sexDict, "性别")
            self.sexButton = sexButton.GetChildren()

            self.passwordValue1, password1 = setTextBox(self.panel, "输入密码", '', 1)
            self.passwordValue2, password2 = setTextBox(self.panel, "重复密码", '', 1)
            addButton = wx.Button(self.panel, id=1, label="点击添加")

            self.vbox.Add(name, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
            self.vbox.Add(mid, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
            self.vbox.Add(phone, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
            self.vbox.Add(sexButton, proportion=1, flag=wx.CENTER)
            self.vbox.Add(password1, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
            self.vbox.Add(password2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
            self.vbox.Add(addButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
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
                userChoiceSex = self.sexButton[1].GetWindow().GetValue()
                self.addOneTeacher(userKeyName, userKeyId, userKeyPhone,userChoiceSex, userKeyPassword1, userKeyPassword2)
        def addOneTeacher(self, userKeyName, userKeyId, userKeyPhone,userChoiceSex, userKeyPassword1, userKeyPassword2):
            messageName, booleanName = checkUserName(userKeyName)
            if not booleanName:
                MessageFrame(f"{messageName}")
                return
            group, loc = self.aams.locNameRepeat(userKeyName, 0)
            if loc != -1:
                MessageFrame(f"该用户已存在 请勿重复注册!")
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
            if userChoiceSex:
                teacher = Teacher(userKeyName, userKeyId, userKeyPassword1, userKeyPhone, "男", outCode())
            else:
                teacher = Teacher(userKeyName, userKeyId, userKeyPassword1, userKeyPhone, "女", outCode())
            self.aams.teacherList.append(teacher)
            Save(self.aams)
            MessageFrame(f"添加成功!")

    @classmethod
    def showAllTeacherButton(cls, aams):
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
                group, loc = self.aams.locNameRepeat(userKeyName, 2)
                if not loc == -1:
                    del self.aams.teacherList[loc]
                    Save(self.aams)
                    MessageFrame(f"删除成功!")
                else:
                    MessageFrame(f"未找到该教师!")
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
            self.AddOneStudent("添加单名学生",self.returntoback,self.aams,1)
        elif eventId == 3:
            self.showAllStudentButton(self.aams)
        elif eventId == 4:
            self.frame.Hide()
            self.FindOneStudentButton("查看单名学生",self.returntoback,self.aams,self.loc)
        elif eventId == 5:
            self.frame.Hide()
            self.DelOneStudentButton("删除单名学生",self.returntoback,self.aams,1)
    class AddOneStudent(AbstractFrame):
        def __init__(self, title,returntoback,aams,loc):
            super().__init__(title,returntoback,aams,loc)
            self.nameValue, name = setTextBox(self.panel, "用户名", '请输入用户名')
            self.idValue, mid = setTextBox(self.panel, "身份证", '请输入身份证')
            self.phoneValue, phone = setTextBox(self.panel, "手机号", '请输入手机号')

            sexDict = {1: "男", 2: "女"}
            sexButton = setButtons(self.panel, sexDict, "性别")
            self.sexButton = sexButton.GetChildren()

            self.passwordValue1, password1 = setTextBox(self.panel, "输入密码", '',1)
            self.passwordValue2, password2 = setTextBox(self.panel, "重复密码", '',1)
            addButton = wx.Button(self.panel, id=1, label="点击添加")
            self.vbox.Add(name, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
            self.vbox.Add(mid, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
            self.vbox.Add(phone, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

            self.vbox.Add(sexButton, proportion=1, flag=wx.CENTER)

            self.vbox.Add(password1, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
            self.vbox.Add(password2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
            self.vbox.Add(addButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
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
                userChoiceSex = self.sexButton[1].GetWindow().GetValue()
                self.addOneStudent(userKeyName, userKeyId, userKeyPhone, userKeyPassword1, userKeyPassword2,userChoiceSex)
        def addOneStudent(self, userKeyName, userKeyId, userKeyPhone, userKeyPassword1, userKeyPassword2,userChoiceSex):
            messageName, booleanName = checkUserName(userKeyName)
            if not booleanName:
                MessageFrame(f"{messageName}")
                return
            group, loc = self.aams.locNameRepeat(userKeyName, 0)
            if loc != -1:
                MessageFrame(f"该用户已存在 请勿重复添加!")
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
            if userChoiceSex:
                student = Student(userKeyName, userKeyId, userKeyPhone, userKeyPassword1, "男")
            else:
                student = Student(userKeyName, userKeyId, userKeyPhone, userKeyPassword1, "女")
            self.aams.studentList.append(student)
            Save(self.aams)
            MessageFrame(f"添加成功!")

    @classmethod
    def showAllStudentButton(cls, aams):
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
                    del self.aams.studentList[loc]
                    Save(self.aams)
                    MessageFrame(f"删除成功!")
                else:
                    MessageFrame(f"未找到该学生!")