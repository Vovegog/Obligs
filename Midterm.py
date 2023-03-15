# Midtermeksamen 3.3.23

# Daniel Viggen

# 1


def eggs_to_market(N: int, lst: list) -> int:
    """Will calculate how many kg's of Gold the farmer can trade his eggs for.
    If input is less than the lowest amount allowed, will return 0.
    If eggs are lower than minimum of horses available OR higher than maximum of horses available, will automatically return 0.
    (The sentence above refer to problem, "their current number must be between M1 and M2 to take the horses, or none will survive.").
    Will also return 0 if eggs at the end is lower than 3, and thus can't be traded for any Gold.

    Args:
        N (int): Amount of eggs you ship in the truck to the market.
        lst (list): List of arguments for allowed minimum/maximum eggs on the truck, eggs surviving in the water, and min/max of eggs allowed on the horses.

    Returns:
        int: Amount of Gold in kg's that you gain.
    """
    h1 = lst[0]
    h2 = lst[1]
    k = lst[2]
    m1 = lst[3]
    m2 = lst[4]

    if N < h1:
        return 0
    elif N > h2:
        N = h2
    if N > k:
        N = k
    if m1 < N < m2:
        return N // 3
    else:
        return 0


# print(eggs_to_market(19, [10, 14, 4, 5, 6]))
# print(eggs_to_market(100, [10,14, 4, 5, 16]))
# print(eggs_to_market(100, [10,14, 4, 0, 16]))


# 2


def catering(guests: int) -> list:
    """Calculates the amount of cake and champagne needed for the guests.

    Args:
        guests (int): The amount of guests at the party. Must be positive.

    Returns:
        list: The list will returned as [cakes, champagne] needed to serve all the guests.
    """
    if guests == 0:
        cakes = 0
    elif 0 < guests <= 6:
        cakes = 1
    else:
        if guests % 6 == 0:
            cakes = guests // 6
        else:
            cakes = guests // 6 + 1
    if guests == 0:
        champagne = 0
    elif 1 < guests <= 5:
        champagne = 1
    else:
        if guests % 5 == 0:
            champagne = guests // 5
        else:
            champagne = guests // 5 + 1
    return [cakes, champagne]


# print(catering(0))


# 3


def insert_str(word: str, ins_string: str, pos: int) -> str:
    """Will let you insert a word at the desired position in a string.

    Args:
        word (str): The word you start with. For the assignments purposes, write "Here".
        ins_string (str): The word you want to insert into the string.
        pos (int): The position you want to insert the word into the string.

    Returns:
        str: A string containing the words you've put in.
    """
    target = word
    ins_string = ins_string
    pos = int(pos)
    if not target.endswith(" "):
        target = target + " "
    target = target[: pos + 1] + ins_string
    print("Word so far: " + target)
    ins_string = input("What's the next word: ")
    pos = int(input("What's the desired position for the word: "))
    if not target.endswith(" "):
        target = target + " "
    target = target[: pos + 1] + ins_string + " " + target[-pos:]
    print("Word so far: " + target)
    ins_string = input("What's the next word: ")
    pos = int(input("What's the desired position for the word: "))
    if not target.endswith(" "):
        target = target + " "
    target = target[: pos + 1] + ins_string + target[: -pos - 1]

    return target


print(insert_str("Here", "the", 4))  # To initalize the function


# 4


def day_of_month_lights(day: int) -> list:
    """Gives a list of strings for use in a 7-segment display.

    Args:
        day (int): The day of the month (1-31) that you want to display.

    Returns:
        list: A list containing two strings to light up a 2-digit date display.
    """
    lights = []
    number_list = [
        "1111110",  # 0
        "1100000",  # 1
        "1011011",  # 2
        "1110011",  # 3
        "1100101",  # 4
        "0110111",  # 5
        "0111111",  # 6
        "1100010",  # 7
        "1111111",  # 8
        "1110111",  # 9
    ]

    if day < 10:
        numbers = "0" + str(day)
    else:
        numbers = str(day)

    lights.append(number_list[int(numbers[:1])])
    lights.append(number_list[int(numbers[1:2])])

    return lights


# print(day_of_month_lights(7))
