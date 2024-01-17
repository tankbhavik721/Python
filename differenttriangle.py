#Write a Python Program to check whether the triangle is equilateral, isosceles or scalene triangle.
a = int(input("enter your first value"))
b = int(input("enter your second value"))
c = int(input("enter your third value"))
if(a+b+c == 180):
    
    if(a+b>c and b+c>a and c+a>b):
        print("this is equilateral or isosceles triangle")
else:
    print("this is not equilateral, isosceles triangle")