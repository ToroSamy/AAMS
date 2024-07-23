import random
from FileManage import Save
from Frame.ErrorFrame import ErrorFrame

from Person.Student import Student


def checkUserName(name: str):
    length = len(name)
    if 3 <= length <= 15:
        if name.isdigit():
            return "用户名不能是纯数字!", False
        if not (any(char.isdigit() for char in name) and any(char.isalpha() for char in name)):
            return "用户名必须同时包含英文和数字!", False
        return "用户名格式正确", True
    return "用户名长度应为3~15个字符!", False


def checkUserPhoneNumber(number: str):
    if (not number.isdigit()) or (len(number) != 11):
        return "手机号必须是11位纯数字!", False
    if number[0] == '0':
        return "手机号不能以0开头!", False
    return "格式正确", True


def checkUserIdNumber(mid):
    length = len(mid)
    if length != 18:
        return "身份证必须是18位!", False
    if not mid[0:17].isalnum():
        return "身份证前17位必须是数字!", False
    if not ((mid[17].isdigit()) or (mid[17] == 'x') or (mid[17] == 'X')):
        return "身份证最后一位必须是X、x或数字!", False
    return "格式正确", True


def outCode():
    code = ''
    for i in range(4):
        randomNum = random.randint(1, 25)
        if random.randint(0, 1) == 0:
            randomNum += 65
        else:
            randomNum += 97
        code += chr(randomNum)
    code += str(random.randint(0, 9))
    return code


class GlobalPanel:
    studentList = []
    teacherList = []
    adminList = []

    # 生成验证码
    @classmethod
    def findAdmin(cls, name):
        number = len(cls.adminList)
        for i in range(number):
            if cls.adminList[i].mName == name:
                return 1, i
        return 0, -1

    @classmethod
    def findTeacher(cls, name: str):
        number = len(cls.teacherList)
        for i in range(number):
            if cls.teacherList[i].mName == name:
                return 2, i
        return 0, -1

    @classmethod
    def findStudent(cls, name):
        number = len(cls.studentList)
        for i in range(number):
            if cls.studentList[i].mName == name:
                return 3, i
        return 3, -1

    @classmethod
    def locNameRepeat(cls, name: str, choice: int):
        if choice == 0:
            group, loc = cls.findAdmin(name)
            if group == 0:
                group, loc = cls.findTeacher(name)
            if group == 0:
                return cls.findStudent(name)
            return group, loc

        elif choice == 1:
            return cls.findAdmin(name)

        elif choice == 2:
            return cls.findTeacher(name)
        return cls.findStudent(name)

    @classmethod
    def loginCheckCode(cls, name, code, rightcode):
        if not code == rightcode:
            errorFrame = ErrorFrame(f"验证码输入有误!")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return False, 0, -1
        message, boolean = checkUserName(name)
        if not boolean:
            errorFrame = ErrorFrame(f"{message}")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return False, 0, -1
        group, loc = cls.locNameRepeat(name, 0)
        if loc == -1:
            errorFrame = ErrorFrame(f"该用户不存在请先注册!")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return False, 0, -1
        return True, group, loc

    @classmethod
    def loginSystem(cls, password, group, loc):
        if group == 1:
            if password == cls.adminList[loc].mPassWord:
                return True
        elif group == 2:
            if password == cls.teacherList[loc].mPassWord:
                return True
        elif group == 3:
            if password == cls.studentList[loc].mPassWord:
                return True
        return False

    @classmethod
    def registerUser(cls, name, mid, phone, password1, password2, userkeycode, code):

        messageName, booleanName = checkUserName(name)
        if not booleanName:
            errorFrame = ErrorFrame(f"{messageName}")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return

        group, loc = cls.locNameRepeat(name, 0)
        if loc != -1:
            errorFrame = ErrorFrame(f"该用户已存在 请勿重复注册!")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return

        messageId, booleanId = checkUserIdNumber(mid)
        if not booleanId:
            errorFrame = ErrorFrame(f"{messageId}")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return

        messagePhone, booleanPhone = checkUserPhoneNumber(phone)
        if not booleanPhone:
            errorFrame = ErrorFrame(f"{messagePhone}")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return

        if not password1 == password2:
            errorFrame = ErrorFrame(f"密码不一致,请重新输入!")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return

        if not code == userkeycode:
            errorFrame = ErrorFrame(f"验证码输入有误!")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return

        student = Student(name, mid, password1, phone)
        cls.studentList.append(student)
        Save(cls)
        errorFrame = ErrorFrame(f"注册成功!")
        errorFrame.ShowModal()
        errorFrame.Destroy()


    @classmethod
    def findPassword(cls, name, mid, phone):
        message, boolean = checkUserName(name)
        if not boolean:
            errorFrame = ErrorFrame(f"{message}")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return False, 0, -1
        group, loc = cls.locNameRepeat(name, 0)
        if loc == -1:
            errorFrame = ErrorFrame(f"该用户不存在请先注册!")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return False, 0, -1
        if group == 1:
            flag1 = not (cls.adminList[loc].mPhoneNumber == phone)
            flag2 = not (cls.adminList[loc].mId == mid)
            if flag1 or flag2:
                errorFrame = ErrorFrame(f"身份验证失败!")
                errorFrame.ShowModal()
                errorFrame.Destroy()
                return False, 1, loc
            else:
                return True, 1, loc
        elif group == 2:
            flag1 = not (cls.teacherList[loc].mPhoneNumber == phone)
            flag2 = not (cls.teacherList[loc].mId == mid)
            if flag1 or flag2:
                errorFrame = ErrorFrame(f"身份验证失败!")
                errorFrame.ShowModal()
                errorFrame.Destroy()
                return False, 2, loc
            else:
                return True, 2, loc
        elif group == 3:
            flag1 = not (cls.studentList[loc].mPhoneNumber == phone)
            flag2 = not (cls.studentList[loc].mId == mid)
            if flag1 or flag2:
                errorFrame = ErrorFrame(f"身份验证失败!")
                errorFrame.ShowModal()
                errorFrame.Destroy()
                return False, 3, loc
            else:
                return True, 3, loc

    @classmethod
    def changePassword(cls, password1, password2, group, loc):
        if password1 == password2:
            if group == 1:
                cls.adminList[loc].mPassWord = password1
            if group == 2:
                cls.teacherList[loc].mPassWord = password1
            if group == 3:
                cls.studentList[loc].mPassWord = password1
            Save(cls)
            errorFrame = ErrorFrame(f"修改成功!")
            errorFrame.ShowModal()
            errorFrame.Destroy()
            return True
        errorFrame = ErrorFrame(f"修改失败!密码不一致!")
        errorFrame.ShowModal()
        errorFrame.Destroy()
        return False
