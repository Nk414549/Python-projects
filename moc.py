print("welcome to my calculator for the surface area and volume of a box.")
l=int(input("please enter the length of the box: "))
print("lenght =",l ,"cm")
w=int(input("please enter the width of the box: "))
print("width =",w ,"cm")
h=int(input("please enter the height of the box: "))
print("height  =",h ,"cm")
#section above is requesting input or values from the user.
volume = l*w*h
surface_area = 2*((l*w)+(w*h)+(l*h))
print(volume,"cm²"," is is the volume of the box")

print(surface_area,"cm³", " is the surface area of the box")
#this section is providing output to the user giving a the answer to the input given.