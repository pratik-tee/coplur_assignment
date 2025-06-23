import random
user_score=0
comp_score=0
while True:
    
 print("Welcome to Stone Paper Scissors Game!")
 print("Enter your choice:")
 print("1. Stone")
 print("2. Paper")
 print("3. Scissor")
 print("4. Exit")

 choices = ["Stone", "Paper", "Scissor"]

 ch = int(input("Your choice (1/2/3): ")) 
 rm=random.choice(choices)
 print("Random choice is ",rm)
 

 if ch==1:
    if rm=="Paper":
        comp_score+=1
        print("user_score =",user_score)
        print("comp_score =",comp_score)
    elif rm=="Scissor":
        user_score+=1
        print("user_score =",user_score)
        print("comp_score =",comp_score)
    else:
        print("Draw")
 elif ch==2:
     if rm=="Stone":
        user_score+=1
        print("user_score =",user_score)
        print("comp_score =",comp_score)
     elif rm=="Scissor":
        comp_score+=1
        print("user_score =",user_score)
        print("comp_score =",comp_score)
     else:
        print("Draw")
 elif ch==3:
       if rm=="Stone":
        comp_score+=1
        print("user_score =",user_score)
        print("comp_score =",comp_score)
       elif rm=="Paper":
        user_score+=1
        print("user_score =",user_score)
        print("comp_score =",comp_score)
       else:
        print("Draw")
 else:
     print("EXiting")
     u_score=user_score
     c_score=comp_score
     break
if u_score>c_score:
    print("user win")
elif u_score<c_score:
    print("computer wins")
else:
    print("Draw")