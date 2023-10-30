class Person:
    def __init__(self,name,idnumber):
        self.name= name
        self.idnumber=idnumber
    
    def display(self):
        print(self.name)
        print(self.idnumber)
        
    def details(self):
        print("name {}".format(self.name))
        print("id {}".format(self.idnumber))
        
class Employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        
        Person.__init__(self,name,idnumber)
    def details(self):
        print("name : {}".format(self.name))
        print("id : {}".format(self.idnumber))
        print("post :{}".format(self.post))
        
a=Employee('ram',234423,23424,"intern")

a.display()
a.details()