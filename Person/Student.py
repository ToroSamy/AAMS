from Person.Person import Person


class Student(Person):
    mMyTeacName = 'null'

    def __init__(self, name, mid, password, phonenumber,sex,teaname='null'):
        super().__init__(name, mid, password, phonenumber,sex)
        self.mMyTeacName = teaname
