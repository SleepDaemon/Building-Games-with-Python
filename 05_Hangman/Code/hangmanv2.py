import random

def divide_into_groups(words):
    easy=[]
    medium=[]
    hard=[]
    for w in words:
        l=(len (w))
        if l <=4:
            hard.append (w)
        elif l > 4 and l <=5:
            medium.append (w)
        elif l >= 6:
            easy.append (w)
    return easy, medium, hard

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']


def print_correct_guesses(word, present_letters):
    for letter in word:
        if letter in present_letters:
            print(letter + " ", end='')
        else:
            print("_ ",end='')

def get_unique_letters(word):
    unique_letters =[]
    for letter in word:
        if letter not in unique_letters:
            unique_letters.append(letter)
    return unique_letters

words_animals=['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 
        'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule',
         'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep',
          'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']

words_shapes=['square', 'triangle', 'rectangle', 'circle', 'ellipse', 'rhombus', 'trapezoid', 'chevron', 'pentagon', 'hexagon', 'septagon', 'octagon', 
'Nonagon', 'Octagon', 'Heptagon', 'Hexagon', 'Triangle', 'Parallelogram', 'Rhombus', 'Square', 'Pentagon', 'Circle', 'Oval', 'Heart', 'Cross', 'Arrow', 
'Cube', 'Cylinder', 'Star', 'Crescent']


words_plants=['apple', 'orange', 'lemon', 'lime', 'pear', 'watermelon', 'grape', 'grapefruit', 'cherry', 'banana', 'cantaloupe', 'mango', 'strawberry', 'tomato', 
'avocado', 'blackberry', 'blueberry', 'plum', 'nectarine', 'raspberry', 'pineapple', 'lemon', 'coconut', 'tomato', 'eggplant', 'cucumber', 'lettuce', 'celery', 
'spinach', 'date', 'olive', 'pea', 'guava', 'kiwi', 'mulberry', 'papaya', 'potato', 'peach', 'zucchini', 'pumpkin', 'squash', 'apricot']

levels = ["easy,medium,hard"]
initial_level = 0
continuos_correct=0

continue_choice="y"

user_choice=input("Choose a Category (animal/shape/fruit):")
if user_choice == "animal":
    words = words_animals
elif user_choice == "shape":
    words = words_shapes
elif user_choice == "fruit":
    words = words_plants

while continue_choice != "n":
    game_solved=False
    print("Category is", user_choice)

    easy, medium, hard = divide_into_groups(words)
    array=[easy, medium, hard]
    if continuos_correct == 3:
        initial_level=1
    elif continuos_correct == 6:
        initial_level=2
    elif continuos_correct == 9:
        print("You won")
        break
    elif continuos_correct==0:
        initial_level=0
    wordchosen=random.choice(array[initial_level])
    wordchosen=wordchosen.lower()
    unique_letters=get_unique_letters(wordchosen)

    num_word=len(wordchosen)
    print("_ "* num_word)

    absent_letters=[]
    present_letters=[]

    hang_index=0
    max_lives=7

    while game_solved == False and hang_index < max_lives:
        print(HANGMAN_PICS[hang_index])
        cad=input("\nGuess a letter: ")
        if cad == "":
            print("No letter")
            continue
        if cad in absent_letters or cad in present_letters:
            print("You already guess this letter.")
            continue

        if (cad) in wordchosen:
            print(cad, "is present")
            present_letters.append(cad)
        else:
            print(cad, "is not present")
            absent_letters.append(cad)
            hang_index+=1

        print("Incorrect letters", absent_letters)

        print_correct_guesses(wordchosen, present_letters)
        
        if len(present_letters) == len(unique_letters):
            game_solved=True

    if hang_index == max_lives:
        print("\nYou lost, answer is", wordchosen)
        continuos_correct = 0
    else:
        print("\nYou won")
        continuos_correct +=1

    print("number of correct", continuos_correct)
    continue_choice=input("Do you want to continue? (y/n)")