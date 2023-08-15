def prime(x):
 if x== 0 or x==1 :
   if x==0:
       print("prime since zero")
   else:
       print("prime since one")
 else:
  for i in range(2,x):
   if ((x%i)==0):
    print("non prime")
    break
   elif  i==x-1 :
    print("prime")
    break



   else:
      continue

x=int(input("enter a number"))
prime(x)