#Write a program that will tell the number of dogs and chicken are
#there when the user will provide the value of total heads and legs.

heads=int(input("Enter heads - "))
legs=int(input("Enter  legs - "))
#dogs+chicken=heads
#4*dogs+2*chicken=legs
dogs=legs//2 - heads
chicken=heads - dogs
if(4*dogs + 2*chicken)!=legs or dogs<0 or chicken<0:
    print("NOT POSSIBLE")
else:
    print("no. of dogs - ",dogs)
    print("no. of chicken - ",chicken)
