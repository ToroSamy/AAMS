import wx

from GlobalFunc.FileManage import Save

from GlobalFunc.Frame import TextFrame, MessageFrame, AbstractFrame
from GlobalFunc.FrameParts import setTextBox


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
    studentList += f"身份证:{aams.studentList[loc].mId}\n"
    studentList += f"年龄:{aams.studentList[loc].mAge}\n"
    studentList += f"手机号:{aams.studentList[loc].mPhoneNumber}\n"
    studentList += f"我的老师:{aams.studentList[loc].mMyTeacName}\n"
    TextFrame(studentList)
