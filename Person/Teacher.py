from Person.Person import Person


class Teacher(Person):
    mCode = ''
    mOwnStudentList = []

    def __init__(self, name, mid, password, phonenumber, code):
        super().__init__(name, mid, password, phonenumber)
        self.mCode = code
        self.mOwnStudentList = []
