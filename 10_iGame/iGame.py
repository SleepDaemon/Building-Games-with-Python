
rows = 8
columns = 8

print(rows, columns)

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

draw_board()

user_row=input("Enter row: ")
user_column=input("Enter column: ")
user_row=int(user_row)
user_column=int(user_column)

modify(user_row,user_column,"X")
match_coords=check_neighbours(user_row, user_column, "X")
swap_symbols(user_row,user_column,match_coords,"X")
draw_board()