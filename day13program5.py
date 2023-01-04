def printJanuary():
    print("JANUARY")
def printFebruary():
    print("FEBRUARY")
def printMarch():
    print("MARCH")
def printApril():
    print("APRIL")
def printMay():
    print("MAY")
def printJune():
    print("JUNE")
def printJuly():
    print("JULY")
def printAugust():
    print("AUGUST")
def printSeptember():
    print("SEPTEMBER")
def printOctober():
    print("OCTOBER")
def printNovember():
    print("NOVEMBER")
def printDecember():
    print("DECEMBER")    
def choice():
    print("Enter Month number between 1-12")
MonthDict={1:printJanuary,2:printFebruary, 3:printMarch, 4:printApril, 5:printMay, 6:printJune,
         7:printJuly, 8:printAugust, 9:printSeptember, 10:printOctober, 11:printNovember,
         12:printDecember}
choice()
MonthNo=int(input())
if MonthNo>=1 and MonthNo<=12:
    MonthDict[MonthNo]()
else:
    print("INVALID")
