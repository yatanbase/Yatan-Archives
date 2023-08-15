# reduces the amount of code while making sublist basically

l1= ["apple","banana","chilli"]
l2= [x.upper() for x in l1]
l3= [x for x in range (5)]
l4= [x for x in l1 if "a" in x]
l5= [x for x in l1 if x != "banana"]

print(l1)
print(l2)
print(l3)
print(l4)
print(l5)