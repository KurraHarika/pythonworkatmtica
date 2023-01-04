'''spins=[('red','18'),('black','13'),('red','7'),('red','5'),('red','18'),
        ('black','13'),('red','25'),('red','9'),('black','26'),('black','15'),
        ('black','20'),('black','31'),('red','3')]
def countReds(aList):
    count=0
    for color,number in aList:
        if color=='black':
            yield count
            count==0
        else:
            count+=1
    yield count
gaps=[gap for gap in countReds(spins)]
print(gaps)'''



def squares(x=0):
    while x<10:
        x=x+1
        yield x*x
yieldList=[i for i in squares()]
print(yieldList)

yieldedList=list(squares())
print(yieldList)
