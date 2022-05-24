import random
import re

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
    if board_state[r-1][c-1]!=" ":
        return True
    else:
        return False

def count_symbol(symbol):
    count=0
    for row in board_state:
        for cell in row:
            if cell == symbol:
                count=count+1
    return count

def check_win():
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
    # looking column wise first
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
    rowIndex=0
    for row in board_state:
        start, group, pattern = check_Xs_Os(row)
        if start!=None:
            return rowIndex+1, start+1
        rowIndex+=1      
    return None, None

def find_corner(board_state):
    for i in range(len(board_state)):
        for j in [0,7]:
            if board_state[i][j]==" ":
                return i+1, j+1
    return None, None

def find_top_bottom(board_state):
    for i in [0,7]:
        for j in range(len(board_state[i])):
            if board_state[i][j]==" ":
                return i+1, j+1
    return None, None

draw_board()

while True:
    user_row=input("Enter row: ")
    user_column=input("Enter column: ")
    user_row=int(user_row)
    user_column=int(user_column)
    is_occupy=check_occupy(user_row,user_column)
    if is_occupy:
        print("Occupied")
        continue

    modify(user_row,user_column,"X")
    match_coords=check_neighbours(user_row, user_column, "X")
    swap_symbols(user_row,user_column,match_coords,"X")
    draw_board()
    win=check_win()
    if win !="continue":
        break

    is_occupy=True
    
    while is_occupy==True:
        computer_row, computer_column=brain(board_state)
        if computer_row==None:
            computer_row, computer_column=find_corner(board_state)
        if computer_row==None:
            computer_row, computer_column=find_top_bottom(board_state)
        if computer_row == None:
            computer_row=random.randint(1,8)
            computer_column=random.randint(1,8)
        is_occupy=check_occupy(computer_row,computer_column)
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