import os
import random
import sys


def restartProgram():
    python = sys.executable
    os.execl(python, python, *sys.argv)


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