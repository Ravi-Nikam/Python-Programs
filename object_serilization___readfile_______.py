import pickle
f=open("data.txt","rb")
d=pickle.load(f) #load means tacking the binary data into object
print(d)
f.close()
