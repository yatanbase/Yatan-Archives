list= ["one ","two ", "three "]

def loop(x):
    print(x*3)

def inst(fpara,list):
    for i in list:
        fpara(i)

inst(loop,list)