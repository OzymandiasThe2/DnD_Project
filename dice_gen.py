from random import randint


def dice_details():  # prints user selection
    dice = []
    number_of_die = int(input("Amount of dice being rolled: "))
    # sides = int(input("Amount of sides on the dice: "))
    for x in range(number_of_die):
        dice.append(DiceRoll())
    for x in dice:
        x.set_sides(int(input("Amount of sides on dice: ")))
        x.randomize_roll()
    for x in dice:
        print(x.get_roll())


class DiceRoll:
    # Type of die to roll #
    def __init__(self):
        self._roll = 0
        self._amount = 0

    def set_sides(self, amount):
        self._amount = amount

    def randomize_roll(self):
        self._roll = randint(1, self._amount)
        return self._roll

    def get_roll(self):
        return self._roll

    def reset(self):
        self._roll = 0
