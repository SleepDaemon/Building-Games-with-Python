import random

# Creates the treasure locations
def compute_choices(max_rows, max_cols, userRow, userCol):
    user_choices = []
    user_choices.append([userRow,userCol])
    if userCol < max_cols-1:
        user_choices.append([userRow,userCol+1])
    if userRow < max_rows-1:
        user_choices.append([userRow+1,userCol])
    if userRow < max_rows-1 and userCol < max_cols-1:
        user_choices.append([userRow+1,userCol+1])
    return user_choices 

# Creates the board at the start of the game
def draw_initial_board(rows, columns):
    board=[]
    for i in range(rows):
        board.append(["0"]*columns)
        print("~ "*columns)
    return board

# Creates the board after the user has made a choice
def draw_current_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "0":
                print("~ ", end="")
            elif board[i][j] == "$":
                print("$ ", end="")
            elif board[i][j] == "#":
                print("# ", end="")                
            elif board[i][j] == "@":
                print("@ ", end="")
        print("\n")

# Checks if the user has won the game
def check_win(board, treasure_locations):
    treasures_found=0
    win_status=True
    for treasure in treasure_locations:
        if board[treasure[0]][treasure[1]] == "$":
            win_status=win_status&True
            treasures_found+=1
        else:
            win_status=win_status&False
    return win_status, treasures_found

# Checks if the user has found a treasure
def check_treasure(board, user_choices, treasure_locations):
   
    exactTreasure=False
    for treasure in treasure_locations:
        treasure_row=treasure[0]
        treasure_col=treasure[1]
        if treasure_row == user_choices[0][0] and treasure_col == user_choices[0][1]:
            print("You found a treasure!")
            board[treasure_row][treasure_col] = "$"
            exactTreasure=True
   
    approxTreasure=False
    for treasure in treasure_locations:
        treasure_row=treasure[0]
        treasure_col=treasure[1]
        for choice in user_choices[1:]:
            if treasure_row == choice[0] and treasure_col == choice[1]:
                approxTreasure=True

    if approxTreasure == True and exactTreasure == False:
        for choice in user_choices:
            if board[choice[0]][choice[1]] == "0":
                board[choice[0]][choice[1]] = "#"

    if approxTreasure == False:
        for choice in user_choices:
            if board[choice[0]][choice[1]] == "0":
                board[choice[0]][choice[1]] = "@"
    return board

# Main function
max_rows=6
max_cols=16
number_of_treasures=4
treasure_locations=[]
all_locations=[]
for i in range(0,max_rows):
    for j in range(0,max_cols):
        all_locations.append([i,j])
for i in range(number_of_treasures):
    random_location=random.choice(all_locations)
    all_locations.remove(random_location)
    treasure_locations.append(random_location)

max_turns=max_rows*max_cols//4-4
turn_num=0

# Ineraction with the user
print("Welcome to the Treasure Hunt!\n You have", max_turns, "turns to find all the treasures.\n @ = You have not found a treasure yet.\n # = You have found a treasure, but you are not sure if it is the correct one.\n $ = You have found the correct treasure.\n ~ = You have not yet been to this location.\n Good luck! \n")
board=draw_initial_board(max_rows,max_cols)
for turn_num in range(max_turns):
    win_status, treasures_found=check_win(board, treasure_locations)
    if win_status == True:
        print("You found all the treasures!")
        break
    print("Your turn:", turn_num, "out of", max_turns)
    print("Found treasures:", treasures_found, "out of", number_of_treasures)
    userRow=int(input("Enter your Row number [0-"+str(max_rows-1)+"]: "))
    userCol=int(input("Enter your Column number [0-"+str(max_cols-1)+"]:"))
    if userRow < 0 or userRow >= max_rows:
        print("Invalid Row number")
        continue
    if userCol < 0 or userCol >= max_cols:
        print("Invalid Column number")
        continue
    user_choices = compute_choices(max_rows, max_cols, userRow, userCol)
    board=check_treasure(board, user_choices, treasure_locations)
    draw_current_board(board)