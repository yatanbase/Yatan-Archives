import pickle

tuple=[1,2,3,4,5," hi can i write my secret stuff here?"]
pfile=open("sample.txt","wb")
pickle.dump(tuple,pfile)

pfile=open("sample.txt","rb") #if it was r ide wont be able to read those binary encrypted files so rb
newfile= pickle.load(pfile)

print(newfile)