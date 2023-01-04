#Reading a file with an alternate format
with open(r'D:\PythonPractice17\Day9\122.txt') as fo:
    temp=fo.read()
    print(temp)


fo=open(r'D:\PythonPractice17\Day9\122.txt')
temp=fo.read()
print(temp)
fo.close()
