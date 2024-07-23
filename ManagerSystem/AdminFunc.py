import wx

from FileManage import Save
from Frame.ErrorFrame import ErrorFrame, MessageFrame
from GlobalPanel import checkUserName, checkUserIdNumber, checkUserPhoneNumber, outCode
from Person.Teacher import Teacher
from Person.Student import Student


class AdminTeacherPanel(wx.Frame):
    def __init__(self, globalpanel, loc, returntoback):
        super().__init__(None, title=f"欢迎管理员" + globalpanel.adminList[loc].mName + "进入管理系统!",
                         size=(300, 270), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)

        exitAdminTeacherButton = wx.Button(parent=panel, id=1, label="退出教师管理", pos=(50, 10))
        addOneTeacherButton = wx.Button(parent=panel, id=2, label="添加单名教师", pos=(50, 10))
        showAllTeacherButton = wx.Button(parent=panel, id=3, label="查看所有教师", pos=(50, 10))
        findOneTeacherButton = wx.Button(parent=panel, id=4, label="查看单名教师", pos=(50, 10))
        delOneTeacherButton = wx.Button(parent=panel, id=5, label="删除单名教师", pos=(50, 10))

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(exitAdminTeacherButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(addOneTeacherButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(showAllTeacherButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(findOneTeacherButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(delOneTeacherButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.onClick, id=1, id2=5)
        self.gp = globalpanel
        self.loc = loc
        self.returntoback = returntoback

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            self.Hide()
            self.returntoback()
        elif eventId == 2:
            self.Hide()
            addOneTeacher = self.AddOneTeacher(self.gp, self.loc, self.returnToBack)
            addOneTeacher.Show()
        elif eventId == 3:
            self.showAllTeacherButton(self.gp)
        elif eventId == 4:
            self.Hide()
            findOneTeacher = self.FindOneTeacherButton(self.gp, self.loc, self.returnToBack)
            findOneTeacher.Show()
        elif eventId == 5:
            self.Hide()
            delOneTeacherButton = self.DelOneTeacherButton(self.gp, self.loc, self.returnToBack)
            delOneTeacherButton.Show()

    def returnToBack(self):
        self.Show()

    class AddOneTeacher(wx.Frame):
        def __init__(self, globalpanel, loc, returntoback):
            super().__init__(None, title=f"欢迎管理员" + globalpanel.adminList[loc].mName + "进入管理系统!",
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

            addButton = wx.Button(parent=panel, id=1, label="点击添加", pos=(100, 50))
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
                self.addOneTeacher(userKeyName, userKeyId, userKeyPhone, userKeyPassword1, userKeyPassword2)
            elif eventId == 2:
                self.Hide()
                self.returntoback()

        def addOneTeacher(self, userKeyName, userKeyId, userKeyPhone, userKeyPassword1, userKeyPassword2):
            messageName, booleanName = checkUserName(userKeyName)
            if not booleanName:
                errorFrame = ErrorFrame(f"{messageName}")
                errorFrame.ShowModal()
                errorFrame.Destroy()
                return

            group, loc = self.gp.locNameRepeat(userKeyName, 0)
            if loc != -1:
                errorFrame = ErrorFrame(f"该用户已存在 请勿重复注册!")
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

            code = outCode()
            teacher = Teacher(userKeyName, userKeyId, userKeyPassword1, userKeyPhone, code)
            self.gp.teacherList.append(teacher)
            Save(self.gp)
            errorFrame = ErrorFrame(f"添加成功!")
            errorFrame.ShowModal()
            errorFrame.Destroy()

    @classmethod
    def showAllTeacherButton(cls, gp):
        number = len(gp.teacherList)
        teacherInfo = ''
        for i in range(number):
            teacherInfo += f"姓名:{gp.teacherList[i].mName}   "
            teacherInfo += f"身份证:{gp.teacherList[i].mId}   "
            teacherInfo += f"年龄:{gp.teacherList[i].mAge}   "
            teacherInfo += f"手机号:{gp.teacherList[i].mPhoneNumber}   "
            teacherInfo += f"邀请码:{gp.teacherList[i].mCode}\n"
        messageFrame = MessageFrame(teacherInfo)

    class FindOneTeacherButton(wx.Frame):
        def __init__(self, globalpanel, loc, returntoback):
            super().__init__(None, title=f"欢迎管理员" + globalpanel.adminList[loc].mName + "进入管理系统!",
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
                group, loc = self.gp.locNameRepeat(userKeyName, 2)
                if not loc == -1:
                    self.findOneTeacherButton(self.gp, loc)
                else:
                    errorFrame = ErrorFrame(f"未找到该教师!")
                    errorFrame.ShowModal()
                    errorFrame.Destroy()
            elif eventId == 2:
                self.Hide()
                self.returntoback()

        @classmethod
        def findOneTeacherButton(cls, gp, loc):
            teacherInfo = ''
            teacherInfo += f"姓名:{gp.teacherList[loc].mName}\n"
            teacherInfo += f"身份证:{gp.teacherList[loc].mId}\n"
            teacherInfo += f"年龄:{gp.teacherList[loc].mAge}\n"
            teacherInfo += f"手机号:{gp.teacherList[loc].mPhoneNumber}\n"
            teacherInfo += f"邀请码:{gp.teacherList[loc].mCode}\n"
            messageFrame = MessageFrame(teacherInfo)

    class DelOneTeacherButton(wx.Frame):
        def __init__(self, globalpanel, loc, returntoback):
            super().__init__(None, title=f"欢迎管理员" + globalpanel.adminList[loc].mName + "进入管理系统!",
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
                group, loc = self.gp.locNameRepeat(userKeyName, 2)
                if not loc == -1:
                    del self.gp.teacherList[loc]
                    Save(self.gp)
                    errorFrame = ErrorFrame(f"删除成功!")
                    errorFrame.ShowModal()
                    errorFrame.Destroy()
                else:
                    errorFrame = ErrorFrame(f"未找到该教师!")
                    errorFrame.ShowModal()
                    errorFrame.Destroy()
            elif eventId == 2:
                self.Hide()
                self.returntoback()


class AdminStudentPanel(wx.Frame):
    def __init__(self, globalpanel, loc, returntoback):
        super().__init__(None, title=f"欢迎管理员" + globalpanel.adminList[loc].mName + "进入管理系统!",
                         size=(300, 270), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)

        exitAdminStudentButton = wx.Button(parent=panel, id=1, label="退出学生管理", pos=(50, 10))
        addOneStudentButton = wx.Button(parent=panel, id=2, label="添加单名学生", pos=(50, 10))
        shouAllStudentButton = wx.Button(parent=panel, id=3, label="查看所有学生", pos=(50, 10))
        findOneStudentButton = wx.Button(parent=panel, id=4, label="查看单名学生", pos=(50, 10))
        delOneStudentButton = wx.Button(parent=panel, id=5, label="删除单名学生", pos=(50, 10))

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(exitAdminStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(addOneStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(shouAllStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(findOneStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(delOneStudentButton, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.onClick, id=1, id2=5)
        self.gp = globalpanel
        self.loc = loc
        self.returntoback = returntoback

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            self.Hide()
            self.returntoback()
        elif eventId == 2:
            self.Hide()
            addOneStudent = self.AddOneStudent(self.gp, self.loc, self.returnToBack)
            addOneStudent.Show()
        elif eventId == 3:
            self.showAllStudentButton(self.gp)
        elif eventId == 4:
            self.Hide()
            findOneStudent = self.FindOneStudentButton(self.gp, self.loc, self.returnToBack)
            findOneStudent.Show()
        elif eventId == 5:
            self.Hide()
            delOneStudentButton = self.DelOneStudentButton(self.gp, self.loc, self.returnToBack)
            delOneStudentButton.Show()

    def returnToBack(self):
        self.Show()

    class AddOneStudent(wx.Frame):
        def __init__(self, globalpanel, loc, returntoback):
            super().__init__(None, title=f"欢迎管理员" + globalpanel.adminList[loc].mName + "进入管理系统!",
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

            addButton = wx.Button(parent=panel, id=1, label="点击添加", pos=(100, 50))
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
                self.addOneStudent(userKeyName, userKeyId, userKeyPhone, userKeyPassword1, userKeyPassword2)
            elif eventId == 2:
                self.Hide()
                self.returntoback()

        def addOneStudent(self, userKeyName, userKeyId, userKeyPhone, userKeyPassword1, userKeyPassword2):
            messageName, booleanName = checkUserName(userKeyName)
            if not booleanName:
                errorFrame = ErrorFrame(f"{messageName}")
                errorFrame.ShowModal()
                errorFrame.Destroy()
                return

            group, loc = self.gp.locNameRepeat(userKeyName, 0)
            if loc != -1:
                errorFrame = ErrorFrame(f"该用户已存在 请勿重复添加!")
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

            student = Student(userKeyName, userKeyId, userKeyPassword1, userKeyPhone)
            self.gp.studentList.append(student)
            Save(self.gp)
            errorFrame = ErrorFrame(f"添加成功!")
            errorFrame.ShowModal()
            errorFrame.Destroy()

    @classmethod
    def showAllStudentButton(cls, gp):
        number = len(gp.studentList)
        StudentInfo = ''
        for i in range(number):
            StudentInfo += f"姓名:{gp.studentList[i].mName}   "
            StudentInfo += f"身份证:{gp.studentList[i].mId}   "
            StudentInfo += f"年龄:{gp.studentList[i].mAge}   "
            StudentInfo += f"手机号:{gp.studentList[i].mPhoneNumber}   "
            StudentInfo += f"我的老师:{gp.studentList[i].mMyTeacName}\n"
        messageFrame = MessageFrame(StudentInfo)

    class FindOneStudentButton(wx.Frame):
        def __init__(self, globalpanel, loc, returntoback):
            super().__init__(None, title=f"欢迎管理员" + globalpanel.adminList[loc].mName + "进入管理系统!",
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
                    self.findOneStudentButton(self.gp, loc)
                else:
                    errorFrame = ErrorFrame(f"未找到该学生!")
                    errorFrame.ShowModal()
                    errorFrame.Destroy()
            elif eventId == 2:
                self.Hide()
                self.returntoback()

        @classmethod
        def findOneStudentButton(cls, gp, loc):
            StudentInfo = ''
            StudentInfo += f"姓名:{gp.studentList[loc].mName}\n"
            StudentInfo += f"身份证:{gp.studentList[loc].mId}\n"
            StudentInfo += f"年龄:{gp.studentList[loc].mAge}\n"
            StudentInfo += f"手机号:{gp.studentList[loc].mPhoneNumber}\n"
            StudentInfo += f"我的老师:{gp.studentList[loc].mMyTeacName}\n"
            messageFrame = MessageFrame(StudentInfo)

    class DelOneStudentButton(wx.Frame):
        def __init__(self, globalpanel, loc, returntoback):
            super().__init__(None, title=f"欢迎管理员" + globalpanel.adminList[loc].mName + "进入管理系统!",
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
                    del self.gp.studentList[loc]
                    Save(self.gp)
                    errorFrame = ErrorFrame(f"删除成功!")
                    errorFrame.ShowModal()
                    errorFrame.Destroy()
                else:
                    errorFrame = ErrorFrame(f"未找到该学生!")
                    errorFrame.ShowModal()
                    errorFrame.Destroy()
            elif eventId == 2:
                self.Hide()
                self.returntoback()
