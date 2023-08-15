class zero: #class can't be empty
    pass
class first:
    def __init__(self,name,age): #initializing function
        self.name=name
        self.age=age

    def sayhello(self):
        print("Top of the mornin to ya!"+self.name)

o1=first("yatan",20)
o1.sayhello()

del(o1) #delete object
