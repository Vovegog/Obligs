# def print_pairs ( n : int ) -> None :
#     for i in range(0, n+1, 2) :
#         print(i)

# print_pairs(12)

# an_letters = "aefhilmnorsxAEFHILMNORSX"
# word = input("I will cheer for you! Enter your name: ")
# for c in word:
#     if c in an_letters:
#         print("Give me an " + c + "! " + c)
#     else:
#         print("Give me a " + c + "! " + c)
# print(word * 3 + "!!!")


def prime(n: int) -> bool:
    """
    Returns True if and only if n is a prime number.
    Restriction: n>0
    """
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
    return is_prime


# print(prime(1546783))


def is_x_larger(n: int) -> int:
    counter = 0
    for i in range(n):
        x = (1001 + i * 58513) % 4
        if x > 2:
            counter = counter + 1
    return counter


# print(is_x_larger(200))


def does_it_print() -> None:
    s1 = "Høgskolen"
    s2 = "i Molde  "
    if len(s1) == len(s2):
        for char1 in s1:
            for char2 in s2:
                if char1 == char2:
                    print(char1 + " is a common letter")


# does_it_print()


def max_val(lst: list) -> float:
    """
    Computes largest value in a list of at least 1 element
    """
    max_so_far = 0
    for num in lst[1:]:
        if num > max_so_far:
            max_so_far = num
    return max_so_far


# print(max_val([1,2,6,4,89,76,56]))


def mult(lst: list) -> None:
    """
    Multiplies the elements in lst by 2
    """
    for i in range(len(lst)):
        lst[i] = lst[i] * 2
    print(lst)


# mult([2,4,6,8,10])


def mathias(lst: list) -> list:
    while len(lst) > 1:
        if lst[1] > lst[0]:
            lst[0] = lst.pop(1)
        else:
            lst.pop(1)
        print(lst)
    return lst[0]


# print(mathias([1,4,10,6]))
# print(max([1,5,4,2,10,25]))

# lst = ["IBE152", "IBE500", "IBE600", "IBE321"]

# def courses_you_will_teach ( lst : list ) -> list :
#     for course in range(len(lst)) :
#         lst.pop(0)
#     print(lst)

# courses_you_will_teach(lst)


lst = [1, 23, 4, 5, 787]


def max_min(lst: list) -> None:
    størst = lst[0]
    minst = lst[0]
    for num in lst:
        if lst[0] * num > størst:
            størst = lst[0] * num
        elif lst[0] * num < minst:
            minst = lst[0] * num
    print(størst)
    print(minst)


# max_min(lst)


def palindrom(text: str) -> bool:
    for i in range(len(text) // 2):
        if len(text) == 1:
            return True
        if text[0] != text[-1]:
            return False
        text = text[1:-1]
        print(text)
    return True


# palindrom("racecar")


def even_numbers(lst: list) -> list:
    index = []
    for num in lst:
        if num % 2 == 0:
            index.append(lst.index(num))
    if index == []:
        return -1
    return index


# print(even_numbers([1,5,7,13,3,11,9]))


def new_number_list(lst: list) -> list:
    new_list = []
    for n in lst:
        if n > 200:
            break
        if n % 5 == 0 and n <= 100:
            new_list.append(n)
    return new_list


# print(new_number_list([1,5,10,20,80,99,100,150,230,50]))


def reverse(ord: str) -> str:
    nytt_ord = ""
    for i in range(len(ord)):
        lengde = len(ord)
        nytt_ord = nytt_ord + ord[lengde - 1]
        ord = ord[:-1]
    return nytt_ord


# print(reverse("dame"))


def even_odd(lst: list) -> str:
    partall = 0
    oddetall = 0
    for i in lst:
        if i % 2 == 0:
            partall += 1
        else:
            oddetall += 1
    return "Partall: " + str(partall) + " - Oddetall: " + str(oddetall)


# print(even_odd([1,2,3,4,5,6,7,8,9,10]))

lst = [["Bjarne", 56, 2], ["Kalle", 76, 1], ["Agnes", 90, 0]]


def arv(lst: list) -> list:
    arver = ["Samfunnet", 0, 0]
    for i in lst:
        alder = i[1]
        barn = i[2]
        if barn > 0 and alder > arver[1]:
            arver = i
    return arver


# print(arv(lst))


list1 = []
list2 = [[1, 2], [3, 4], [5, 6]]


def listetull(list1: list, list2: list) -> None:
    list1.append(list2[1])
    list1.append(list2[0])
    print(list1)


listetull(list1, list2)
