class Circle:
    pi=22/7
    def __init__(self,radius):
        self.radius=radius
        
    def calculateArea(self):
        temp=self.pi*self.radius**2
        return temp
    def calculatePerimeter(self):
        temp=2*self.pi*self.radius
        return temp
    
n=int(input())
a=Circle(n)
area=a.calculateArea()
peri=a.calculatePerimeter()
print('Area of circle with radius ',n,'is',area)
print('Perimeter of circle with radius ',n,'is',peri)
