import random
import re
import numpy as np

rows = 8
columns = 8

board_state=[
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," ","X","O"," "," "," "],
    [" "," "," ","O","X"," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "]
]

def draw_board():
    '''
    Draws the board
    '''
    line_string_0="".join(str(x) for x in board_state[0])
    line_string_1="".join(str(x) for x in board_state[1])
    line_string_2="".join(str(x) for x in board_state[2])
    line_string_3="".join(str(x) for x in board_state[3])
    line_string_4="".join(str(x) for x in board_state[4])
    line_string_5="".join(str(x) for x in board_state[5])
    line_string_6="".join(str(x) for x in board_state[6])
    line_string_7="".join(str(x) for x in board_state[7])
    print("  12345678")
    print(" +--------+")
    print('1|'+line_string_0+'|1')
    print('2|'+line_string_1+'|2')
    print('3|'+line_string_2+'|3')
    print('4|'+line_string_3+'|4')
    print('5|'+line_string_4+'|5')
    print('6|'+line_string_5+'|6')
    print('7|'+line_string_6+'|7')
    print('8|'+line_string_7+'|8')
    print(" +--------+")
    print("  12345678")

def modify(r,c,symbol):
    '''
    User will give input from 1-8, and python translates it to 0-7.
    So we do r-1, c-1
    '''
    board_state[r-1][c-1]=symbol

def check_occupy(r,c):
    '''
    Checks if the cell is occupied
    '''
    if board_state[r-1][c-1]!=" ":
        return True
    else:
        return False

def count_symbol(symbol):
    '''
    Counts the number of symbol (X or O as specified) in the board
    '''
    count=0
    for row in board_state:
        for cell in row:
            if cell == symbol:
                count=count+1
    return count

def check_win():
    '''
    Counts the number of Xs and Os in the board, and returns the winner
    '''
    num_xs=count_symbol("X")
    num_os=count_symbol("O")
    print("X:",num_xs)
    print("O:",num_os)
    if num_xs+num_os==(rows*columns):
        if num_xs>num_os:
            return "X"
        elif num_xs<num_os:
            return "O"
        else:
            return "Draw"
    else:
        return "continue"

def check_neighbours(r,c,symbol):
    '''
    Checks the neighbours of the cell, looks vertically & horizontally for the same symbol
    '''
    match_coords=[]
    row_num=r-2
    while row_num >=0:
        if board_state[row_num][c-1]==symbol:
            match_coords.append((row_num+1,c,"up"))
            break
        elif board_state[row_num][c-1]==" ":
            break
        row_num=row_num-1
    row_num=r
    while row_num <rows:
        if board_state[row_num][c-1]==symbol:
            match_coords.append((row_num+1,c,"down"))
            break
        elif board_state[row_num][c-1]==" ":
            break
        row_num=row_num+1
    # looking row wise
    column_num=c-2
    while column_num >=0:
        if board_state[r-1][column_num]==symbol:
            match_coords.append((r,column_num+1,"left"))
            break
        elif board_state[r-1][column_num]==" ":
            break
        column_num=column_num-1
    column_num=c
    while column_num <columns:
        if board_state[r-1][column_num]==symbol:
            match_coords.append((r,column_num+1,"right"))
            break
        elif board_state[r-1][column_num]==" ":
            break
        column_num=column_num+1
    print(match_coords)
    return match_coords

def swap_symbols(r,c,match_coords,symbol):
    '''
    Swaps the symbols of the cells in the match_coords list
    '''
    for coord in match_coords:
        if coord[2]=="up":
            cur_row=r-1
            cur_col=c-1
            print(cur_row,cur_col,coord[0],coord[1])
            while cur_row>coord[0]-1:
                board_state[cur_row][cur_col]=symbol
                cur_row=cur_row-1
        elif coord[2]=="down":
            cur_row=r
            cur_col=c-1
            print(cur_row,cur_col,coord[0],coord[1])
            while cur_row<coord[0]:
                board_state[cur_row][cur_col]=symbol
                cur_row=cur_row+1
        elif coord[2]=="left":
            cur_row=r-1
            cur_col=c-1
            while cur_col >coord[1]-1:
                board_state[cur_row][cur_col]=symbol
                cur_col=cur_col-1
        elif coord[2]=="right":
            cur_row=r-1
            cur_col=c-1
            while cur_col<coord[1]:
                board_state[cur_row][cur_col]=symbol
                cur_col=cur_col+1

