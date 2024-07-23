import os

from Person.Admin import Admin
from Person.Student import Student
from Person.Teacher import Teacher

SFile = 'StudentList.txt'
AFile = 'AdminList.txt'
TFile = 'TFile/TeacherList.txt'


def StudentListSave(StuList):
    with open(SFile, 'w') as file:
        for obj in StuList:
            file.write(f'{obj.mName},'
                       f'{obj.mId},'
                       f'{obj.mPassWord},'
                       f'{obj.mPhoneNumber},'
                       f'{obj.mMyTeacName},'
                       f'{obj.mSex},'
                       f'{obj.mAge}\n')


def AdminListSave(AdminList):
    with open(AFile, 'w') as file:
        for obj in AdminList:
            file.write(f'{obj.mName},'
                       f'{obj.mId},'
                       f'{obj.mPassWord},'
                       f'{obj.mPhoneNumber},'
                       f'{obj.mSex},'
                       f'{obj.mAge}\n')


def TeacherListSave(TeacherList):
    with open(TFile, 'w') as file:
        for obj in TeacherList:
            file.write(f'{obj.mName},{obj.mId},{obj.mPassWord},{obj.mPhoneNumber},{obj.mCode},{obj.mSex},{obj.mAge}\n')
            stuFilename = 'TFile/TSList/'
            stuFilename += f'{obj.mName}.txt'
            with open(stuFilename, 'w') as sfile:
                for sobj in obj.mOwnStudentList:
                    sfile.write(f'{sobj.mName},'
                                f'{sobj.mId},'
                                f'{sobj.mPassWord},'
                                f'{sobj.mPhoneNumber},'
                                f'{sobj.mMyTeacName},'
                                f'{sobj.mSex},'
                                f'{sobj.mAge}\n')


def initTeacherList(TeacherList):
    os.makedirs('TFile/TSList', exist_ok=True)
    if not os.path.exists(TFile):
        with open(TFile, 'w'):
            pass

    with open(TFile, 'r') as file:
        nameList = []
        for tline in file:
            teacherStrip = tline.strip().split(',')
            name = teacherStrip[0]
            nameList.append(name)
            mid = teacherStrip[1]
            password = teacherStrip[2]
            phone = teacherStrip[3]
            code = teacherStrip[4]
            sex = teacherStrip[5]
            teacher = Teacher(name, mid, password, phone,sex, code)
            TeacherList.append(teacher)

    for i in range(len(nameList)):
        stuFilename = 'TFile/TSList/'
        stuFilename += nameList[i]
        stuFilename += ".txt"
        if not os.path.exists(stuFilename):
            with open(stuFilename, 'w'):
                pass
        with open(stuFilename, 'r') as sfile:
            for sline in sfile:
                steacherStrip = sline.strip().split(',')
                name = steacherStrip[0]
                mid = steacherStrip[1]
                password = steacherStrip[2]
                phone = steacherStrip[3]

                tname = nameList[i]
                sex = steacherStrip[5]
                student = Student(name, mid, password, phone,sex, tname)
                TeacherList[i].mOwnStudentList.append(student)


def Save(GlobalPanel):
    StudentListSave(GlobalPanel.studentList)
    AdminListSave(GlobalPanel.adminList)
    TeacherListSave(GlobalPanel.teacherList)


def initStudentList(StuList):
    if not os.path.exists(SFile):
        with open(SFile, 'w'):
            pass
    with open(SFile, 'r') as file:
        for line in file:
            studentStrip = line.strip().split(',')  # 碎片化一个学生
            student = Student(studentStrip[0], studentStrip[1], studentStrip[2], studentStrip[3],studentStrip[5], studentStrip[4])
            StuList.append(student)


def initAdminList(AdminList):
    if not os.path.exists(AFile):
        with open(AFile, 'w'):
            pass
    with open(AFile, 'r') as file:
        for line in file:
            adminStrip = line.strip().split(',')
            admin = Admin(adminStrip[0], adminStrip[1], adminStrip[2], adminStrip[3], adminStrip[4])
            AdminList.append(admin)


def initList(GlobalPanel):
    initAdminList(GlobalPanel.adminList)
    initStudentList(GlobalPanel.studentList)
    initTeacherList(GlobalPanel.teacherList)
