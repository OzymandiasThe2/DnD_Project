from random import randint, choice, randrange


def diceDetails(): # prints user selection
    dice = []
    numberDie = int(input("Amount of dice being rolled: "))
    # sides = int(input("Amount of sides on the dice: "))
    for x in range(numberDie):
        dice.append(DiceRoll())
    for x in dice:
        x.setSides(int(input("Amount of sides on dice: ")))
        x.randRoll()
    for x in dice:
        print(x.getRoll())


class DiceRoll:
    # Type of die to roll #
    def __init__(self):
        self._roll = 0
        self._amount = 0

    def setSides(self, amount):
        self._amount = amount

    def randRoll(self):
        self._roll = randint(1, self._amount)
        return self._roll

    def getRoll(self):
        return self._roll

    def reset(self):
        self._roll = 0

