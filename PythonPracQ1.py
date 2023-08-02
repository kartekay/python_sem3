'''
Write a function that takes the lengths of three sides :
side1, side2 & side3 of the triangle as the input from the
user using input function and return the area and perimeter
of the triangle as a tuple. Also, assert that sum of the
length of any two sides is greater than the third side.
'''

import math
def triangle():
    a=int(input("Enter side 1 "))
    b=int(input("Enter side 2 "))
    c=int(input("Enter side 3 "))
    s1=a+b
    s2=b+c
    s3=a+c
    assert s1>c and s2>a and s3>b
    if s1>c and s2>a and s3>b:
        print("To be a triangle sum of length of any two sides is always greater than the third")
  
    perimeter=a+b+c
    s=perimeter/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    tri=(perimeter,area)

    return tri


tup=triangle()
print("Perimeter : {}, units".format(tup[0]))
print("Area: {:.3f} sq. units".format(tup[1]))
