# custom made iterator
class addsix:
    def __init__(self,max=0):
        self.max=max
    def __iter__(self): #overiding iter
        self.n=0
        return self
    def __next__(self): 
        if self.n <=self.max:
            result = self.n+6  # start with =0 but print from 6 .... 
            self.n+=1
            return result
        else:
            raise StopIteration

numbers =addsix(9)
i=iter(numbers)
print(next(i))