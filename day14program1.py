'''
reverse of a string
inp-Mango
oup-ognaM
'''

##def reverseString(s):
##    if s=='Mango Kiwi':
##        return 'iwiK ognaM'
##    if s=='Orange':
##        return 'egnarO'
##    return 'ayapap tunococ'
##inp=input().split()
##print(inp)
##print(reverseString(inp))


def reverseString(a):
    s=[i[::-1] for i in a]
    return s
inp=input().split()
print(*reverseString(inp))
