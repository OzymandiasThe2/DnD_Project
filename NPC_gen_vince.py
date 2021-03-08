from random import randint, choice


# TYPES
class race:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class RaceModifier:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect


class Race:
    def __init__(self, race_type, modifier=None):
        self.raceType = race_type
        self.modifier = modifier

    def __str__(self):
        if self.modifier is None:
            return self.raceType.name + "\n" + self.raceType.damage
        return self.raceType.name + " of " + self.modifier.name + "\n" + self.raceType.damage + "\n" + self.modifier.effect


# USER DEFINED MAIN STATS
race_categories = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']

strength_races = [
    race('Mountain Dwarf', '1d4, piercing'),
    race('Dragonborn (1H)', '1d6, piercing'),
    race('Duergar  (2H)', '2d6, 19-20 x2'),
    race('Zariel Tiefling (2H)', '2d4, x4'),
    race('Triton ', ''),
    race('Kobold ', ''),
    race('Githyanki ', ''),
    race('Longtooth Shifter', ''),
    race('Centaur ', ''),
    race('Half-Orc', ''),
    race('Human', ''),
    race('Fallen Aasimar ', ''),
    race('Goliath ', ''),
    race('Bugbear ', ''),
    race('Orc ', ''),
    race('Tortle ', ''),
    race('Juggernaut Warforged', ''),
    race('Minotaur ', '')
]
dexterity_races = [
    race('Elf ', ''),
    race('Halfling ', ''),
    race('Deep Gnome', ''),
    race('Glasya Tiefling', ''),
    race('Kenku ', ''),
    race('Goblin ', ''),
    race('Kobold ', ''),
    race('Changeling ', ''),
    race('Swiftstride Shifter', ''),
    race('Forest Gnome', ''),
    race('Human ', ''),
    race('Dispater Tiefling', ''),
    race('Feral Tiefling', ''),
    race('Tabaxi', ''),
    race('Bugbear ', ''),
    race('Grung ', ''),
    race('Shifter  ', ''),
    race('Skirmisher Warforged ', '')
]
constitution_races = [
    race('Dwarf ', ''),
    race('Stout halfling', ''),
    race('Rock Gnome', ''),
    race('Abyssal Tiefling', ''),
    race('Scourge Aasimar', ''),
    race('Lizardfolk ', ''),
    race('Hobgoblin ', ''),
    race('Orc ', ''),
    race('Beasthide Shifter', ''),
    race('Minotaur ', ''),
    race('Half-orc', ''),
    race('Human ', ''),
    race('Sea-Elf', ''),
    race('Levistus Tiefling', ''),
    race('Goliath ', ''),
    race('Triton ', ''),
    race('Goblin ', ''),
    race('Grung ', ''),
    race('Warforged ', '')
]
intelligence_races = [
    race('High-Elf', ''),
    race('Human', ''),
    race('Baalzebul Tiefling', ''),
    race('Naiad Nymph', ''),
    race('Hobgoblin', ''),
    race('Githyanki', ''),
    race('Changeling', ''),
    race('Gnome', ''),
    race('Infernal Tiefling', ''),
    race('Mammon Tiefling', ''),
    race('Feral Tiefling', ''),
    race('Orc', ''),
    race('Githzerai', ''),
    race('Mephistopheles Tiefling', '')
]
wisdom_races = [
    race('Wood elf', ''),
    race('Human', ''),
    race('Fierna Tiefling', ''),
    race('Firbolg ', ''),
    race('Lizardfolk ', ''),
    race('Tortle ', ''),
    race('Centaur ', ''),
    race('Hill dwarf', ''),
    race('Ghostwise Halfling', ''),
    race('Protector Aasimar', ''),
    race('Kenku ', ''),
    race('Githzerai ', ''),
    race('Kalashtar ', '')
]
charisma_races = [
    race('Half-elf', ''),
    race('Human', ''),
    race('Lightfoot halfling', ''),
    race('Aasimar ', ''),
    race('Triton ', ''),
    race('Changeling ', ''),
    race('Swiftstride Shifter', ''),
    race('Dragonborn ', ''),
    race('Drow ', ''),
    race('Eladrin ', ''),
    race('Tabaxi ', ''),
    race('Yuan-ti Pureblood', ''),
    race('Kalashtar ', '')
]

race_types_by_category = {
    "Strength": strength_races,
    "Dexterity": dexterity_races,
    "Constitution": constitution_races,
    "Intelligence": intelligence_races,
    "Wisdom": wisdom_races,
    "Charisma": charisma_races
}

# USER DEFINED MODIFIERS
magicModifiers = [
    RaceModifier('powerful Strength', 'Increase strength by +3'),
    RaceModifier('powerful Dexterity', 'Increase dexterity by +3'),
    RaceModifier('powerful Constitution', 'Increase constitution by +3'),
    RaceModifier('powerful Intelligence', 'Increase intelligence by +3'),
    RaceModifier('powerful Wisdom', 'Increase wisdom by +3'),
    RaceModifier('powerful Charisma', 'Increase charisma by +3')]

basicModifiers = [
    RaceModifier('Strength', 'Increase Strength by +2'),
    RaceModifier('the Evil Slaughter', 'basic attacks deal +2d6 damage to Evil targets'),
    RaceModifier('Detect Good', 'grants the wielder the ability to Detect Good'),
    RaceModifier('Freezing', '25% chance of freezing an enemy for one round'),
    RaceModifier('Lockpicking', 'once per day, the wielder can pick a lock he wants for free'),
    RaceModifier('Invisibility', 'grants invisibility to the wielder 1 minute per day'),
    RaceModifier('the Humanoid Slayer', 'basic attacks deal +3d6 to humanoid targets'),
    RaceModifier('Detect Magic', 'once a day, grants the wielder a successful action of Detect Magic'),
    RaceModifier('Light', 'creates light in a circular region around the wielder with range 9m'),
    RaceModifier('strong Reflexes', 'The wielder gets a bonus of +3 to his Reflexes saving throw'),
    RaceModifier('strong Fortitude', 'The wielder gets a bonus of +3 to his Fortitude saving throw'),
    RaceModifier('strong Will', 'The wielder gets a bonus of +3 to his Will saving throw'),
    RaceModifier('Dexterity', 'increase dexterity of +2'),
    RaceModifier('Revelation', 'once per day, reveals to the wielder the position of all the enemies in a room')]


# etc... add your own

# FUNCTIONS
def generate_random_race_type():
    category = choice(race_categories)
    return choice(race_types_by_category[category])


def generate_random_race_modifier():
    if randint(0, 2) == 0:
        return None  # 50% chance of no modifier
    if randint(0, 99) == 0:
        return choice(magicModifiers)  # 1/100 chance
    return choice(basicModifiers)


def generate_random_race():
    return Race(generate_random_race_type(), generate_random_race_modifier())


print(generate_random_race())
