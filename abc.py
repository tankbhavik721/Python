#Write a Python Program to check whether a number is negative, positive or zero.

a = int(input("Enter your number"))
if(a==0):
    print("this is a zero number")
elif(a>=1):
    print("this is a positive number")
elif(a<-1):
    print("this is a negative number")