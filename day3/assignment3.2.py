num=int(input("Enter a number"))
number=num
result=0
while num!=0:
    k=num%10
    result=(result*10)+k
    num=num//10
print(result)
    
if number==result:
    print("Number is palindrome")
else:
    print("The number is not palindrome")

