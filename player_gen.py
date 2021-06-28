from random import choices, choice


class FixedStatBonus:
    def __init__(self, bonuses):
        self.bonuses = bonuses

    def update_stats(self, stats):
        for base_stat in self.bonuses:
            stats[base_stat] += self.bonuses[base_stat]
        return stats


class RandomStatBonus:
    def __init__(self, stat_choices, bonus_amount, repetitions):
        self.stat_choices = stat_choices
        self.bonus_amount = bonus_amount
        self.repetitions = repetitions

    def update_stats(self, stats):
        for _ in range(self.repetitions):
            stats[choice(self.stat_choices)] += self.bonus_amount
        return stats


# Edge case class for the Tosculi race, really weird

class TosculiBonus:
    def __init__(self):
        self.bonus_stats = ["str", "dex", "con", "int", "wis", "cha"]
        self.negative_stats = ["int", "wis", "cha"]

    def update_stats(self, stats):
        stat_choice = choice(self.bonus_stats)
        stats[stat_choice] += 2
        if stat_choice in self.negative_stats:
            stats[choice(self.bonus_stats)] -= 2
        return stats


# TODO: Make the following code into proper code structures

# bonus data goes here
# way too many race data that I would have to 'manually' put in, no way am I doing that
# using three different cases for test purposes
# Case 1: Human is just a random stat disribution
# Case 2: Orc is spefic stat distribution
# Case 3: Archer isn't actually a race, its a class
# TODO: might implement a proper database structure system

bonuses_by_race = {
    "Human": [FixedStatBonus({"str": 2, "dex": 1}), RandomStatBonus(["int", "wis"], 1, 1)],
    "Orc": [FixedStatBonus({"str": 5, "int": 1})],
    "Tosculi": TosculiBonus,
    "Archer": [FixedStatBonus({"str": 3, "int": 2}), RandomStatBonus(["int", "wis", "dex"], 2, 2)]
}


def final_ran_stats():
    # Most of the print lines are just for debugging
    stat_base = {}
    stat_type_value = []
    stat_type_key = ["str", "dex", "con", "int", "wis", "cha"]
    for stat in stat_type_key:
        d6_roll = [1, 2, 3, 4, 5, 6]  # represents a D6 (6-sided die)
        d6_roll = choices(d6_roll, k=4)  # pick a number from a D6, four times, into a list
        print(stat, "=", d6_roll)  # DEBUG Line: prints the numbers of the 4 dice
        d6_roll.remove(min(d6_roll))  # remove the lowest number from rolls(list)
        print(stat, "=", d6_roll)  # DEBUG Line: prints the updated dice list
        list_sum_of_dice = sum(d6_roll)  # add up remaining three dice rolls
        # TODO: make a pity roll if you get only 1s
        print(stat, "=", list_sum_of_dice)  # DEBUG Line: prints the added sum of all remaining dice
        print("--------------------")
        stat_type_value.append(list_sum_of_dice)  # adds each sum to a list
    print(stat_type_value)  # DEBUG Line: prints total for each Stat Type

    for key in stat_type_key:  # create a complete character stat roll
        for value in stat_type_value:
            stat_base[key] = value
            stat_type_value.remove(value)
            break
    character_base_stats = stat_base  # Base stats of the generated character
    print("Base character stats are: " + str(character_base_stats))
    print("====================")

    # TODO: Display stat modifiers
    # base stats
    try:
        stats = character_base_stats
    except Exception:  # If any error occurs during generation the stats become 0
        print("An error occurred during generation")
        stats = {"str": 0, "dex": 0, "con": 0, "int": 0, "wis": 0, "cha": 0}
        print(stats)

    # FINAL Stuff for race
    # Apply all bonuses from the race
    race_name = choice(list(bonuses_by_race.keys()))
    for bonus in bonuses_by_race[race_name]:
        stats = bonus.update_stats(stats)

    print(race_name, stats)
    s = ''.join(str(stats))
    # Probably a pythonic way to do this better, maybe for loop?
    s = s.replace('{', "")  # Remove list fluff
    s = s.replace('}', "")  # Remove list fluff
    s = s.replace("'", "")  # Remove list fluff
    print("Race is:", race_name, "\n Stats are: ", s)


