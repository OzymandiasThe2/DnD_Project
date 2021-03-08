from random import randint, choice, randrange, choices


def statDetails():
    print("[1] Pre-determined stats\n[2] Generate random stats")
    selector = int(input("Enter a number for what you want: "))
    if selector == 1:
        print("Please input stats to that are pre-determined: ")
        InputStats()
    else:
        print("Here are statblocks to use, remove the lowest number from each of the blocks and the sum is your base "
              "stat: ")
        RanStats()

        print("Still testing\nGoodbye")


"""Stat Generation"""
stats = {'STR': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
         'DEX': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
         'CON': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
         'WIS': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
         'INT': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
         'CHA': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]}


def RanStats():
    statBase = {}
    statTypeValue = []
    statTypeKey = ["str", "dex", "con", "int", "wis", "cha"]
    for x in statTypeKey:
        list = [1, 2, 3, 4, 5, 6]  # represents a D6
        list = choices(list, k=4)  # pick numbers between 1-6, four times, into a list
        print(x, "=", list)
        list.remove(min(list))  # remove the lowest number from rolls(list)
        print(x, "=", list)
        listSum = sum(list)  # add up remaining three dice rolls
        # TODO make a pity counter if you get only 1s
        print(x, "=", listSum)
        print("--------------------")
        statTypeValue.append(listSum)   # adds each sum to a list
    print(statTypeValue)    # total for each Stat Type
    for key in statTypeKey:     # create a complete character stat roll
        for value in statTypeValue:
            statBase[key] = value
            statTypeValue.remove(value)
            break
    characterBase = statBase.copy()
    print(characterBase)
    print("Base character stats are: " + str(characterBase))
    print("====================")


def InputStats():
    temp_STR = input("What is your STR: ")
    temp_DEX = input("What is your DEX: ")
    temp_CON = input("What is your CON: ")
    temp_WIS = input("What is your WIS: ")
    temp_INT = input("What is your INT: ")
    temp_CHA = input("What is your CHA: ")

    stats['STR'] = temp_STR
    stats['DEX'] = temp_DEX
    stats['CON'] = temp_CON
    stats['WIS'] = temp_WIS
    stats['INT'] = temp_INT
    stats['CHA'] = temp_CHA

    print("STR:" + str(temp_STR),
          "DEX:" + str(temp_DEX),
          "CON:" + str(temp_CON),
          "WIS:" + str(temp_WIS),
          "INT:" + str(temp_INT),
          "CHA:" + str(temp_CHA))


# statDetails()


