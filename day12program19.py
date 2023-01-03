class Rectangle:
    def __init__(self,length,width):
        assert(length>=0 and width>=0),'Invalid'
        self.length=length
        self.width=width   
    def calculateArea(self):
        temp=self.length*self.width
        return temp
    def calculatePerimeter(self):
        temp=2*(self.length+self.width)
        return temp
    
l=int(input())
w=int(input())
try:
    ob=Rectangle(l,w)
    area=ob.calculateArea()
    peri=ob.calculatePerimeter()
    print('Area of Rectangle is',area)
    print('Perimeter of Rectangle is',peri)
except AssertionError as obj:
    print(obj)
