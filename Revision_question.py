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
#a = int(input("Enter number :"))  

#flag = 0

#for i in range(2,a):

#    if(a%i==0):
#        flag = 1
#if(flag==1):
#    print(a, "not prime number")
#else:
#    print(a,"prime number")
    
#factorial number

#print all prime number for 1 to n or in range or in interval

#lower = int(input("Enter your starting no :"))
#upper = int(input("Enter your ending no :"))

#for num in range(lower,upper + 1):
#    if num>1:

#        for i in range(2,num):
#            if num%i==0:
#                break
#        else:
#            print(num,"prime number")             
#strong number or not

#hcf 
# frequency 
#a = int(input("Enter your number :"))
#total = 0
#while a>0:
#    b = a%10
#    a = a//10
#    total = total + 1
#print(total)
#
#armstrong number 
#num = int(input("Enter your number"))
#order = len(str(3))
#sum = 0
#tamp = num

#while tamp>0:
#    digit = tamp%10
#    cube = digit ** order
#    sum = sum + cube
#    tamp = tamp//10
    
#if sum==num:
#    print("armstrong number")
#else:
#    print("no armstrong number")
#
#strong number
a = int(input("Enter your number :"))
original = a
sum = 0
while a>0:
    fact = 1
    b= a%10
     
    for i in range(b,0,-1):
        
        fact = fact * i
        i = i + 1
        
    a = a//10
    sum = sum + fact
if sum==original:
    print(sum,"strong number")
else:
    print(sum,"not a strong number")  
    
















