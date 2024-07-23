class Person:


    def __init__(self, name, mid, password, phonenumber,sex):
        self.mName = name
        self.mId = mid
        self.mPassWord = password
        self.mPhoneNumber = phonenumber
        self.mSex = sex
        age = 2024 - int(mid[6:10])
        if age > 0:
            self.mAge = age
        else:
            self.mAge = 0

