from Person.Person import Person


class Admin(Person):
    def __init__(self, name, mid, password, phonenumber):
        super().__init__(name, mid, password, phonenumber)
