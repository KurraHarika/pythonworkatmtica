def printSunday():
    print("SUNDAY")
def printMonday():
    print("MONDAY")
def printTuesday():
    print("TUESDAY")
def printWednesday():
    print("WEDNESDAY")
def printThursday():
    print("THURSDAY")
def printFriday():
    print("FRIDAY")
def printSaturday():
    print("SATURDAY")
def choice():
    print("Enter day number between 1-7")
    #print("0:Sunday")
    #print("1:Monday")
    #print("2:Tuesday")
    #print("3:Wednesday")
    #print("4:Thursday")
    #print("5:Friday")
    #print("6:Saturday")
    #print("7:Quit")
    #return
#dayNum={0:printSunday,1:printMonday, 2:printTuesday, 3:printWednesday, 4:printThursday, 5:printFriday, 6:printSaturday }
dayDict={1:printSunday,2:printMonday, 3:printTuesday, 4:printWednesday, 5:printThursday, 6:printFriday, 7:printSaturday }
#selection=0
#while True:
    #if selection == 7:break
    #choice()
    #selection=int(input("select a day option:"))
    #if(selection>=0) and (selection<7):
      # dayNum[selection]()
    #else:
       # print("INVALID")
choice()
dayNo=int(input())
if dayNo>+1 and dayNo<=7:
    dayDict[dayNo]()
else:
    print("INVALID")
