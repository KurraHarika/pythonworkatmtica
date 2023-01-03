class Student:
    college='MTICA'
    course='MCA'

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
    def displayStudent(self):
        print('Name : '+self.name.title())
        print('Rollno : '+str(self.rollno))
        print('College : '+self.college)
        print('Course : '+self.course)
lstObj=[]       
for i in range(5):
    n=input()
    m=int(input())
    temp='a'+str(i)
    temp=Student(n,m)
    lstObj.append(temp)
for i in lstObj:
    i.displayStudent()
