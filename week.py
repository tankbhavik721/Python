#Write a Python Program to input week number and print week day

weekday = int(input("enter weekday in (1-7) format :"))

if(weekday == 1):
    print("Sonday")
elif (weekday == 2):
    print("Monday")
elif(weekday == 3):
    print("Tuesday")
elif(weekday == 4):
    print("Wednesday")
elif(weekday == 5):
    print("Thursday")
elif(weekday == 6):
    print("Friday")
elif(weekday == 7):
    print("Saturday")
else:
    print("enter weekday is not in (1-7) format, please retry with given format")
