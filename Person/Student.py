from Person.Person import Person


class Student(Person):
    mMyTeacName = 'null'

    def __init__(self, name, mid, password, phonenumber,teaname='null'):
        super().__init__(name, mid, password, phonenumber)
        self.mMyTeacName = teaname
