#Given 2 fractions, find the sum of those 2 fractions.Take the 
#numerator and denominator values of the fractions from the user.

import math
n1=int(input("Enter 1st numerator - "))
n2=int(input("Enter 2st numerator - "))
d1=int(input("Enter 1st denominator - "))
d2=int(input("Enter 2st denominator - "))
lcm=math.lcm(d1,d2)
n1=int(n1*(lcm/d1))
n2=int(n2*(lcm/d2))
print("Sum of the fraction = ",n1+n2,"/",lcm)
