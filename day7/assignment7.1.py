import re

#To validate the email
email=input("Enter email")

if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
    print("Valid email")
else:
    print("Invalid email")
    
#To validate mobile number
phone=input("Enter phone number")

if re.match(r'^[6-9]\d{9}$',phone):
    print("Valid phone no")
else:
    print("Invalid phone no")
    
#To validate string
string=input("Enter string")

if re.match(r'^[A-Za-z]+$',string):
    print("Valid string")
else:
    print("Invalid string")
    
#To validate alpha numeric string
string=input("Enter alpha numeric string")

if re.match(r'^[A-Za-z0-9]+$',string):
    print("Valid string")
else:
    print("Invalid string")