import random #imports the random module that is used later in the code 
# game board
#while True:
name = input('Please enter your name: ') # input 1]
    #name2 = int(name)
    #namelen = name(len(2)) 
#name1 = int(input('please enter your name: '))
name2 = type(name)
print(name2)
if name2 == str:
    print(f'welcome to naughts and crosses {name}, I hope you enjoy')
elif name2 == int or float:
    input(f' you didnt enter a name properly {name}, Please enter your name again')  # this asks the user to input their name and after the user does this it valadates the input

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"] #the varuable that is used to print the board

current_player = 'X'
game_running = True
winner = None 
#print(current_player, type)
#the game board is defined
#print(f'welcome to naughts and crosses {name}, I hope you enjoy')
def game_board(board):
    print("--------")
    print(str("|" + board[0] + "|" + board[1] + "|" + board[2] + "|"))
    print("--------")
    print(str("|" + board[3] + "|" + board[4] + "|" + board[5] + "|"))
    print("--------")
    print(str("|" + board[6] + "|" + board[7] + "|" + board[8]+ "|"))
    print("--------")
   
    #this prints out the game board this also inntlises the game board
    return
game_board(board) # prints the game board to the screen


user_choice = input('Please enter X or O: ') # the user choses x or o
user_choice2 = user_choice.capitalize() # captlises the user input
#if user_choice2 != 'X':
    #print('Try again')
#elif user_choice2 != 'O':
    #print('Try again')
    
    
    #return 
 #todo 
computer_choice = [] # creates a list where the computer choice 
if user_choice2 == 'X':  # the if else statment choses the computers this choice is oppset to the user choice so that the computer and the user can play between each other
    computer_choice = 'O'
else:
    computer_choice = 'X'
    
    
print(f"You are player: {user_choice2}") #prints the users player to the screen 
print(f"Your opponent is player: {computer_choice}") #prints the other player to the screen 



# the player input is where the player inputs where they are going to put their marker
def player_input(board):
    inp = int(input('Please enter a number between 1 and 9: ')) # input 2 
  #  #print(inp - 1)
    if board[inp-1] == "-":
        board[inp-1] = current_player
    else:
        print('try again!!')
    return


#check for win or tie
#this checks the horizontal of the board fro all the possabilties of a win or tie
def check_horizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True
# this checks the rows of all the possabilties of a win
def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True
# this checks all possabilties of a win in the diagnail     
def check_diag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True
# this checks if aa win has happened     
def check_if_win(board):
    global game_running
    if check_horizontle(board):
        #print(board)
        print(f"The winner is {winner} !!!!")
        game_running = False
    elif check_row(board):
        #print(board)
        print(f"The winner is {winner} !!!!")
        game_running = False
    elif check_diag(board):
        #print(board)
        print(f"The winner is {winner} !!!!")
        game_running = False
# this checks if their is a tie         
def check_if_tie(board):
    global game_running
    if "-" not in board:
        #print(board(board))
        print('It is a tie!')
        game_running = False
# switch player
# this switches the player between x and o 
def switch_player():
    global current_player  #todo
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return    
# this is the funtion that controls where the computer's marker is placed during single player         
def computer(board):
    #while computer_choice == True:
    pos = random.randint(0 , 8)
    if board[pos] == '-':
        board[pos] = computer_choice
    return
    
# this controls the game 
while game_running == True:
    game_board(board)
    #user_choice()
    player_input(board)
    #game_board(board)
    #switch_player()
    check_horizontle(board)
    check_row(board)
    check_diag(board)
    check_if_win(board)
    check_if_tie(board)
    switch_player()
    game_board(board)
    #computer(board)
    #switch_player()
    #computer_choice(board)
