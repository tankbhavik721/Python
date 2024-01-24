#prime number or not
a = int(input("Enter your number :"))
flag = 0
for i in range(2,a):
    
    if(a%i==0):
        flag = 1
if flag==0:
    print("prime number")
else:
    print("Not prime number")

