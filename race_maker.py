from random import choices, choice


class FixedStatBonus:
    def __init__(self, bonuses):
        self.bonuses = bonuses

    def updateStats(self, stats):
        for x in self.bonuses:
            stats[x] += self.bonuses[x]
        return stats


class RandomStatBonus:
    def __init__(self, statChoices, bonusAmount, repititions):
        self.statChoices = statChoices
        self.bonusAmount = bonusAmount
        self.repititions = repititions

    def updateStats(self, stats):
        for _ in range(self.repititions):
            stats[choice(self.statChoices)] += self.bonusAmount
        return stats


class TosculiBonus:
    def __init__(self):
        self.bonusStats = ["str", "dex", "con", "int", "wis", "cha"]
        self.negativeStats = ["int", "wis", "cha"]

    def updateStats(self, stats):
        statChoice = choice(self.bonusStats)
        stats[statChoice] += 2
        if (statChoice in self.negativeStats):
            stats[choice(self.bonusStats)] -= 2
        return stats


# bonus data goes here
bonuses_by_race = {
    "human": [FixedStatBonus({"str": 2, "dex": 1}), RandomStatBonus(["int", "wis"], 1, 1)],
    "orc": [FixedStatBonus({"str": 5, "int": 1})],
    "archer": [FixedStatBonus({"str": 3, "int": 2}), RandomStatBonus(["int", "wis", "dex"], 2, 2)]
}

statBase = {}
statTypeValue = []
statTypeKey = ["str", "dex", "con", "int", "wis", "cha"]
for x in statTypeKey:
    D6_Roll = [1, 2, 3, 4, 5, 6]  # represents a D6
    D6_Roll = choices(D6_Roll, k=4)  # pick a number from a D6, four times, into a list
    print(x, "=", D6_Roll)
    D6_Roll.remove(min(D6_Roll))  # remove the lowest number from rolls(list)
    print(x, "=", D6_Roll)
    listSum = sum(D6_Roll)  # add up remaining three dice rolls
    # TODO make a pity roll if you get only 1s
    print(x, "=", listSum)
    print("--------------------")
    statTypeValue.append(listSum)  # adds each sum to a list
print(statTypeValue)  # total for each Stat Type
for key in statTypeKey:  # create a complete character stat roll
    for value in statTypeValue:
        statBase[key] = value
        statTypeValue.remove(value)
        break
characterBase = statBase
print(characterBase)
print("Base character stats are: " + str(characterBase))
print("====================")

# base stats
try:
    stats = characterBase
except Exception:
    stats = {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 0, "cha": 0}
# print(stats)

# can be randomly generated
raceList = list(bonuses_by_race.keys())
getRace = choice(raceList)

raceName = getRace

# apply all bonuses from the race
for bonus in bonuses_by_race[raceName]:
    stats = bonus.updateStats(stats)

print(raceName, stats)

print("===========================================================================")
