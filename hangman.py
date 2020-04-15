import random


def game():
    word_list = ["sausage", "snorkel", "chunky", "egypt", "butter"]

    secret_word_choose = random.randint(0, (len(word_list)-1))
    secret_word = word_list[secret_word_choose]

    guessed_letters = ""
    display_letters = ""

    for letter in secret_word:
        display_letters = display_letters + "_"

    # Python3 program to Split string into characters 
    def split(word): 
        return [char for char in word] 
        
    display_letters = split(display_letters) 

    remaining_guess_count = 6
    win = False
    # global remaining_guess_count
    # global guessed_letters
    # global display_letters
    # global secret_word

    while remaining_guess_count > 0:
        print(f"You have {remaining_guess_count} chances remaining.")
        # print(display_letters)
        to_show = ''.join(display_letters)
        print(to_show)
        if (to_show == secret_word):
            win = True
            break

        guess = input("What is your next guess?\n")
        guessed_letters += guess
        
        count = 0
        count_correct = 0
        for letter in secret_word:
            if (secret_word[count] == guess):
                display_letters[count] = guess
                count += 1
                count_correct += 1
            else:
                count += 1
        
        if (count_correct == 0):
            remaining_guess_count -= 1

    if (win == True):
        print("You won!")
    else:
        print("Sorry you are a loserrrrr")

    play_again = input("Do you want to play again? (Y/N)\n")
    if (play_again == "y"):
        game()
    else:
        print("Goodbye")

        

game()