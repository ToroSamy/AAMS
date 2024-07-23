
from GlobalFunc.Frame import TextFrame

from Person.Person import Person


class Student(Person):
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
        return personList
        #TextFrame(personList)
    def updateMyInfo(self,personBasicInfoList):
        self.mName = personBasicInfoList[0]
        self.mId = personBasicInfoList[1]
        self.mPassWord = personBasicInfoList[2]
        self.mPhoneNumber = personBasicInfoList[3]
        self.mSex = personBasicInfoList[4]
        year = personBasicInfoList[1]
        age = 2024 - int(year[6:10])
        if age > 0:
            self.mAge = age
        else:
            self.mAge = 0
