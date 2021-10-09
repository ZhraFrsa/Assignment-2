import random

print('palam_polom_pilish GAME')

userwin = 0
computer1 = 0
computer2 = 0
round = 1
i = 0

while i <= 4:
    c1 = random.randint(1,2)
    c2 = random.randint(1,2)
    print('1: ✋, 2: 🤚')   
    user = int(input('enter your choice = '))
    i += 1

    if(user==1 and c1==2 and c2==2) or (user==2 and c1==1 and c2==1):
        userwin += 1
        print("you win")
        print("round=", round)
    
    elif(user==1 and c1==2 and c2==1) or (user==2 and c1==1 and c2==2):
        computer1 += 1
        print("computer1 win")
        print("round=", round)

    elif(user==2 and c1==2 and c2==1) or (user==1 and c1==1 and c2==2):
        computer2 += 1
        print("computer2 win")
        print("round=", round)

    elif(user == c1 == c2):
        print("no winner")
        print("round=", round)

    round += 1
    
    if(i == 5):
        if(userwin > computer1 and userwin > computer2):
            print(' you are the winner of this game 👑')
            break
        elif(computer1 > userwin and computer1 > computer2):
            print(' computer1 is the winner of this game 👑')
            break
        elif(computer2 > userwin and computer2 > computer1):
            print(' computer2 is the winner of this game 👑')
            break
        elif(userwin==computer1 or userwin==computer2 or computer1==computer2):
            print(' this game is without a winner 🙁')
            break
        break
