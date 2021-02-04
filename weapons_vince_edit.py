from random import randint, choice

#TODO: Thank your local Vincent for cleaning up the nightmare field of IF conditions

#TYPES
class WeaponType():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        
class WeaponModifier():
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

class Weapon():
    def __init__(self, weaponType, modifier = None):
        self.weaponType = weaponType
        self.modifier = modifier
        
    def __str__(self):
        if(self.modifier == None):
            return self.weaponType.name+"\n"+self.weaponType.damage
        return self.weaponType.name+" of "+self.modifier.name+"\n"+self.weaponType.damage+"\n"+self.modifier.effect

#USER DEFINED WEAPONS
weaponCategories = ['Sword', 'Ranged', 'Hammer', 'Magic']

swordWeapons = [
    WeaponType('Dagger', '1d4, piercing'), 
    WeaponType('Longsword (1H)', '1d6, piercing'), 
    WeaponType('Greatsword (2H)', '2d6, 19-20 x2'), 
    WeaponType('Scythe (2H)', '2d4, x4'), 
    WeaponType('Bastard Sword', '1d10, 19-20 x2')]
rangedWeapons = [
    WeaponType('Crossbow', '1d8, 19-20 x2'),
    WeaponType('Longbow', '1d8, x3'),
    WeaponType('Composite Longbow', '1d8, x3'),
    WeaponType('Shortbow', '1d6, x3'),
    WeaponType('Composite Shortbow', '1d6, x3'),
    WeaponType('Repeating Crossbow', '1d8, 19-20 x2')]
hammerWeapons = [
    WeaponType('Morningstar (1H)', '1d8, x2'),
    WeaponType('Warhammer (1H)', '1d8, x3'),
    WeaponType('Waraxe (1H)', '1d10, x3'),
    WeaponType('Greataxe (2H)', '1d12, x3'),
    WeaponType('Great club (2H)', '1d10, x2'),
    WeaponType('Great Hammer (2H, requires 18 in strength)', '1d12, 19-20 x3')]
magicWeapons = [
    WeaponType('Wand', 'n charges of random spell'),
    WeaponType('Staff', '1d6, 19-20 x2, n charges of random spell')]
    
weaponTypesByCategory = {
    "Sword": swordWeapons, 
    "Ranged": rangedWeapons, 
    "Hammer": hammerWeapons, 
    "Magic": magicWeapons
}

#USER DEFINED MODIFIERS
magicModifiers = [
    WeaponModifier('powerful Strength', 'Increase strength by +3'),
    WeaponModifier('powerful Dexterity', 'Increase dexterity by +3'),
    WeaponModifier('powerful Constitution', 'Increase constitution by +3'),
    WeaponModifier('powerful Intelligence', 'Increase intelligence by +3'),
    WeaponModifier('powerful Wisdom', 'Increase wisdom by +3'),
    WeaponModifier('powerful Charisma', 'Increase charisma by +3')]

basicModifiers = [
    WeaponModifier('Strength', 'Increase Strength by +2'),
    WeaponModifier('the Evil Slaughter', 'basic attacks deal +2d6 damage to Evil targets'),
    WeaponModifier('Detect Good', 'grants the wielder the ability to Detect Good'),
    WeaponModifier('Freezing', '25% chance of freezing an enemy for one round'),
    WeaponModifier('Lockpicking', 'once per day, the wielder can pick a lock he wants for free'),
    WeaponModifier('Invisibility', 'grants invisibility to the wielder 1 minute per day'),
    WeaponModifier('the Humanoid Slayer', 'basic attacks deal +3d6 to humanoid targets'),
    WeaponModifier('Detect Magic', 'once a day, grants the wielder a successful action of Detect Magic'),
    WeaponModifier('Light', 'creates light in a circular region around the wielder with range 9m'),
    WeaponModifier('strong Reflexes', 'The wielder gets a bonus of +3 to his Reflexes saving throw'),
    WeaponModifier('strong Fortitude', 'The wielder gets a bonus of +3 to his Fortitude saving throw'),
    WeaponModifier('strong Will', 'The wielder gets a bonus of +3 to his Will saving throw'),
    WeaponModifier('Dexterity', 'increase dexterity of +2'),
    WeaponModifier('Revelation', 'once per day, reveals to the wielder the position of all the enemies in a room')]
    #etc... add your own

#FUNCTIONS
def generateRandomWeaponType():
    category = choice(weaponCategories)
    return choice(weaponTypesByCategory[category])

def generateRandomWeaponModifier():
    if(randint(0, 2)==0): return None #50% chance of no modifier
    if(randint(0, 99)==0): return choice(magicModifiers) #1/100 chance
    return choice(basicModifiers)

def generateRandomWeapon():
    return Weapon(generateRandomWeaponType(), generateRandomWeaponModifier())

print(generateRandomWeapon())
