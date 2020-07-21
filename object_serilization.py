#object serilization
import pickle
#f=open("data.txt","wb")
#dc={"id":123,"name":"Rv","age":23}
#object to binary
#pickle.dump(dc,f) #dump means converting object data into binary and store it into file
#dec=pickle.dumps(dc). #shows data in binary format 
#print(dec)
#f.close()


class person:
    def __init__(self):
        self.name="Ravikumar"
        self.age=1

    def show(self):
        print("Name:",self.name,"\n","Age:",self.age)

p1=person()
f=open("ob.txt","wb")
pickle.dump(p1,f)
f.close()

print("unpicked")
f=open("ob.txt","rb")
p1=pickle.load(f)
p1.show()




