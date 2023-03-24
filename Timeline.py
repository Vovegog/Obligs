import random
import os
# 1 Create deck of cards
# 2 Create "table"
# 3 Have computer pull a random card onto the table
# 4 Player pulls card
    # 5 Decide which index-position to put down card. For loop to print out table? Turns out; YES
        # 6 If correct, see 4. If wrong, game over.
# 7 Try again?


# Open and read the file

with open("Timeline_happenings.txt", "r") as file:
    cards = file.read()

# Convert into a nested list. 1 done

temp_list = []
for line in cards:  # Split the read file at line-shifts
    temp_list.append(cards.split("\n"))
temp_list = temp_list[0] # Remove the nesting that happens

game_list = []
for i in range(len(temp_list)): 
    card = temp_list[i] # Take each element in the list
    card = card.split(",") # Split by the comma
    game_list.append(card) # And append it as a list
                           # This gives us a nested list where [i][0] is year, and [i][1] is name of the card

def clearScreen():
    os.system("cls")

# Run game while True
# Duplicate card-list for use with remove()
    # Then run game while range(len(duped_list)) > 0 and play_game is True
clearScreen()

play_game = True
lose_game = False
while play_game:
    dupe_list = []
    cards_on_table = [] # Create a table. 2 done
    dupe_list = game_list # Make a duplicate deck of cards for easy "start over"

    rand = random.choice(dupe_list) # Start the game off by picking a random card. 3 done
    cards_on_table.append(rand) # And add it to the table
    dupe_list.remove(rand) # Remove it from the playable deck of cards

    # Block of code for whether you want to play again
    if lose_game == True:
        clearScreen()
        play = input("Do you wish to try again? \"Yes\" to play again or \"No\" to exit the game: ")
        if play.lower() == "no":
            break
        elif play.lower() == "yes":
            lose_game = False
        else:
            print("Invalid input! Please try again.")
        

    while len(dupe_list) > 0 and not lose_game: # This loop can be moved into a function
        rand = random.choice(dupe_list) # Pick random card for player. 4 done
        dupe_list.remove(rand) # Remove it from the playable cards
        for i in range(len(cards_on_table)):
            print("Index " + str(cards_on_table.index(cards_on_table[i])) + f" - {cards_on_table[i][1]}") # Print index-value and name of cards currently on the table

        print(f"You picked \"{rand[1]}\", where do you want to put it?")
        guess = int(input("Put card in index value: ")) # Let the player guess index to put card
        if guess > len(cards_on_table): # If selected index is out of range, choose the end index
            guess = len(cards_on_table) 
        cards_on_table.insert(guess, rand)
        print(cards_on_table)
        print(len(cards_on_table))

        if guess == 0:
            # Check only to right
            if int(cards_on_table[0][0]) <= int(cards_on_table[1][0]):
                pass
            else:
                print("You guessed wrong. You lose!")
                lose_game = True
        elif guess == len(cards_on_table)-1:
            # Check only to left
            if int(cards_on_table[guess-1][0]) <= int(cards_on_table[guess][0]): # If placed card has bigger year than the one to the left, pass
                pass
            else:
                print("You guessed wrong. You lose!")
                lose_game = True
        else:
            # Check both ways
            if int(cards_on_table[guess-1][0]) <= int(cards_on_table[guess][0]) <= int(cards_on_table[guess+1][0]):
                pass
            else:
                print("You guessed wrong. You lose!")
                lose_game = True
        
        clearScreen()
