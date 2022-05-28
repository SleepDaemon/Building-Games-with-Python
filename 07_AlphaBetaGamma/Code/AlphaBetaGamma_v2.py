# This code will take the number of digits from user
import random
from wsgiref.util import guess_scheme

digits=int(input("Enter the number of digits: "))
max_guess = 5*digits
print("I am thinking of a "+str(digits)+"-digit number. Try to guess what it is. ,")
print('''The clues I give are...
When I say:    That means:
  Gamma       None of the digits is correct.
  Beta         One digit is correct but in the wrong position.
  Alpha        One digit is correct and in the right position.''')
print("I have thought up a number. You have "+str (max_guess)+" guesses to get it.")
while True:
    lst = random.sample(range(0, 9), digits)
    lst2=[]
    for val in lst:
        lst2.append(str(val))
    lst=lst2
    guess_count = 1
    win_status=False
    while guess_count < max_guess:
        print("Guess", guess_count)
        user_guess = input("Enter your guesses: ("+str(digits)+" Digits) ")
        if user_guess ==  "":
            print("You didn't enter anything")
            continue
        print(user_guess)
        guess_count += 1
        hints=[]
        win_status=False

        #Alpha Check
        for i in range(len(lst)):
            if lst[i] == user_guess[i]:
                hints.append("Alpha")

        #Beta Check
        for i in range(len(user_guess)):
            for j in range(len(lst)):
                if i !=j:
                    if user_guess[i] == lst[j]:
                        hints.append("Beta")

        #Gamma Check
        for i in range(len(user_guess)):
            digit_absent=True
            for j in range(len(lst)):
                    if user_guess[i] != lst[j]:
                        digit_absent=digit_absent&True
                    else:
                        digit_absent=digit_absent&False
            if digit_absent:
                hints.append("Gamma")
        print(hints)

        #Check Win
        win_check=True

        for i in range(len(lst)):
            if lst[i] == user_guess[i]:
                win_check=win_check&True
            else:
                win_check=win_check&False
        if win_check:
            print("You Win!")
            win_status=True
            print(lst)
            choice = input("Play Again? (Y/N) ")
            break
    if win_status==False:
        print("You Lose!", lst)
        choice = input("Play Again? (Y/N) ")
    if choice == "N" or choice == "n":
        print("Quitting Game")
        break
