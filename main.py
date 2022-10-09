import random

def orignalForm(letter):
    if(letter== 'g'):
        return 'gun'
    if(letter== 'w'):
        return 'water'
    if(letter== 's'):
        return 'snake'
    

def game(computer,player):
    if(player == 'g' or player == 'w' or player =='s'):
        print("computer chose:"+ " " + orignalForm(computer))
        print("player chose:" + " " + orignalForm(player))
        
    if(computer == 'g' and player =='s'):
        return 'computer wins'
    elif(player == 'g' and computer =='s'):
        return 'player wins'
    elif(computer == 'w' and player =='g'):
        return 'computer wins'
    elif(computer == 'g' and player =='w'):
        return 'player wins'
    elif(computer == 's' and player =='w'):
        return 'computer wins'
    elif(computer == 'w' and player =='s'):
        return 'player wins'
    elif(computer == 'w' and player =='w'):
        return 'tie'
    elif(computer == 'g' and player =='g'):
        return 'tie'
    elif(computer == 's' and player =='s'):
        return 'tie'
    else:
        return 'pick the letter from the start sentence'

   


randomNum = random.randint(1,3)
if randomNum == 1:
    comp= 's'
elif randomNum == 2:
    comp='w'
elif randomNum ==3:
    comp= 'g'
you = input("Player's turn: Snake(s), Water(w) or Gun(g)? : ").strip()

print(game(comp,you))