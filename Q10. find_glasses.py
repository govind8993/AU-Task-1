#Given the height, width and breadth of a milk tank, you have to 
#find out how many glasses of milk can be obtained? Assume all the 
#inputs are provided by the user.
#Input: Dimensions of the milk tank H = 20cm, L = 20cm, B = 20cm Dimensions of the glass h = 
#3cm, r = 1cm

H=20
L=20
B=20
h=3
r=1
volume_tank=H*L*B
volume_glass=3.14*(r**2)*h
glasses=int(volume_tank//volume_glass)
print("Glasses of milk =",glasses,"glasses")
