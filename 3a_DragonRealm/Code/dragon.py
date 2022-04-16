import random

restart="y"
while restart=="y":
    print("You are in a land full of Dragons.\nIn front you have three caves, one has treasure while the other has a hungry dragon, other has nothing.\nWhich cave will you choose? (1, 2, or 3)")
    choice = input()
    choice=int(choice)

    print("You chose cave", choice)
    options=[1,2,3]
    random.shuffle(options)
    dragon_choice=options[0]
    treasure_choice=options[1]
    empty_choice=options[2]


    if choice == dragon_choice:
        print("Dragon cave, you have died")
    elif choice == empty_choice:
        print("Empty cave, you have nothing")
    elif choice == treasure_choice:
        print("Treasure cave, you have gold")
        print("--"*15)
        restart_2="y"
        while restart_2=="y":
            print("Level 2, there are 3 caves.\nOne has treasure, one has nothing, and the other has Snakes.\nWhich cave will you choose? (1, 2, or 3)")
            choice = input()
            choice=int(choice)

            print("You chose cave", choice)
            options=[1,2,3]
            random.shuffle(options)
            snake_choice=options[0]
            treasure_choice=options[1]
            empty_choice=options[2]

            if choice == snake_choice:
                print("Snake Cave, you have died")
                retstart_2=input("Do you want restar from Checkpoint? (y/n)")
            elif choice == empty_choice:
                print("Empty Cave, you have nothing")
                retstart_2=input("Do you want restar from Checkpoint? (y/n)")
            elif choice == treasure_choice:
                print("Treasure Cave, you have completed the game")
                restart_2="n"
                # print("restart 2",restart_2)
        

    print("End of game")
    restart=input("Do you want to restart? (y/n)")
    print("***"*15)


print("Bye")