'''
Write a function that finds the sum of the n terms of the
following series. Import the factorial function created in
question 3.
1–x2/2!+x4/4!–x6/6!+…xn/n!
'''

# Importing factorial function created previously
from PythonPracQ3 import factorial

# Function to find sum of given series
def sum_series(x, n):
    sum = 0
    for i in range(1, n+1):
        term = ((-1)**(i+1))*(x**(2*i-2)/factorial(2*i-2))
        #-1 to the power i+1 is because i starts from 1 ,every even value in series is subtracted.
        sum += term
    return sum

if __name__ == "__main__":
    n = int(input("Enter n: "))
    x = int(input("Enter x: "))
    sum = sum_series(x, n)
    print("\nSum of {} terms of series for x={}: {}".format(n, x, sum))



