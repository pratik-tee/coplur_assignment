a=24
b=20
result=a//b
print("division is ",result)
print("addition is",a+b)
print(f"addition is {a+b}")
print(f"subtraction is {a-b}")
print(f"multiplication is {a*b}")
print(f"division is {a/b}")

print(f"..",a+b*a/b)
print(f"modulus is {b%a}")
a+=3
print(a)
print(f"result is {a}")

c=10
d=8
print(bin(c))
print(bin(d))
print(c & d)
'''
n=int(input("enter n"))
if n%2==0:
    print("even")
    print("both are on equal space")
else:
    print("odd")


 
 per=int(input("Enter percentage:"))
if per>90:
    print("Grade A")
elif per>70 and per<90:
    print("Grade B")
else:
    print("Grade C")


n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
opr=input("Enter operation:")
if opr=="+":
    print(f"addition is {n1+n2}")
elif opr=="-":
    print(f"subtraction is {n1 - n2}")
elif opr=="*":
    print(f"multiplication is {n1 * n2}")
elif opr=="/":
    print(f"division is {n1 / n2}")
else:
    print("wrong choice")


print("true")  if(10>5) else print("false")   #one line if else condition
i=2
print(f"{i} is even") if i%2==0 else print(f"{i} is even")
if(10>5):  print("True")   #it is also one line if else

#loops

for x in range(10,1,-2):
    print(x)

n=int(input("Enter number:"))
for x in range(1,11,2):

    print(n,"*",x,"=",n*x)


#nested for  loop
for x in range(2,5):
    print(f"table of {x} is ")
    for y in range(1,11):
        print(x,"*",y,"=",x*y)

for x in range(1,10):
    for y in range(1,x+1):
        print(y,end=" ")
    print()



#while loop

i=1
while i<=10:
    print(i)
    i+=1


while True:
    n=int(input("enter any number and 0 exit:"))
    if n==0:
        break
    else:
     print(n)
'''
str="pratik tinwal"
print(str[2:5:2])
l=len(str)
print(l)
for x in range(l):
     print(str[x],end=" ")

print(ord("z"))
print(chr(121))


list=[2,4,5,5,7,"A",[9,0]]
list[0]=10         #these are mutable (these can be change )
list.append("B")
list.insert(2,50)
list.extend([99,98,97])
list.remove(99)                         #it remove all the element of given number like here 99 removes at all places
list.pop(1)                              # it removes element at particukar indexes
print(list)

print(len(list))
print(list[6][0])   #list in list (nested list)

print(list[-1::-1])
list.reverse()
print(list)


lst=[1,2,7,4,5,6]
m=lst[0]
for x in lst:
    if m<=x:
        m=x
    else:
     continue
print(m)





