# WAP for Snake and Ladder

print('\n*** Welcome To Snake and Ladder Game ***')

import random 

ladder = {3:21, 8:45, 16:27, 35:65, 48:71, 59:82, 76:95, 85:99}
snake = {24:5, 43:22, 60:42, 56:25, 69:49, 90:72, 86:53, 94:73, 98:58}

position1 = 0
position2 = 0

def movement(position):
    dice = random.randint(1,6)
    print(f'\nDice : {dice}')
    position = position + dice
    
    if position in snake:
        print("\nYou got Bitten by the Snake")
        position = snake[position]
        print(f'position : {position}')
        
    elif position in ladder:
        print("\nYou climbed the Ladder")
        position = ladder[position]
        print(f'position : {position}')
        
    else:
        print(f'position : {position}')
    
    return position

while True:
    
    player_1 = input("\nPlayer 1 - Enter 'a' to throw Dice : ").lower()
    
    if player_1 != 'a':
        continue

    position1 = movement(position1)
    
    if position1 >= 100:
        print('Congratulations Player 1, You Won')
        break
    
    player_2 = input("\nPlayer 2 - Enter 'b' to throw Dice : ").lower()
    
    if player_2 != 'b':
        continue
    
    position2 = movement(position2)
    
    if position2 >= 100:
        print('Congratulations Player 2, You Won')
        break