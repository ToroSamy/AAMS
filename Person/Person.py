class Person:


    def __init__(self, name, mid:str, password, phonenumber):
        self.mName = name
        self.mId = mid
        self.mPassWord = password
        self.mPhoneNumber = phonenumber
        age = 2024 - int(mid[6:10])
        if age > 0:
            self.mAge = age
        else:
            self.mAge = 0

