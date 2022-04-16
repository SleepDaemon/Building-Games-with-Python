import random
from wsgiref.util import guess_scheme
lst = random.sample(range(0, 9), 3)
lst2=[]
for val in lst:
    lst2.append(str(val))

max_guess = 10

lst=lst2
print('''I am thinking of a 3-digit number. Try to guess what it is. ,
The clues I give are...
When I say:    That means:
  Gamma       None of the digits is correct.
  Beta         One digit is correct but in the wrong position.
  Alpha        One digit is correct and in the right position.
I have thought up a number. You have 10 guesses to get it.''')
while True:
    guess_count = 1
    while guess_count < max_guess:
        print("Guess", guess_count)
        user_guess = input("Enter your guesses: (Three Digits) ")
        if user_guess ==  "":
            print("You didn't enter anything")
            continue
        print(user_guess)
        guess_count += 1
        hints=[]

        #Alpha Check
        if user_guess[0] == lst[0]:
            hints.append("Alpha")
        if user_guess[1] == lst[1]:
            hints.append("Alpha")
        if user_guess[2] == lst[2]:
            hints.append("Alpha")

        #Beta Check
        if user_guess[0] == lst[1]:
            hints.append("Beta")
        if user_guess[0] == lst[2]:
            hints.append("Beta")
        if user_guess[1] == lst[0]:
            hints.append("Beta")
        if user_guess[1] == lst[2]:
            hints.append("Beta")
        if user_guess[2] == lst[0]:
            hints.append("Beta")
        if user_guess[2] == lst[1]:
            hints.append("Beta")

        #Gamma Check
        if user_guess[0] != lst[0] and user_guess[0] != lst[1] and user_guess[0] != lst[2]:
            hints.append("Gamma")
        if user_guess[1] != lst[0] and user_guess[1] != lst[1] and user_guess[1] != lst[2]:
            hints.append("Gamma")
        if user_guess[2] != lst[0] and user_guess[2] != lst[1] and user_guess[2] != lst[2]:
            hints.append("Gamma")
        print(hints)

        #Check Win
        if user_guess[0] == lst[0] and user_guess[1] == lst[1] and user_guess[2] == lst[2]:
            print("You Win!")
            print(lst)
            choice = input("Play Again? (Y/N) ")
            break
    if choice == "N" or choice == "n":
        print("Quitting Game")
        break
