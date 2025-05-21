#Take 2 numbers as input from the user.Write a program to swap 
#the numbers without using any special python syntax

number1=int(input("Enter first number - "))
number2=int(input("Enter second number - "))
number1,number2 = number2,number1
print("Swapped numbers -",number1,number2,sep=" ")
