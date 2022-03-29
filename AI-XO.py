#Author: Mohamed Hany Saad
#Last modified: 29/03/2022 02:32
#Tic-Tac-Toe game vs AI computer

import random
import time

layout ='''
 ___________
| 1 | 2 | 3 |
|___|___|___|
| 4 | 5 | 6 | 
|___|___|___|
| 7 | 8 | 9 |
|___|___|___|'''    #Initializing game board

check_list = [0,1,2,3,4,5,6,7,8,9]  #List to check if their are three contiguous signs in any pattern

print(layout)

def update_state(player,char):  #Function to update the game board by the played sign in the chosen square
    for i in range(10):
        print("\n")
    global layout
    global check_list
    if player == "first":
        sign = "X"
    else:
        sign = "O"
    char = str(char)    
    layout = layout.replace(char,sign)  #Replace the chosen numbered square in the game board by the player's sign
    
    char = int(char)
    check_list[char] = sign

def isWinner():     #Function the uses the check_list to check if there are three contiguous signs in either in a row, column or diagonally and declare that there is a winner
    global check_list
    if check_list[1] == check_list[2] and check_list[1] == check_list[3]:
        return True
    elif check_list[1] == check_list[4] and check_list[1] == check_list[7]:
        return True
    elif check_list[1] == check_list[5] and check_list[1] == check_list[9]:
        return True
    elif check_list[2] == check_list[5] and check_list[2] == check_list[8]:
        return True
    elif check_list[3] == check_list[6] and check_list[3] == check_list[9]:
        return True
    elif check_list[3] == check_list[5] and check_list[3] == check_list[7]:
        return True
    elif check_list[4] == check_list[5] and check_list[4] == check_list[6]:
        return True
    elif check_list[7] == check_list[8] and check_list[7] == check_list[9]:
        return True
    
def draw():     #Function to declare a draw if all the squares are taken and the isWinner function fails to return True
    global layout
    contains_digit = any(map(str.isdigit, layout))
    if contains_digit == False:
        return True

def get_input(player):      #Function to check the validity of the player's move (If the input isn't a single digit from 1-9 or the square is taken, then the input is rejected)
    valid = False
    global layout
    while not valid:
        message = player + " player please enter a single number: "
        move = input(message)
        if len(move) == 1 and move.isdigit():
            if move in layout:
                valid = True
        
    return move

def comp_move():    #Function for the computer to choose which square to play with ordered priorities
    global check_list
    global layout
    
    while True:
        
        for i in range(1,10):
            if i in check_list:
              check_list[i]= "O"    #Priority 1: Plays every square to check if it will result in a win for the computer then play it
              if isWinner():         
                 check_list[i]= i  
                 update_state("comp",i)
                 break
              else:
                 check_list[i]= i
            else:
                pass
        if isWinner():
              break                
                    
        for i in range(1,10):
            if i in check_list:
               check_list[i]= "X"   #Priority 2: Plays every square to check if it will result in a win for the player and a loss for the computer then play it
               if isWinner():
                 check_list[i]= i   
                 update_state("comp",i)
                 break
               else:
                 check_list[i]= i
              
            else:
                pass
        if check_list[i] == "O":
            break         
        
            
        if check_list[5] == 5:  #Priority 3: If the center square is empty then play it
            update_state("comp",5)
            break
        else:  
            while True:
                i = random.randint(1,9)     #Priority 4: Plays a random square on the edges or corners
                i = str(i)
            
                if i in layout:
                    update_state("comp",i)
                    break
                else:
                    i = 0
            break
                  
def main():
    while True:     #Game loops until there's a winner or Draw
        p1 = get_input("First")     #Get player's move      
        update_state("first",p1)    #Update the game board and check_list with the move
        print (layout)

        if isWinner():      #Check if player won
            print("Player 1 won!")
            break

        if draw():      #Check for Draw
            print("Draw")
            break
        
        print("Computer turn...")
        time.sleep(1)   #Just for suspense ;D
        comp_move()     #Check the best move for the computer
        print (layout)

        if isWinner():      #Check if computer won
            print("Computer won!")
            break

        if draw():      #Check for Draw
            print("Draw")
            break
main()
