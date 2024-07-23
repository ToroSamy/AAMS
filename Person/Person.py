import wx

from GlobalFunc.FileManage import Save
from GlobalFunc.Frame import AbstractFrame, MessageFrame
from GlobalFunc.FrameParts import setTextBox, setButtons
from GlobalFunc.Func import checkUserName, checkUserIdNumber, checkUserPhoneNumber





class Person:
    def __init__(self, name, mid, password, phonenumber,sex):
        self.mName = name
        self.mId = mid
        self.mPassWord = password
        self.mPhoneNumber = phonenumber
        self.mSex = sex
        self.mUpdataInfo = self.UpdateMyInfo
        age = 2024 - int(mid[6:10])
        if age > 0:
            self.mAge = age
        else:
            self.mAge = 0
    def updateMyInfo(self,person):
        pass
    def showMyInfo(self):
        pass

    class UpdateMyInfo(AbstractFrame):
        def __init__(self, title, returntoback, aams, loc,personInstance):
            super().__init__(title, returntoback, aams, loc)
            self.nameValue, name = setTextBox(self.panel, "用户名", "请输入用户名")
            self.idValue, mid = setTextBox(self.panel, "身份证", "请输入身份证")
            self.phoneValue, phone = setTextBox(self.panel, "手机号", "请输入手机号")

            sexDict = {1: "男", 2: "女"}
            sexButton = setButtons(self.panel, sexDict, "性别")
            self.sexButton = sexButton.GetChildren()

            self.passwordValue1, password1 = setTextBox(self.panel, "输入密码", "", 1)
            self.passwordValue2, password2 = setTextBox(self.panel, "重复密码", "", 1)
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
            self.personInstance = personInstance
        def onClick(self, event):
            eventId = event.GetId()
            if eventId == 1:
                userKeyName = self.nameValue.GetValue()
                userKeyId = self.idValue.GetValue()
                userKeyPhone = self.phoneValue.GetValue()
                userKeyPassword1 = self.passwordValue1.GetValue()
                userKeyPassword2 = self.passwordValue2.GetValue()
                userChoiceSex = self.sexButton[1].GetWindow().GetValue()
                person = self.returnPerson(userKeyName, userKeyId, userKeyPhone, userKeyPassword1,
                                                             userKeyPassword2,
                                                             userChoiceSex)
                self.personInstance.updateMyInfo(person)
                Save(self.aams)
                MessageFrame(f"修改成功!")


        def returnPerson(self, name, mid, phone, password1, password2, userChoiceSex):
            messageName, booleanName = checkUserName(name)
            if not booleanName:
                MessageFrame(f"{messageName}")
                return
            group, loc = self.aams.locNameRepeat(name, 0)
            if name == "admin12138":
                MessageFrame(f"用户名与默认管理员用户名一致")
                return
            if loc != -1:
                MessageFrame(f"该用户已存在 请勿重复修改!")
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

            return Person(name, mid, password1, phone, sex)



