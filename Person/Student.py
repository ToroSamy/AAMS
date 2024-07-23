
from GlobalFunc.Frame import TextFrame

from Person.Person import Person


class Student(Person):
    mMyTeacName = 'null'

    def __init__(self, name, mid, password, phonenumber,sex,teaname='null'):
        super().__init__(name, mid, password, phonenumber,sex)
        self.mMyTeacName = teaname

    def showMyInfo(self):
        personList = ''
        personList += f"姓名:{self.mName}\n"
        personList += f"性别:{self.mSex}\n"
        personList += f"身份证:{self.mId}\n"
        personList += f"年龄:{self.mAge}\n"
        personList += f"手机号:{self.mPhoneNumber}\n"
        personList += f"我的老师:{self.mMyTeacName}\n"
        TextFrame(personList)
    def updateMyInfo(self,person):
        self.mName = person.mName
        self.mName = person.name
        self.mId = person.mid
        self.mPassWord = person.password
        self.mPhoneNumber = person.phonenumber
        self.mSex = person.sex
        age = 2024 - int(person.mid[6:10])
        if age > 0:
            self.mAge = age
        else:
            self.mAge = 0
