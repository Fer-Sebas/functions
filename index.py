# Functions

# Functions bundle instructions/behavior

def starting_scene() :
    print("You wake up in the jungle of Mexico...")
    print("1. Stand up")
    print("2. Stay hidden")
    print("3. Look at the glowing Axolotl")

def level_2() :
    print("You looked at the glowing Axolotl")
    print("1. Be amazed")
    print("2. Put it in your inventory")
    print("3. Touch it")

def game_over() :
    print('You have no lives left.')
    print ('game over')

def losing_a_life() :
    lives = lives - 1
    print("You lost a life")

    starting_scene()

lives = 3    

while lives > 0:
    starting_scene()

    answer1 = int(input("What do you do?"))

    if answer1 != 3 :
        losing_a_life()        

    if answer1 == 3 :
        level_2()

        answer2 = int(input("What is your decision?"))

        if answer2 != 1 :
            losing_a_life()

        else :
            print("you reached level 3")

    break