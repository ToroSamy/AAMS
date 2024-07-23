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





def Save(GlobalPanel):
    StudentListSave(GlobalPanel.studentList)
    AdminListSave(GlobalPanel.adminList)
    TeacherListSave(GlobalPanel.teacherList)



