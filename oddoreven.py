import random 
def game():
    userturn = 1
    compturn = 1
    user_score = 0
    comp_score = 0
    print("game")
    print("1.ODD OR 2.EVEN")
    user=int(input('enter 1 for odd 2 for even'))
    choice= 'even' if user == 2 else 'odd'
    print('you choose',choice)
    print('enter the number to toss')
    comp=random.randint(1,6)
    user=int(input())
    print('computer:',comp)
    add = user + comp
    print(add)
    if add % 2 == 0:
        start = 2
    else:
        start = 1

    while True:
        if (start == 1 and user == 1) or (start == 2 and user == 2) :
            if compturn == 0 and user_score > comp_score:
                print('YOU WON')
                break
            elif compturn == 0 and user_score == comp_score:
                print('Tie')
                break
            print('USER ROUND')
            userinput = int(input())
            if userinput < 1 or userinput > 6:
                print('only 1 to 6 are allowed')
                continue
            compinput = random.randint(1,6)
            print('computer:',compinput)
            if userinput == compinput: 
                print('OUT')
                print("Computer round")
                print(f'computer needs {user_score+1} to win')   
                if start == 1:
                    start = 2
                    userturn = 0
                    
                else: 
                    start = 1
                    userturn = 0  
            if userturn == 0:
                continue           
            user_score+=userinput
            print(user_score)
        else:
             if userturn == 0 and comp_score > user_score:
                print('COMPUTER WON')
                break
             elif compturn == 0 and user_score == comp_score:
                print('Tie')
                break
            
             print('COMPUTER ROUND')
           
             userinput=int(input())
             if userinput < 1 or userinput > 6:
                print('only 1 to 6 are allowed')
                continue
             compinput=random.randint(1,6)
             print('computer:',compinput)
            
             if userinput == compinput:
                print('OUT')
                print('User round')
                print(f'You need {comp_score+1} to win')    
                if start == 1:
                    start = 2
                    compturn = 0
                    
                else: 
                    start = 1
                    compturn = 0 
             if compturn == 0:
                
                continue
                    
             comp_score+=compinput
             print(comp_score)
    print('computer score:',comp_score,'user score:',user_score)
               
game()