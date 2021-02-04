from random import randint, choice


# TODO: Thank your local Vincent for cleaning up the nightmare field of IF conditions

# TYPES
class raceType():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class raceModifier():
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect


class Race():
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
    raceType('Mountain Dwarf', '1d4, piercing'),
    raceType('Dragonborn (1H)', '1d6, piercing'),
    raceType('Duergar  (2H)', '2d6, 19-20 x2'),
    raceType('Zariel Tiefling (2H)', '2d4, x4'),
    raceType('Triton ', ''),
    raceType('Kobold ', ''),
    raceType('Githyanki ', ''),
    raceType('Longtooth Shifter', ''),
    raceType('Centaur ', ''),
    raceType('Half-Orc', ''),
    raceType('Human', ''),
    raceType('Fallen Aasimar ', ''),
    raceType('Goliath ', ''),
    raceType('Bugbear ', ''),
    raceType('Orc ', ''),
    raceType('Tortle ', ''),
    raceType('Juggernaut Warforged', ''),
    raceType('Minotaur ', '')
]
dexterityRaces = [
    raceType('Elf ', ''),
    raceType('Halfling ', ''),
    raceType('Deep Gnome', ''),
    raceType('Glasya Tiefling', ''),
    raceType('Kenku ', ''),
    raceType('Goblin ', ''),
    raceType('Kobold ', ''),
    raceType('Changeling ', ''),
    raceType('Swiftstride Shifter', ''),
    raceType('Forest Gnome', ''),
    raceType('Human ', ''),
    raceType('Dispater Tiefling', ''),
    raceType('Feral Tiefling', ''),
    raceType('Tabaxi', ''),
    raceType('Bugbear ', ''),
    raceType('Grung ', ''),
    raceType('Shifter  ', ''),
    raceType('Skirmisher Warforged ', '')
]
constitutionRaces = [
    raceType('Dwarf ', ''),
    raceType('Stout halfling', ''),
    raceType('Rock Gnome', ''),
    raceType('Abyssal Tiefling', ''),
    raceType('Scourge Aasimar', ''),
    raceType('Lizardfolk ', ''),
    raceType('Hobgoblin ', ''),
    raceType('Orc ', ''),
    raceType('Beasthide Shifter', ''),
    raceType('Minotaur ', ''),
    raceType('Half-orc', ''),
    raceType('Human ', ''),
    raceType('Sea-Elf', ''),
    raceType('Levistus Tiefling', ''),
    raceType('Goliath ', ''),
    raceType('Triton ', ''),
    raceType('Goblin ', ''),
    raceType('Grung ', ''),
    raceType('Warforged ', '')
]
intelligenceRaces = [
    raceType('High-Elf', ''),
    raceType('Human', ''),
    raceType('Baalzebul Tiefling', ''),
    raceType('Naiad Nymph', ''),
    raceType('Hobgoblin', ''),
    raceType('Githyanki', ''),
    raceType('Changeling', ''),
    raceType('Gnome', ''),
    raceType('Infernal Tiefling', ''),
    raceType('Mammon Tiefling', ''),
    raceType('Feral Tiefling', ''),
    raceType('Orc', ''),
    raceType('Githzerai', ''),
    raceType('Mephistopheles Tiefling', '')
]
wisdomRaces = [
    raceType('Wood elf', ''),
    raceType('Human', ''),
    raceType('Fierna Tiefling', ''),
    raceType('Firbolg ', ''),
    raceType('Lizardfolk ', ''),
    raceType('Tortle ', ''),
    raceType('Centaur ', ''),
    raceType('Hill dwarf', ''),
    raceType('Ghostwise Halfling', ''),
    raceType('Protector Aasimar', ''),
    raceType('Kenku ', ''),
    raceType('Githzerai ', ''),
    raceType('Kalashtar ', '')
]
charismaRaces = [
    raceType('Half-elf', ''),
    raceType('Human', ''),
    raceType('Lightfoot halfling', ''),
    raceType('Aasimar ', ''),
    raceType('Triton ', ''),
    raceType('Changeling ', ''),
    raceType('Swiftstride Shifter', ''),
    raceType('Dragonborn ', ''),
    raceType('Drow ', ''),
    raceType('Eladrin ', ''),
    raceType('Tabaxi ', ''),
    raceType('Yuan-ti Pureblood', ''),
    raceType('Kalashtar ', '')
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
    raceModifier('powerful Strength', 'Increase strength by +3'),
    raceModifier('powerful Dexterity', 'Increase dexterity by +3'),
    raceModifier('powerful Constitution', 'Increase constitution by +3'),
    raceModifier('powerful Intelligence', 'Increase intelligence by +3'),
    raceModifier('powerful Wisdom', 'Increase wisdom by +3'),
    raceModifier('powerful Charisma', 'Increase charisma by +3')]

basicModifiers = [
    raceModifier('Strength', 'Increase Strength by +2'),
    raceModifier('the Evil Slaughter', 'basic attacks deal +2d6 damage to Evil targets'),
    raceModifier('Detect Good', 'grants the wielder the ability to Detect Good'),
    raceModifier('Freezing', '25% chance of freezing an enemy for one round'),
    raceModifier('Lockpicking', 'once per day, the wielder can pick a lock he wants for free'),
    raceModifier('Invisibility', 'grants invisibility to the wielder 1 minute per day'),
    raceModifier('the Humanoid Slayer', 'basic attacks deal +3d6 to humanoid targets'),
    raceModifier('Detect Magic', 'once a day, grants the wielder a successful action of Detect Magic'),
    raceModifier('Light', 'creates light in a circular region around the wielder with range 9m'),
    raceModifier('strong Reflexes', 'The wielder gets a bonus of +3 to his Reflexes saving throw'),
    raceModifier('strong Fortitude', 'The wielder gets a bonus of +3 to his Fortitude saving throw'),
    raceModifier('strong Will', 'The wielder gets a bonus of +3 to his Will saving throw'),
    raceModifier('Dexterity', 'increase dexterity of +2'),
    raceModifier('Revelation', 'once per day, reveals to the wielder the position of all the enemies in a room')]


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
