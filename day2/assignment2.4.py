# To find smallest number in the list
l=[2,4,6,9,8,0]
m=l[0]
for i in l:
    if m>=i:
        m=i
    else:
        continue
print("the smallest is ",m)

#To find the second smallest number in the list
l.remove(m)
lst=list(l)
n=l[0]
for i in lst:
    if n>=i:
        n=i
    else:
        continue
print("second smallest is ",n)

#To find greatest element in list
lst1=[1,2,7,4,5,6]
p=lst1[0]
for x in lst1:
    if p<=x:
        p=x
    else:
     continue
print("greatest is ",p)

#To find second  greatest element in list
lst1.remove(p)
lst2=list(lst1)
q=lst2[0]
for x in lst2:
    if q<=x:
        q=x
    else:
     continue
print("second greatest is ",q)





