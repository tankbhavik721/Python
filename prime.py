#find prime number
#a = int(input("Enter your number"))

#flag = 0

#for i in range(2,a):

#    if(a%i==0):
#        flag = 1
#if(flag==1):
#    print("not prime")
#else:
#    print("prime number")
a = int(input("Enter your number"))

for i in range(2,a):

    if(a%i==0):
        print("not prime")
    else:
        print("prime number")
        