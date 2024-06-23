#Write a python Program to read a number and display corresponding day using if_elif_else?
a = int(input("Enter number of the day : "))
if a == 1:
    print("Monday")
elif a==2:
    print("Tuesday")
elif a==3:
    print("Wednesday")
elif a==4:
    print("Thursday")
elif a==5:
    print("Friday")
elif a==6:
    print("Saturday")
elif a==7:
    print("Sunday")
else:
    print("Invalid Input")