import random 
import time as t

total_que = 5

def generate_eqn(level):
    operators=["+","-","*"]
    operator= random.choice(operators)
    if level=="easy":
        left=random.randint(1,10)
        right=random.randint(1,10)
    if level=="hard":
         left=random.randint(11,19)
         right=random.randint(13,17)

    expression=str(left) +" "+ operator +" "+ str(right) #so we get eqn which canbe calculated by eval()
    answer=eval(expression) #so for eval we cast int to string
    return expression,answer 

your_level=input("select you level easy or hard : ")
wrong=0
start=t.time()
for i in range(total_que):
        exp,ans=generate_eqn(your_level)  #***imp***
        user_ans=input("question " + str(i+1) + ") " +exp +" ") 
        if user_ans==str(ans):
            continue
        wrong+=1
    #as eval() gives int so we need to cast answer given by eval to string

end=t.time()
result_time =round(end-start,4)
score =int(total_que-wrong)
print("it took you ", result_time )

if score==5 and int(result_time)<15 and your_level!="hard":
     print("good spped with accuracy")
if score==5 and int(result_time)>15 and your_level!="hard":
     print("average speed but good accuracy")
if your_level=="hard" and result_time<30 and score>=3:
     print("amazing speed")
else :
     print("work harder mate")
