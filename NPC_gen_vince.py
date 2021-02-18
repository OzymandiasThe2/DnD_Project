from random import randint, choice


# TODO: Thank your local Vincent for cleaning up the nightmare field of IF conditions

# TYPES
class RaceType:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class RaceModifier:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect


class Race:
    def __init__(self, raceType, modifier=None):
        self.raceType = raceType
        self.modifier = modifier

    def __str__(self):
        if (self.modifier == None):
            return self.raceType.name + "\n" + self.raceType.damage
        return self.raceType.name + " of " + self.modifier.name + "\n" + self.raceType.damage + "\n" + self.modifier.effect


# USER DEFINED WEAPONS
raceCategories = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']

strengthRaces = [
    RaceType('Mountain Dwarf', '1d4, piercing'),
    RaceType('Dragonborn (1H)', '1d6, piercing'),
    RaceType('Duergar  (2H)', '2d6, 19-20 x2'),
    RaceType('Zariel Tiefling (2H)', '2d4, x4'),
    RaceType('Triton ', ''),
    RaceType('Kobold ', ''),
    RaceType('Githyanki ', ''),
    RaceType('Longtooth Shifter', ''),
    RaceType('Centaur ', ''),
    RaceType('Half-Orc', ''),
    RaceType('Human', ''),
    RaceType('Fallen Aasimar ', ''),
    RaceType('Goliath ', ''),
    RaceType('Bugbear ', ''),
    RaceType('Orc ', ''),
    RaceType('Tortle ', ''),
    RaceType('Juggernaut Warforged', ''),
    RaceType('Minotaur ', '')
]
dexterityRaces = [
    RaceType('Elf ', ''),
    RaceType('Halfling ', ''),
    RaceType('Deep Gnome', ''),
    RaceType('Glasya Tiefling', ''),
    RaceType('Kenku ', ''),
    RaceType('Goblin ', ''),
    RaceType('Kobold ', ''),
    RaceType('Changeling ', ''),
    RaceType('Swiftstride Shifter', ''),
    RaceType('Forest Gnome', ''),
    RaceType('Human ', ''),
    RaceType('Dispater Tiefling', ''),
    RaceType('Feral Tiefling', ''),
    RaceType('Tabaxi', ''),
    RaceType('Bugbear ', ''),
    RaceType('Grung ', ''),
    RaceType('Shifter  ', ''),
    RaceType('Skirmisher Warforged ', '')
]
constitutionRaces = [
    RaceType('Dwarf ', ''),
    RaceType('Stout halfling', ''),
    RaceType('Rock Gnome', ''),
    RaceType('Abyssal Tiefling', ''),
    RaceType('Scourge Aasimar', ''),
    RaceType('Lizardfolk ', ''),
    RaceType('Hobgoblin ', ''),
    RaceType('Orc ', ''),
    RaceType('Beasthide Shifter', ''),
    RaceType('Minotaur ', ''),
    RaceType('Half-orc', ''),
    RaceType('Human ', ''),
    RaceType('Sea-Elf', ''),
    RaceType('Levistus Tiefling', ''),
    RaceType('Goliath ', ''),
    RaceType('Triton ', ''),
    RaceType('Goblin ', ''),
    RaceType('Grung ', ''),
    RaceType('Warforged ', '')
]
intelligenceRaces = [
    RaceType('High-Elf', ''),
    RaceType('Human', ''),
    RaceType('Baalzebul Tiefling', ''),
    RaceType('Naiad Nymph', ''),
    RaceType('Hobgoblin', ''),
    RaceType('Githyanki', ''),
    RaceType('Changeling', ''),
    RaceType('Gnome', ''),
    RaceType('Infernal Tiefling', ''),
    RaceType('Mammon Tiefling', ''),
    RaceType('Feral Tiefling', ''),
    RaceType('Orc', ''),
    RaceType('Githzerai', ''),
    RaceType('Mephistopheles Tiefling', '')
]
wisdomRaces = [
    RaceType('Wood elf', ''),
    RaceType('Human', ''),
    RaceType('Fierna Tiefling', ''),
    RaceType('Firbolg ', ''),
    RaceType('Lizardfolk ', ''),
    RaceType('Tortle ', ''),
    RaceType('Centaur ', ''),
    RaceType('Hill dwarf', ''),
    RaceType('Ghostwise Halfling', ''),
    RaceType('Protector Aasimar', ''),
    RaceType('Kenku ', ''),
    RaceType('Githzerai ', ''),
    RaceType('Kalashtar ', '')
]
charismaRaces = [
    RaceType('Half-elf', ''),
    RaceType('Human', ''),
    RaceType('Lightfoot halfling', ''),
    RaceType('Aasimar ', ''),
    RaceType('Triton ', ''),
    RaceType('Changeling ', ''),
    RaceType('Swiftstride Shifter', ''),
    RaceType('Dragonborn ', ''),
    RaceType('Drow ', ''),
    RaceType('Eladrin ', ''),
    RaceType('Tabaxi ', ''),
    RaceType('Yuan-ti Pureblood', ''),
    RaceType('Kalashtar ', '')
]


raceTypesByCategory = {
    "Strength": strengthRaces,
    "Dexterity": dexterityRaces,
    "Constitution": constitutionRaces,
    "Intelligence": intelligenceRaces,
    "Wisdom": wisdomRaces,
    "Charisma": charismaRaces
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
def generateRandomRaceType():
    category = choice(raceCategories)
    return choice(raceTypesByCategory[category])


def generateRandomRaceModifier():
    if (randint(0, 2) == 0): return None  # 50% chance of no modifier
    if (randint(0, 99) == 0): return choice(magicModifiers)  # 1/100 chance
    return choice(basicModifiers)


def generateRandomRace():
    return Race(generateRandomRaceType(), generateRandomRaceModifier())


print(generateRandomRace())
