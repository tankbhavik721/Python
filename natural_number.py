#natural number from 1 to n.
#n = int(input("Enter your number :"))
#for i in range(1,n,1):
#    print(i)
#    i = i + 1

# Write a Python Program to print all natural numbers in reverse (from n to 1). – using while loop
#n = int(input("Enter your number :"))

#i = n

#while i>=1:
#    print(i)
#    i = i - 1

# Write a Python Program to print all alphabets from a to z. – using while loop
#i = 'A'

#while ord(i) <= ord('Z'):
#    print(i)
#    i = chr(ord(i) + 1)

#Write a Python Program to print all even numbers between 1 to 100. – using while loop
#i = 0
#while i <= 100:
#    if i % 2 == 0:
#        print(i)
#    i = i + 1
    
# Write a Python Program to print all odd number between 1 to 100.
#i = 0

#while i<=100:
#    if(i%2!=0):
#        print(i)
#    i = i + 1 

#Write a Python Program to find sum of all natural numbers between 1 to n
#num = int(input("Enter Your number :"))

#i = 1
#total = 0
#while(i<=num):

#    if(i%2!=0):
#        print(i)
#        total = total + i 
#    i = i + 1
    
#print("total" , total)

# Write a Python Program to find sum of all even numbers between 1 to n.
#num = int(input("Enter your number :"))

#i = 0
#total = 1
#while i<=num:

#   if(i%2==0):
#        print(i)
#        total = total + 1
#    i = i + 1
#print("total", total)

# Write a Python Program to find sum of all odd numbers between 1 to n.
#num = int(input("Enter your number :"))

#i = 0
#total = 1
#while i<=num:

#   if(i%2!=0):
#        print(i)
#        total = total + 1
#   i = i + 1
#print("total", total)

# Write a Python Program to print multiplication table of any number.
num = int(input("Enter your number :"))

for i in range(1,11):
    print(num,"*",i,"=",num*i)
