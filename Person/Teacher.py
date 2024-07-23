from Person.Person import Person


class Teacher(Person):
    mCode = ''
    mOwnStudentList = []

    def __init__(self, name, mid, password, phonenumber,sex, code):
        super().__init__(name, mid, password, phonenumber,sex)
        self.mCode = code
        self.mOwnStudentList = []
