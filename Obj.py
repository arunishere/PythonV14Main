class Person:

    def __init__(self, name, age, role):
        
        self.name = name
        self.age = age
        self.role = role
        
        Person.Company = "DBS"

    def getName(self):

        return self.name

    def getDetails(self):

        return self.name, self.age, self.role
    

    def getCompany():

        return Person.Company


person1 = Person("John", 20, "Student")
person2 = Person("Sean", 23, "Developer")

print(person2.getDetails())

