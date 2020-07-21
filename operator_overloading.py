class student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        print("id",id(self.m1))
        print("m1",self.m1,"m2",self.m2)

    def __add__(self,other):
        m1=self.m1+ self.m2 
        m2=other.m1 +other.m2
        print("**********************")
        s3=student(m1,m2)
        return s3
        


s1=student(12,10)
s2=student(12,11)
s3=s1+s2
print(s3.m1)
