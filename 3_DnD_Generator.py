from random import randint, choice, randrange

from dice_gen import DiceRoll, dice_details
from monster_gen import monster_details
from name_gen import Names, name_details
from stat_gen import RanStats, InputStats, statDetails
from weapon_gen import generate_random_weapon
from NPC_gen_vince import generate_random_race

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
            dice_details()
        elif selector == 2:
            statDetails()
        elif selector == 3:
            name_details()
        elif selector == 4:
            monster_details()
        elif selector == 5:
            print(generate_random_weapon())
            # weaponDetails()
        elif selector >= 6:
            print(generate_random_race())
    except ValueError or IndexError:
        print("Goodbye")
        break

    if __name__ == "__main__":
        main()
