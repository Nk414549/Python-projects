print ("Welcome to the bank calculator for interest of amount of money in savings account.")
Amount =float(input("Please enter the amount in your acount:"))
#A number is inputed which is going to be processed.
if (1 <= Amount) and  (Amount<=99):
#this section shows that the value inputted falls under the boundery stated above then processing follows next
    print ("Your interest earned will be 0.05% of","£",Amount)
    percent = (Amount*0.05)/100
    print (percent, "is 0.05% of","£",Amount)
#percent is for the processing of the percentage of the value given by the user.
elif (100 <= Amount)  and  (Amount<=149):
    print ("Your interest earned will be 1% of","£", Amount)
    percent = (Amount*1)/100
    print (percent, "is 1% of","£",Amount)
#elif is used to give more options of where the number could fall into.
elif (150 <= Amount)  and  (Amount<=249):
    print ("Your interest earned will be 2% of","£",Amount)
    percent = (Amount*2)/100
    print (percent, "is 2% of","£",Amount)
#elif is used to give more options of where the number could fall into.
elif (250 <= Amount)  and  (Amount<=399):
    print ("Your interest earned will be 3% of","£",Amount)
    percent = (Amount*3)/100
    print (percent, "is 3% of","£",Amount)
#elif is used to give more options of where the number could fall into.
elif (400 <= Amount)  and  (Amount<=499):
    print ("Your interest earned will be 3.5% of","£",Amount)
    percent = (Amount*3.5)/100
    print (percent, "is 3.5% of","£",Amount)
#elif is used to give more options of where the number could fall into.
elif (500 <= Amount)  and  (Amount<=749):
    print ("Your interest earned will be 4% of","£",Amount)
    percent = (Amount*4)/100
    print (percent, "is 4% of","£",Amount)
#elif is used to give more options of where the number could fall into.
elif (750 <= Amount)  and  (Amount<=999):
    print("Your interest earned will be 4.5% of","£",Amount)
    percent = (Amount*4.5)/100
    print (percent, "is 4.5% of","£",Amount)
#elif is used to give more options of where the number could fall into.
elif (1000 <= Amount)  and  (Amount<=99999):
    print ("Your interest earned will be 5% of","£",Amount)
    percent = (Amount*5)/100
    print (percent, "is 5% of","£",Amount)
else:
    print("This number is not in the boundary provided")
#elif is used to give more options of where the number could fall into.
