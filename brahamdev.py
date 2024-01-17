#Write a Python Program to input any character and check whether it is alphabet, digit or special character.
ch = input("Enter your value :")
if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    print("alphabat")
elif(ch>='0' and ch<='9'):
    print("this is digit")
else:
    print("this is special charecter")





