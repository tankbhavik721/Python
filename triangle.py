#Write a Python Program to input angles of a triangle and check whether triangle is valid or not.
a = int(input("enter your first number"))
b = int(input("enter your second number"))
c = int(input("enter your third number"))

if(a+b+c == 180):
    print("this is a valid triangle")
else:
    print("this is not a valid triangle")
    