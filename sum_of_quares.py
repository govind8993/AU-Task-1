#Write a program to find the sum of squares of first n natural 
#numbers where n will be provided by the user.

n=5
sum=0
for i in range(1,n+1):
    sum=sum+(i**2)
print("Sum of Squares of first",n,"numbers =",sum,sep=" ")
