from random import randint, choice, randrange


def weaponDetails():
    weaponTypes = ['Handgun', 'Bow', 'Rifle', 'Sword', 'Hammer', 'Axe', 'Staff']
    weaponSize = ['Tiny', 'Small', 'Normal', 'Large', 'Enormous']
    weaponRarity = ['Trash', 'Average', 'Magical', 'Legendary']
    weaponNames = {'Sword': ['Rapier of Force', 'Adventurous Claymore'],
                   'Hammer': ['Destiny Smasher', 'Test'],
                   'Staff': ['Monkey Lords Staff', 'Test'],
                   'Rifle': ['Deadshot', 'Test'],
                   'Handgun': ['Golden Gun', 'Test'],
                   'Bow': ['Ancestral Relic Bow', 'Test'],
                   'Axe': ['Talinoq Bloodletter', 'Test']}
    rw = RandWeapon(weaponSize, weaponRarity, weaponTypes)
    rw = rw.get_weapon()
    print(rw)  # This will calc your weapons"""
    if 'Legendary' in rw:
        print("Congratulation you got the:")
        if 'Handgun' in rw:
            print(choice(weaponNames['Handgun']))
        if 'Bow' in rw:
            print(choice(weaponNames['Bow']))
        if 'Rifle' in rw:
            print(choice(weaponNames['Rifle']))
        if 'Sword' in rw:
            print(choice(weaponNames['Sword']))
        if 'Hammer' in rw:
            print(choice(weaponNames['Hammer']))
        if 'Axe' in rw:
            print(choice(weaponNames['Axe']))
        if 'Staff' in rw:
            print(choice(weaponNames['Staff']))
    # TODO: add more variation and if statements so you don't get a long ass gun


class RandWeapon:

    def __init__(self, weaponStats, weaponRarity, weaponTypes):
        self.weaponStats = weaponStats
        self.weaponTypes = weaponTypes
        self.weaponRarity = weaponRarity

    def getRandomStats(self):
        return self.weaponStats[randint(0, len(self.weaponStats) - 1)]

    def getRandomTypes(self):
        return self.weaponTypes[randint(0, len(self.weaponTypes) - 1)]

    def getRandomRarity(self):
        return self.weaponRarity[randint(0, len(self.weaponRarity) - 1)]

    def get_weapon(self):
        return '{} {} {}'.format(self.getRandomStats(), self.getRandomRarity(), self.getRandomTypes())
