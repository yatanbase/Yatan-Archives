f= open("function","r")
print(f.read())

f.close()

f=open("function","w")
f.write("all past text is formatted")
f.close()

f=open("function","r")
print(f.read())
f.close()

f=open("function","a")
f.write("appended line")
f.close()

f=open("function","r")
print(f.read())
f.close()