from random import randint, choice, randrange

from NPC_gen import generateNPC
from dice_gen import DiceRoll, diceDetails
from monster_gen import monsterDetails
from name_gen import Names, nameDetails
from stat_gen import RanStats, InputStats, statDetails
from weapon_gen import RandWeapon, weaponDetails
from weapon_genV2 import printWeaponsGen
from weapons_vince_edit import generateRandomWeapon



def main():
    def clear(arr):
        for x in arr:
            x.reset()


while True:
    print("Welcome brave adventure.\nWhat is your request?")
    print("[1] Dice Rolls\n[2] Stat Gen\n[3] Name Gen\n[4] Monster Gen\n[5] Loot Gen\n[6] NPC Gen\n[0] Exit")
    try:
        selector = int(input("Enter a number for what you want: "))
        if selector == 0 or selector is None:
            print("Goodbye")
            break
        if selector == 1:
            diceDetails()
        elif selector == 2:
            statDetails()
        elif selector == 3:
            nameDetails()
        elif selector == 4:
            monsterDetails()
        elif selector == 5:
            print(generateRandomWeapon())
            # weaponDetails()
        elif selector >= 6:
            print(generateNPC())
    except ValueError or IndexError:
        print("Goodbye")
        break

    if __name__ == "__main__":
        main()
