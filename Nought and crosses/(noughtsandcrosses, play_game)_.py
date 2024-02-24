import random
import os.path
import json
random.seed()
rowcol=[1,2,3,4,5,6,7,8,9]
def draw_board():
    board=('''
             -----------
            | 1 | 2 | 3 |    
             -----------
            | 4 | 5 | 6 |
             -----------
            | 7 | 8 | 9 |
             -----------''')# Design of board
    print(f"Layresult of the board: {board}")
    return board

def welcome(board):#Function to print the welcome message
    board=draw_board()
    print(f"Welcome to the 'Tic Tac Toe' game.\nThe layout of the board is shown below: {board}")
    return board #show the board by calling draw_board function

def initialise_board(board):
    board='''
            1 2 3
            4 5 6
            7 8 9''' # setting all element in ' '
    return board

def get_player_move(board):
    while True:
        try:
            count=0
            inp=int(input(f"{board} Choose your place(1-9): "))#Asking user for their desire cell
            if(inp<1 or inp>9):
                print("Invalid Move !")
                continue
            for i in range(0,9):# make sure if user input is valid
                if(inp==rowcol[i]):
                    count+=1
                    break
            if(count==1): 
                break
            else:# checking whether the move was previously made   
                print("Move has been already made!!(Enter again)")
                continue
        except:
            print("Invalid Move !")
            continue  
    for i in range(0,9):  
        if(inp==rowcol[i]):
            rowcol[i]="X"
            break
    board=(f'''
             -----------
            | {rowcol[0]} | {rowcol[1]} | {rowcol[2]} |    
             -----------
            | {rowcol[3]} | {rowcol[4]} | {rowcol[5]} |
             -----------
            | {rowcol[6]} | {rowcol[7]} | {rowcol[8]} |
             -----------''' ) #indexing the choice
               
    return board,inp #returning row and column input


def choose_computer_move(board,inp):
    while True:
        count=0
        ranind=random.randrange(0,9)  # Letting computer randomly choose any cell
        if(rowcol[ranind]!="X" and rowcol[ranind]!="O"):
            rowcol[ranind]="O" #Displaying computer move as O
            break
        for i in range(0,9):
            if rowcol[i]!="X" and rowcol[i]!="O":
                count=count+1
        if(count==0):
            break 
        else:
            continue   
    board=(f'''
             -----------
            | {rowcol[0]} | {rowcol[1]} | {rowcol[2]} |    
             -----------
            | {rowcol[3]} | {rowcol[4]} | {rowcol[5]} |
             -----------
            | {rowcol[6]} | {rowcol[7]} | {rowcol[8]} |
             -----------''' ) #Indexing the choice
   
    print(board)    
           

def check_for_win():
    if(rowcol[0]=="X" and rowcol[1]=="X" and rowcol[2]=="X"): # Making conditioData for human win, True if human win
        return True
    elif(rowcol[3]=="X" and rowcol[4]=="X" and rowcol[5]=="X"):
        return True
    elif(rowcol[6]=="X" and rowcol[7]=="X" and rowcol[8]=="X"):
        return True
    elif(rowcol[0]=="X" and rowcol[3]=="X" and rowcol[6]=="X"):
        return True
    elif(rowcol[1]=="X" and rowcol[4]=="X" and rowcol[7]=="X"):
        return True
    elif(rowcol[2]=="X" and rowcol[5]=="X" and rowcol[8]=="X"):
        return True
    elif(rowcol[0]=="X" and rowcol[4]=="X" and rowcol[8]=="X"):
        return True
    elif(rowcol[2]=="X" and rowcol[4]=="X" and rowcol[6]=="X"):
        return True
    
    if(rowcol[0]=="O" and rowcol[1]=="O" and rowcol[2]=="O"): # Making condition for computer win, False if computer wiData
        return False
    elif(rowcol[3]=="O" and rowcol[4]=="O" and rowcol[5]=="O"):
        return False
    elif(rowcol[6]=="O" and rowcol[7]=="O" and rowcol[8]=="O"):
        return False
    elif(rowcol[0]=="O" and rowcol[3]=="O" and rowcol[6]=="O"):
        return False
    elif(rowcol[1]=="O" and rowcol[4]=="O" and rowcol[7]=="O"):
        return False
    elif(rowcol[2]=="O" and rowcol[5]=="O" and rowcol[8]=="O"):
        return False
    elif(rowcol[0]=="O" and rowcol[4]=="O" and rowcol[8]=="O"):
        return False
    elif(rowcol[2]=="O" and rowcol[4]=="O" and rowcol[6]=="O"):
        return False
    
       

def check_for_draw(): # Condition if all the cells are drawn and winning condition is not matched
    count=0
    for i in range(0,9):
        if(rowcol[i]!="X" and rowcol[i]!="O"):
            count+=1
    if(count==0):
        return True 
    else:
        return False   # Returning true if this codes condition mets otherwise false
        

def play_game(): # Code for playing game
    board=draw_board()
    score=0
    while True: #Initialising loop
        board=initialise_board(board) # Starting by initialise of  board initialise_board(board) function
        board,inp=get_player_move(board) # First asking user to enter their bid
        result=check_for_win() # Calling for checking the wiData
        if(result==True): # Displaying player has won if the return of score is 1
            score+=1
            print(board)
            print("Bravo! You've Won")
            break    
        elif(result==False):  # Displaying computer has won if the return of score is -1
            score-=1
            print(board)
            print("Computer has won")
            break
        choose_computer_move(board,inp)
        result=check_for_win()
        if(result==True):
            score+=1
            print("Bravo! You've Won")
            break    
        elif(result==False):
            score-=1
            print("Computer has won")
            break
        result=check_for_draw() # Checking the condition for draw
        if(result==True):
            score=0
            print('Draw!!')# Displaying draw if the return of score is 0
            break
        count=0
        for i in range(0,9):
            for j in range(1,10):
                if(rowcol[i]==j):
                    count+=1
        if(count==0): # Break result if draw
            break
        else:
            continue   # continuing the program
    return score    
    


def thanks():
    print("Thank you for playing the game")


def menu(): # Taking input of user in form of 1 or 2 or 3 or q
    while True:
        inp=input('''Menu:
        Start Game (1)
        Save Score (2)
        Load High Scores(3)
        End the program(q) : ''')
        if(inp=="1"): 
            score=play_game()
        if(inp=="2"):
            save_score(score)
        if(inp=="3"):
            leaders=load_scores()
            display_leaderboard(leaders)
        if(inp=="q" or inp=="Q"):
            thanks()   
            break 
        continue     #Continuing the program   


def load_scores(): # Codes to display score
 
    f=open("leaderboard.txt","r") # a text file to store the score of players in dictionary as name in Key side and score in value
    leaders=f.read() # Creating leaders variable
    return leaders # Return the value in variable


def save_score(score):

    name=input("Enter your name: ") # Asking player name
    Data={name:score} # Creating dictionary variable
    f=open("leaderboard.txt","a") 
    score=f.write(str(Data)) # Inputing score in text file
    f.close()
    #return


def display_leaderboard(leaders): # Function to display leaderboard

    print(f"Leaderboard Scores:\n{leaders}") 


menu() #Calling the function
