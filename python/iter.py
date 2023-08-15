# list, tuple, dict are itterable

list= [1,2,3,4,5]
iter_obj = iter(list)

print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

#we can define these in class
class sample():
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        x=self.a
        self.a += 1
        return x

obj= sample()

iterr= iter(obj)

print(next(iterr))
print(next(iterr))
print(next(iterr))
