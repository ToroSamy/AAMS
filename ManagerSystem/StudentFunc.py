import wx

from FileManage import Save
from Frame.ErrorFrame import ErrorFrame, MessageFrame


def findTeacherByCode(gp, code):
    number = len(gp.teacherList)
    for i in range(number):
        if gp.teacherList[i].mCode == code:
            return i
    return -1


class SetMyTeacher(wx.Frame):
    def __init__(self, globalpanel, loc, returntoback):
        super().__init__(None, title=f"欢迎学生" + globalpanel.studentList[loc].mName + "进入管理系统!",
                         size=(300, 150), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))
        panel = wx.Panel(self)
        self.gp = globalpanel
        self.returntoback = returntoback
        self.lo = loc

        userCodeMesaage = wx.StaticText(parent=panel, label="邀请码")
        self.userCodeTextCtrl = wx.TextCtrl(panel)
        self.userCodeTextCtrl.SetValue('请输入您老师的邀请码')

        hboxName = wx.BoxSizer(wx.HORIZONTAL)
        hboxName.Add(userCodeMesaage, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hboxName.Add(self.userCodeTextCtrl, proportion=5, flag=wx.EXPAND | wx.ALL, border=10)


        addButton = wx.Button(parent=panel, id=1, label="点击注册", pos=(100, 50))
        returnButton = wx.Button(parent=panel, id=2, label="点击返回", pos=(100, 50))

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hboxName, proportion=1, flag=wx.CENTER)
        vbox.Add(addButton, proportion=1, flag=wx.CENTER)
        vbox.Add(returnButton, proportion=1, flag=wx.CENTER)
        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.onClick, id=1, id2=3)

    def onClick(self, event):
        eventId = event.GetId()
        if eventId == 1:
            userKeyCode = self.userCodeTextCtrl.GetValue()
            index = findTeacherByCode(self.gp, userKeyCode)
            if not index == -1:
                if self.gp.studentList[self.lo].mMyTeacName != 'null':
                    errorFrame = ErrorFrame(f"你已经设置过老师了")
                    errorFrame.ShowModal()
                    errorFrame.Destroy()
                    return
                self.gp.studentList[self.lo].mMyTeacName = self.gp.teacherList[index].mName
                self.gp.teacherList[index].mOwnStudentList.append(self.gp.studentList[self.lo])

                Save(self.gp)
                errorFrame = ErrorFrame(f"设置成功!")
                errorFrame.ShowModal()
                errorFrame.Destroy()
                return
            errorFrame = ErrorFrame(f"未匹配到相应的邀请码!")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return

        elif eventId == 2:
            self.Hide()
            self.returntoback()

def showStudentInfoSelf(gp,loc):
    studentList = ''
    studentList += f"姓名:{gp.studentList[loc].mName}\n"
    studentList += f"身份证:{gp.studentList[loc].mId}\n"
    studentList += f"年龄:{gp.studentList[loc].mAge}\n"
    studentList += f"手机号:{gp.studentList[loc].mPhoneNumber}\n"
    studentList += f"我的老师:{gp.studentList[loc].mMyTeacName}\n"
    messageFrame = MessageFrame(studentList)