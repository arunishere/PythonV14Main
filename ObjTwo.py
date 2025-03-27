

#Diff between Funtion & Method
#Function inside the classs -- > Methods


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
    

    def setName(self, nameNew):

        self.name = nameNew
        print('Data has been updated.')


person1 = Person("John", 20, "Student")
person2 = Person("Sean", 23, "Developer")
person1.setName("John Den")


print(person2.getName())

