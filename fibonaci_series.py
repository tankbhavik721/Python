#fibonaci series
a = int(input("Enter your number :"))

t1 = 1
t2 = 2

i = 1

while(i<=a):
    temp = t1 + t2
    print(temp)
    t1 = t2
    t2 = temp
    

    i = i + 1