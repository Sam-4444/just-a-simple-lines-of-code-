class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.year=1991

    def say_hello(self):
        print(f" Hello {self.name} , you are {self.age} years old !")



class master(person):
    def __init__(self,name,age,job):
        super().__init__(name,age)
        self.job=job
    def say_hello(self):
        print(f" Hello my name is {self.name} and I am a/an {self.job} and I am {self.age} years old ! and I have been born in {a.year}")


a=master("sam",44,"Programmer")
a.say_hello()


myList = [0, 1, 2, 3, 4, 5, 6]
for i in range(len(myList)):
    print(myList[i])

i = 0
while i < len(myList):
    print(myList[i])
    i += 1



class learner :
    def __init__(self,name="Sam !",age=0):
        self.name=name
        self.age=age


a=learner()
print(f"{a.name} and the age is {a.age}" )


