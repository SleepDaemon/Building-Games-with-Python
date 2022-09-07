import random
num=random.randint(1,20)

user=input ("Hello, What's your name?: ")
print (user)
print ("Well,", user, "I am thinking of a number between 1 and 20.")
print ("Guess in 6 tries or less")

for i in range(6):
    guess=input("take a guess: ")
    guess=int(guess)
    if guess > num:
        print("too High")
    if guess < num:
        print("too Low")
    if guess == num:
        print("Correct")
        break
if guess != num:
    print ("I was thinking of", num)
    print ("You lose, Play again?")