def check_Xs_Os(row):
    '''
    Checks if the row has Xs and Os, for the computer to find potential advantage points
    '''
    string_row="".join(str(x) for x in row)
    # looking for the pattern of 1 space, 1 or more Xs followed by 1 ore more Os
    p = re.compile(" X+O+")
    for m in p.finditer(string_row):
        # print("found p1 at", m.start(), m.group(), row)
        return m.start(), m.group(), "p1"

    # looking for the pattern of 1 or more Os, 1 or more Xs followed by 1 space
    p = re.compile("O+X+ ")
    for m in p.finditer(string_row):
        # print("found p2 at", m.start(), m.group(), row)
        return m.start()+len(m.group())-1, m.group(), "p2"
    
    p=re.compile(" X+ +")
    for m in p.finditer(string_row):
        # print("found p3 at", m.start(), m.group(), row)
        return m.start(), m.group(), "p3"
        
    p=re.compile(" +X+ ")    
    for m in p.finditer(string_row):
        # print("found p4 at", m.start(), m.group(), row)
        return m.start()+len(m.group())-1, m.group(), "p4"
        
    return None, None, None

def brain(board_state):
    '''
    The computer's brain
    '''
    possible_moves=[]

    rowIndex=0
    for row in board_state:
        start, group, pattern = check_Xs_Os(row)
        if start!=None:
            print("Horizontal")
            possible_moves.append([rowIndex+1, start+1])
            # return rowIndex+1, start+1
        rowIndex+=1   
    # vertical search
    rowIndex=0
    board_state_transpose=np.transpose(board_state)
    for row in board_state_transpose:
        start, group, pattern = check_Xs_Os(row)
        if start!=None:
            print("Vertical")
            possible_moves.append([start+1, rowIndex+1])
            # return start+1, rowIndex+1
        rowIndex+=1
    return possible_moves
    # return None, None

def find_corner(board_state):
    '''
    Finds the first empty sides
    '''
    for i in range(len(board_state)):
        for j in [0,7]:
            if board_state[i][j]==" ":
                return i+1, j+1
    return None, None

def find_top_bottom(board_state):
    '''
    Find empty space in the top and bottom rows
    '''
    for i in [0,7]:
        for j in range(len(board_state[i])):
            if board_state[i][j]==" ":
                return i+1, j+1
    return None, None

draw_board()

while True:
    '''
    The main game loop
    '''
    # player's turn
    user_row=input("Enter row: ")
    user_column=input("Enter column: ")
    user_row=int(user_row)
    user_column=int(user_column)
    is_occupy=check_occupy(user_row,user_column)
    if is_occupy:
        print("Occupied")
        continue
    
    # modify the board to user input
    modify(user_row,user_column,"X")
    match_coords=check_neighbours(user_row, user_column, "X")
    swap_symbols(user_row,user_column,match_coords,"X")
    draw_board()
    win=check_win()
    if win !="continue":
        break

    is_occupy=True

    # computer's turn
    while is_occupy==True:
        list_moves=brain(board_state)
        # find corner
        computer_row, computer_column=find_corner(board_state)
        if computer_row != None:
            list_moves.append([computer_row, computer_column])
        # find top and bottom
        computer_row, computer_column=find_top_bottom(board_state)
        if computer_row != None:
           list_moves.append([computer_row, computer_column])
        # random move
        computer_row=random.randint(1,8)
        computer_column=random.randint(1,8)
        list_moves.append([computer_row, computer_column])
        # choose one of the possible moves
        selected_move=random.choice(list_moves)
        computer_row=selected_move[0]
        computer_column=selected_move[1]
        is_occupy=check_occupy(computer_row,computer_column)
   
    # modify the board to computer input
    modify(computer_row,computer_column,"O")
    match_coords=check_neighbours(computer_row, computer_column, "O")
    swap_symbols(computer_row,computer_column,match_coords,"O")
    print('computer choice: ',computer_row,computer_column)
    draw_board()
    win=check_win()
    if win!="continue":
        break
if win == "X":
    print("X wins")
elif win == "O":
    print("O wins")