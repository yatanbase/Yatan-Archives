#how to change value in a tuple

tuple=(1,"a",2,3)

tuple=list(tuple)

tuple.append(4)

for i in tuple:
    print(i)