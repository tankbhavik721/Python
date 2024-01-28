#max between number
#a = 10
#b = 3
#c = 200
#d = 20
#if(a>b and a>c and a>d):
##    print(a,"maximum value")
#elif(b>a and b>c and b>d):
#    print(b,"maximum value")
#elif(c>a and c>b and c>d):
#    print(c,"maximum value")
#else:
#    print(d, "maximum number")

#printing reverse counting 
#i = 10
#while i>0:
#    print(i)
#    i = i - 1     
#for i in range(10,0,-1):
#    print(i)           

#prime number or not prime number
a = int(input("Enter number :"))  

flag = 0

for i in range(2,a):

    if(a%i==0):
        flag = 1
if(flag==1):
    print(a, "not prime number")
else:
    print(a,"prime number")
    
#prime or not prime number by loop
   

