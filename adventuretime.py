# 1. Need at least 3 stages/chapters --
# 2. At least 2 choices --
# 3. Needs a running score --
# 4. Must error-handle invalid inputs -?
# 5. Clear beginning and end --
# 6. Must use loops to navigate through the stages --
# 7. Use dictionaries for storing the stages/choices --
# 8. Allow for adding more "choices" --
# 9. No break/continue --

import os

player_info = {"name": "", "score": 0, "sword": False}
game_over = False
stage = 1

screens = {
    "stage1": {
        "description": "You wake up in a small clearing in the woods. \nYou can hear birds chirp around you as you start looking around. \nNo apparent roads are around you, but you can start your trek through the 'trees' or some nearby 'bushes'. \nDo you wish you to go through the 'bushes', or the 'trees'?",
        "choices": {
            "trees": {
                "text": "You start heading through the trees. After a couple minutes you realize there's no end to the forest. You head back.",
                "score": -5,
            },
            "bushes": {
                "text": "You start moving through the nearby bushes, and after a while the forest starts clearing out a little bit. You arrive at a small lake.",
                "score": 4,
            },
        },
    },
    "stage2": {
        "description": "You look around the edge of the lake, nearby you can see a fishing rod and a small road leading around the lake. Do you want to test your luck and 'fish', or do you want to take the 'road'?",
        "choices": {
            "fish": {
                "text": "You pick up the fishing rod and throw the line out into the lake. \nYou look around the sky and appreciate the clouds and the sun for a bit. Suddenly you feel a pull on the rod, and you start reeling in. \nYou pull up a big sword! You decide to tie it onto your back with the fishing line before you head on.",
                "score": 10,
            },
            "road": {
                "text": "You start walking down the gravel road that leads around the lake. \nFor a fleeting moment, you wonder what you could've found in the lake. No time for that, though! \nYou keep your pace on the road, heading uphill the nearby mountain.",
                "score": 3,
            },
        },
    },
    "stage3": {
        "description": "After a long trip on the road leading along a small mountainside, you arrive at some sort of cave leading into the mountain. \nDo you wish to 'enter' and explore the cave, or 'continue' on the current road?",
        "choices": {
            "enter": {
                "text": "You enter the cave and find a huge troll staring into your soul. \nYou sense fear rushing through your entire body.",
                "score": 3,
            },
            "continue": {
                "text": "You decide to avoid the cave, you never know what could lurk inside. \nStealthily with a pop in your step, you rush past! And not a moment too soon, as you hear a roar behind you. \nScared, you run away as fast as you can.",
                "score": -5,
            },
        },
    },
    "stage4": {
        "description": "After the cave, you see a town at the base of the mountain. You're almost safe! \nYou have two options, you could try to 'slide' down the side to get down quick, or you can take the long winding 'road' down.",
        "choices": {
            "slide": {
                "text": "You set one foot into the gravel and push down. You start sliding down at breakneck speeds, \nat some point your foot starts slipping and you begin tumbling down. After what seems like an eternity, \nyou end up at the bottom. Safe, but very bruised.",
                "score": -15,
            },
            "road": {
                "text": "You decide to take the safe way down. The road snakes left and right in a spiral-like way, \nand it feels like an eternity passes by before you end up at the bottom. \nYou get down safe, although a little dehydrated.",
                "score": 5,
            },
        },
    },
}


def clear_screen():
    """
    Clears the console screen.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def game_start():
    """
    Will inititalize the game and will ask for the player's name before introducting the game.
    """
    if player_info["name"] == "":
        player_info["name"] = input("Hi!\nPlease input your name: ")
        print(
            f"Hello {player_info['name']}, welcome to the game!\nDuring your adventure you will be asked to give inputs.\nI will try to interpret what you want as well as I can, but please refrain from using both of the keywords in the same sentence.\n\nLet's begin!"
        )


def help(curr_stage: str):
    """Is used to print out valid keywords (choices) for the section the player is currently in.

    Args:
        curr_stage (str): The current screen/stage the player is in. Looks up based on indexing and variable "stage".
    """
    print("Valid inputs are:\n")
    for key in screens[curr_stage]["choices"].keys():
        print(key)
    print("\nYou can make a sentence with the word you wish to use.\n")
    choose_path(player_info["score"], stage)


def troll_fight(score: int) -> int:
    """An optional fight with a mountain troll. Will run based on if player has sword and is on the correct screen.

    Args:
        score (int): Takes the players' current score and updates it with +score from winning the fight.

    Returns:
        int: Returns the updated score from the fight.
    """
    print(
        "You pull the sword you fished up earlier from your back and go toe to toe with the huge troll snearing in your face."
    )
    print(
        "Against all odds you stand your ground. The troll swing wildly around itself for you while you dodge and weave underneath it and between its legs."
    )
    print(
        "After a long and arduous fight, you manage to cut its ankle and it falls to the ground."
    )
    print(
        "With determination in your eyes, you lift the sword high up into the air and thrust it into the trolls left eye as deep as you can."
    )
    print(
        "Blood spouts like a huge fountain all over the floor, and you emerge victorious."
    )
    print(
        "In the back of the trolls' cave, you find lots of riches and many interesting artifacts."
    )
    print("You take some trophies for yourself and head on your way.")

    return score + 25


def check_legal_input(choice: str, valid_choices: list, invalid: bool):
    """Error-checking for player input. If input does not exist as a keyword, it returns default variables to keep the loop running.
    Made to be called inside "choose_path" function.

    Args:
        choice (str): Whatever the uses gives as an input.
        valid_choices (list): Pulls from the "choices" section of the dictionary, based on whatever scene is currently in play.
        invalid (bool): The state of the input-loop. If it returns invalid == False, the loop will break and the game continues.

    Returns:
        invalid: If the function does not detect a valid choice, will return "True" to have the player give another input.
    """
    for key in valid_choices:
        if key in choice:
            choice = key
            invalid = False
            return choice, invalid
        else:
            clear_screen()
            print(
                'Invalid choice! Please try again with a different choice. Hint: Type "Help" if you\'d like to see the valid choices.\n'
            )
    return 1, True


def choose_path(score: int, stage: int) -> int:
    """Will ask the user for an input, what does the player want to do.

    Args:
        score (int): The current score of the player.
        stage (int): Looks up based on indexing in the dictionary, what stage is currently in play.

    Returns:
        int: Returns the score to be updated in the player_info stats.
    """
    invalid = True
    curr_stage = "stage" + str(stage)
    valid_choices = list(screens[curr_stage]["choices"].keys())

    while invalid == True:
        print(screens[curr_stage]["description"])
        choice = input("\nWhat do you want to do?\n\n").lower()

        clear_screen()

        if choice == "help":
            help(curr_stage)

        choice, invalid = check_legal_input(choice, valid_choices, invalid)

    if choice == "fish" and curr_stage == "stage2":
        player_info["sword"] = True

    clear_screen()

    print(screens[curr_stage]["choices"][choice]["text"])

    if (
        choice == "enter" and curr_stage == "stage3" and player_info["sword"] == True
    ):  # If the fight is triggered, print out the fight and add some points to the tally
        score = troll_fight(score)

    return score + screens[curr_stage]["choices"][choice]["score"]


while not game_over:
    game_start()
    player_info["score"] = choose_path(player_info["score"], stage)
    stage += 1
    if stage > len(screens):
        game_over = True

print(
    f"The game is over, {player_info['name']}. You reached stage {stage} and earned a score of {player_info['score']}."
)
print("Congratulations!")
input("Thanks for playing.")

