class Number:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        return self.num1/self.num2

n1=int(input())
n2=int(input())
a=Number(n1,n2)
try:
    print(n1,'/',n2,'=',a.div(),sep='')
except ZeroDivisionError as a:
    print(a)
print(n1,'-',n2,'=',a.sub(),sep='')
print(n1,'*',n2,'=',a.mul(),sep='')
print(n1,'+',n2,'=',a.add(),sep='')
