#Write a Python Program to input all sides of a triangle and check whether triangle is valid or not.
a = int(input("enter your first value"))
b = int(input("enter your second value"))
c = int(input("enter your third value "))
if( a+b>c and b+c>a and c+a>b):
    print("this is a valid trinagle")
else:
    print("this is not a valid triangle")
