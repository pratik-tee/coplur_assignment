name=input("Enter name:")
Class=input("Enter class:")
print("Enter marks on all subjects")
sub1=int(input(""))
sub2=int(input(""))
sub3=int(input(""))
sub4=int(input(""))
sub5=int(input(""))
Total=sub1+sub2+sub3+sub4+sub5
print("Name of student is ",name)
print("Class of student is ",Class)
print(f"Total marks of all subjects is {Total} ")
per=(Total/500)*100
print(f"Percentage is {per}")

