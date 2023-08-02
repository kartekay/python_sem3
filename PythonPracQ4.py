'''
Write a function that takes a number (>=10) as an input and
return the digits of the number as a set.
'''

def digits(x):
    ar=set()
    while(x!=0):
        t=divmod(x,10)
        x=t[0]
        ar.add(t[1])
    return ar
x=int(input("Enter the number:should be greater than 10 = "))
if x<10:
    print("Number less than 10 ")
    quit()
else:
    print(digits(x))
