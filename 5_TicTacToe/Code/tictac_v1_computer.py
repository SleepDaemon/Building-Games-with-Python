from copy import deepcopy
import random
from textwrap import fill
import time

def draw_board(array):
    print (" 0| X|  ")
    print ("__|__|__")
    print ("  | 0|  ")
    print ("__|__|__")
    print ("  |  | X")
    print ("  |  |  ")

def draw_board_with_values(array):
    print (" "+array[0]+"| "+array[1]+"| "+array[2])
    print ("__|__|__")
    print (" "+array[3]+"| "+array[4]+"| "+array[5])
    print ("__|__|__")
    print (" "+array[6]+"| "+array[7]+"| "+array[8])
    print ("  |  |  ")

def check_win(tictac_array):
    if  tictac_array[0] == tictac_array[4] and tictac_array[4] == tictac_array[8] and tictac_array[8]!=" ":
       if tictac_array[0] == "X":
          return "X"
       else:
            return "0"
    elif  tictac_array[2] == tictac_array[4] and tictac_array[4] == tictac_array[6] and tictac_array[6]!=" ":
       if tictac_array[2] == "X":
          return "X"
       else:
            return "0"
    elif  tictac_array[0] == tictac_array[1] and tictac_array[1] == tictac_array[2] and tictac_array[2]!=" ":
       if tictac_array[0] == "X":
          return "X"
       else:
            return "0"
    elif  tictac_array[3] == tictac_array[4] and tictac_array[4] == tictac_array[5] and tictac_array[5]!=" ":
       if tictac_array[3] == "X":
          return "X"
       else:
            return "0"
    elif  tictac_array[6] == tictac_array[7] and tictac_array[7] == tictac_array[8] and tictac_array[8]!=" ":
       if tictac_array[6] == "X":
          return "X"
       else:
            return "0"
    elif  tictac_array[0] == tictac_array[3] and tictac_array[3] == tictac_array[6] and tictac_array[6]!=" ":
       if tictac_array[0] == "X":
          return "X"
       else:
            return "0"
    elif  tictac_array[1] == tictac_array[4] and tictac_array[4] == tictac_array[7] and tictac_array[7]!=" ":
       if tictac_array[1] == "X":
          return "X"
       else:
            return "0"
    elif  tictac_array[2] == tictac_array[5] and tictac_array[5] == tictac_array[8] and tictac_array[8]!=" ":
       if tictac_array[2] == "X":
          return "X"
       else:
            return "0"
    elif tictac_array[0] != " " and tictac_array[1] != " " and tictac_array[2] != " " and tictac_array[3] != " " and tictac_array[4] != " " and tictac_array[5] != " " and tictac_array[6] != " " and tictac_array[7] != " " and tictac_array[8] != " ":
      print ("match draw")
      return "X0"
    else: 
       return False

def get_empty_spaces(fill_tictac):
   empty_spaces_remaining=[]
   for i in range (len(fill_tictac)):
         if fill_tictac [i] == " ":
            empty_spaces_remaining.append(i)
   return empty_spaces_remaining

def computer_brain(fill_tictac):
   empty_spaces=get_empty_spaces(fill_tictac)
   #Main Offense Module
   for empty_space in empty_spaces:
      copy_original_board=deepcopy(fill_tictac)
      copy_original_board[empty_space]="0"
      winner=check_win(copy_original_board)
      if winner=="0":
         fill_tictac[empty_space]="0"
         return fill_tictac
   #Main Defense Module
   for empty_space in empty_spaces:
      copy_original_board=deepcopy(fill_tictac)
      copy_original_board[empty_space]="X"
      winner=check_win(copy_original_board)
      if winner=="X":
         fill_tictac[empty_space]="0"
         return fill_tictac
   computer_space=random.choice(empty_spaces)
   #First Offense Module
   corners=[0,8]
   available_corners=[]
   for corner in corners:
      if fill_tictac [corner] == " ":
         available_corners.append(corner)
   if len(available_corners)==2:
      computer_space=random.choice(available_corners)   
      fill_tictac[computer_space]= "0"
      return fill_tictac
   #Second Offense Module
   if fill_tictac [6] == "0" and fill_tictac [8] == "X" and fill_tictac [2] == " ":
       fill_tictac[2]="0"
       return fill_tictac
   elif fill_tictac [8] == "0" and fill_tictac [6] == "X" and fill_tictac [0] == " ":
       fill_tictac[0]="0"
       return fill_tictac
   elif fill_tictac [0] == "0" and fill_tictac [6] == "X" and fill_tictac [8] == " ":
       fill_tictac[8]="0"
       return fill_tictac          
   if fill_tictac[8]=="X" and fill_tictac[0]==" ":
       fill_tictac[0]="0"
       return fill_tictac
   elif fill_tictac[8]=="X" and fill_tictac[6]==" ":
       fill_tictac[6]="0"
       return fill_tictac
   elif fill_tictac[8]==" " and fill_tictac[0]=="X":
       fill_tictac[8]="0"
       return fill_tictac
   elif fill_tictac[6]==" " and fill_tictac[2]=="X":
       fill_tictac[6]="0"
       return fill_tictac
   elif fill_tictac[2]==" " and fill_tictac[0]=="X":
       fill_tictac[2]="0"
       return fill_tictac
   # nothing chosen return random
   fill_tictac[computer_space]="0"
   return fill_tictac
blank_tictac = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

fill_tictac = ["0", "X", "X", "X", "0", " ", " ", " ", "0"]
fill_tictac=blank_tictac
print("Game starts")

print ("Computer is 0, and Player is X")

player_valid_move=True

while check_win(fill_tictac)==False:
   if player_valid_move==True:
      print("Computer is making it's turn")
      time.sleep(3) 
      fill_tictac = computer_brain (fill_tictac)
      print("tictac_array:",fill_tictac)
      if check_win(fill_tictac)=="0":
         print("Computer has won")
         break
      elif check_win(fill_tictac)=="X0":
         break
      
      draw_board_with_values(fill_tictac)

   print ("Player's Turn")
   time.sleep(2)
   space=int(input ("choose your space (0-8)"))
   if fill_tictac[space] != " ":
      print ("space is filled, choose different space")
      player_valid_move=False
      continue
   else:
      player_valid_move=True
   fill_tictac[space] = "X"
  
   draw_board_with_values(fill_tictac)
   if check_win(fill_tictac)!=False:
      break  
draw_board_with_values(fill_tictac)