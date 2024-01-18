#a = int(input("Enter :"))

#for i in range(0,a):

#    for j in range(0,a):

#        if(i==0 or i==a-1 or j+i==a):

#            print("*", end="")
#        else:
#            print(end=" ")
#    print("\n")


#********
#*      *
#*      *
#********
#*
#*
#*
#a = int(input("Enter :"))

#for i in range(0,a):

#    for j in range(0,a):

#        if(j==0 or i==0 or i==a-5 or j==a-1 or):

#            print("*",end="")
#        else:
#            print(end=" ")
#    print("\n")

a = int(input("Enter : "))

for i in range(0,a):
    
    for j in range(0,a):
        
        if(i==0 or j==a/2):
         print("*",end="")
        else:
            print(end=" ")
        
    print(end="\n")            