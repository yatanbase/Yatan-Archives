#labda inside another function
#lambda = one line function?
#lambda are anonymous since they can take any amount of argument but one expression

def apendnum(n):
    return lambda a : a*n

double= apendnum(2)
triple= apendnum(3)

print(triple(13))
