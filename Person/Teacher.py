import os

from GlobalFunc.Frame import TextFrame
from Person.Person import Person
from Person.Student import Student


class Teacher(Person):
    mCode = ''
    mOwnStudentList = []

    def __init__(self, name, mid, password, phonenumber,sex, code):
        super().__init__(name, mid, password, phonenumber,sex)
        self.mCode = code
        self.mOwnStudentList = []
    def showMyInfo(self):
        personList = ''
        personList += f"姓名:{self.mName}\n"
        personList += f"性别:{self.mSex}\n"
        personList += f"身份证:{self.mId}\n"
        personList += f"年龄:{self.mAge}\n"
        personList += f"手机号:{self.mPhoneNumber}\n"
        personList += f"邀请码:{self.mCode}\n"
        TextFrame(personList)


