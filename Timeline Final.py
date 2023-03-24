import random
import os

def read_cards(file_path):
    """
    Reads the cards from the given file and returns a nested list.
    """
    with open(file_path, "r") as file:
        cards = file.read()
    temp_list = []
    for line in cards:
        cards.split("\n")
        cards.split(",")
#    temp_list = temp_list[0]
    game_list = []
    for i in range(len(temp_list)):
        card = temp_list[i]
    #    card = card.split(",")
        game_list.append(card)
    return game_list

def clear_screen():
    """
    Clears the console screen.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def play_game():
    """
    Starts a new game.
    """
    clear_screen()
    game_list = read_cards("Timeline_happenings.txt")
    play_game = True
    lose_game = False
    while play_game:
        dupe_list = game_list.copy() # Copy deck of cards into a playable deck
        cards_on_table = []          # Create table
        rand = random.choice(dupe_list) # Pick a random card
        cards_on_table.append(rand)     # Add to table
        dupe_list.remove(rand)          # Remove from deck of cards
        if lose_game:       # If you lost the game :
            play = input("Do you wish to play again? \"Yes\" to play again or \"No\" to exit the game: ")
            if play.lower() == "no":    # Stop the game
                break
            elif play.lower() == "yes": # Or play again
                lose_game = False
            else:
                print("Invalid input! Please try again.") # Error handling for invalid input
            clear_screen()
        while len(dupe_list) > 0 and not lose_game:
            rand = random.choice(dupe_list) # Pick random card
            dupe_list.remove(rand)          # Remove from deck of cards
            # Then print out all current cards on the table with associated year
            for i in range(len(cards_on_table)):
                print("Index " + str(cards_on_table.index(cards_on_table[i])) + f" - {cards_on_table[i][0]}, {cards_on_table[i][1]}")
            print(f"You picked \"{rand[1]}\", where do you want to put it?")
            guess = int(input("Put card in index value: ")) # Lets user pick place on the table (by index value)
            if guess > len(cards_on_table): # If index is out of range
                guess = len(cards_on_table) # Make the guess into the last index available
            cards_on_table.insert(guess, rand)  # Add card to table
            clear_screen()
            if guess == 0:  # If card is added to index-value 0, check only for card to the right
                if int(cards_on_table[0][0]) <= int(cards_on_table[1][0]):
                    pass
                else:
                    print("You guessed wrong. You lose!")
                    lose_game = True
            elif guess == len(cards_on_table)-1:     # If card is added to the end of the table, check only for card to the left
                if int(cards_on_table[guess-1][0]) <= int(cards_on_table[guess][0]):
                    pass
                else:
                    print("You guessed wrong. You lose!")
                    lose_game = True
            else:   # Check for cards to both the left AND the right
                if int(cards_on_table[guess-1][0]) <= int(cards_on_table[guess][0] )<= int(cards_on_table[guess+1][0]):
                    pass
                else:
                    print("You guessed wrong. You lose!")
                    lose_game = True
            if dupe_list == []: # If the playable deck of cards is empty, you win! If you play again, this list will be filled over again
                print("Congratulations! You win!")
                lose_game = True    # Is named "lose_game", but acts more like a "play game?"
                break   # Breaks the loop and asks you if you want to play again

play_game()