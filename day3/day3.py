'''
d={1:'alice',2:'bob',3:'ani',4:{1:'pratik',2:'tinwal'}}
d[5]='archit'
print(d[3])
print(d[4][1])
print(d)
print(d[5])
print(type(d))
del(d[5])
print(d)
d2=d.copy()
print(d2)
d2.pop(3)               #To delete the particular element
print(d2)
print(d2.items())
print(d2.keys())
d2.clear()

print(d2)
d[7]='ironman'
d2.update(d)            #update is used for inserting multiple values in the list
print(d2)

#Tuple
tup=('aim','dig','duck','kemo')
print(tup)
print(type(tup))
l=len(tup)
print(l)
for x in range(l):
    print(x,tup[x])
print(tup[2])
tum=(99.90,98,97)
print(tum+tup) # To concatenate the tuple data
t3=(tum,tup)
print(t3)
t=('abc')*3
print(t)
del t
#print(t)     generate error because t is deleted

l=['f','g','h']
t=tuple(l)
print(type(t))
print(t)

n=(1,3,4,5,6,2,8,9)
print('Min is ',min(n))
print('Max is ',max(n))
print('Sum is ',sum(n))
print(n.count(3),n.index(4),sep=',')
print(n.index(4))


#Set           unoedered,unindexed,unchangeble, dublicate value does not allowed
s={'banana','apple','pineapple'}
print(s)
s.add('mango')
print(s)
s1={'iphone','mi','sumsung'}
s2=s.union(s1)
print(s2)
s3={1,2,3}
s4=s1|s3
print(s4)

s5=set()
s6=set()
s7=set()
for i in range(5,100,4):
    s5.add(i)
print(s5)
for i in range(5, 100, 5):
     s6.add(i)
print(s6)
s7=s5.intersection(s6)
print(s7)

'''
#Function
def my_fun(name):
    print(name,"pratik tinwal")
my_fun("Hello")

def my_fun2(a=0,b=0):           #  =0 passes the default values in a and b
    print(a+b)
my_fun2(5,6)

def my_fun3(*city):
    print("the last city is ",city[-1])

my_fun3('delhi','bhopal','noida')

def my_fun4(city3,city2,city1):
    print("the last city is ",city1)
my_fun4(city1='mumbai',city2='delhi',city3='jaipur')

f=open("new.txt","w")
f.write("We are humans ")
f.write("That are learning python")
f.close()

f=open("new.txt","r")
for x in f:
    print(x)
f.close()

f=open("new.txt","r")    #alternate way to read file
print(f.read())
f.close()

with open("new.txt") as file:
    data=file.read()
    print(data)

f=open("new1.txt","a")
f.write("/n New line added")
f.close()


