class Person:
    def __init__(self,n,g,a): 
        self.name=n
        self.gender=g
        self.age=a
        
    def talk(self):  
        print("hi I'm" , self.name)
        
    def vote(self):
        if self.age<=18 :
            print("Not eligibe to vote")
        else:
            print("Eligible to vote")
# Below is used in case we give name ,gender,age in the class itself for a single objest to return    
#obj =Person()
#obj.talk()
#obj.vote()

obj1=Person("sam","male",22)
obj2=Person("rami","female",16)
print(obj1.name,obj2.name)
print("********************************")

obj1.talk()
obj1.vote()

print("********************************")


obj2.talk()
obj2.vote()