from random import randint, choice

# STUFF TO USE!!!
# http://neverwinter.gamepedia.com/Half-Elf#Names
from name_gen import nameDetails, Names


def generateNPC():
    NPCrace = generateRACE()
    NPCclass = generateCLASS()
    NPCsubclass = subClasses()
    NPCgender = generateGENDER()
    NPCcharachteristics = generateCHARStats()
    # npc = NameGenerator.generate(GENDERFlag, RACEflag)
    tempname = Names("NPC")
    npc = tempname.getName()
    # npc = npc + ' \n' + '(' + NPCgender + ') \n' + NPCrace + ' \n' + NPCclass + ' \n'
    npc = 'Name: ' + npc + '\nGender: ' + NPCgender + '\nRace: ' + NPCrace + '\nClass: ' + NPCclass + '\nSubclass: ' + NPCsubclass + '\n'
    npc = npc + NPCcharachteristics
    return npc


def generateRACE():
    global Two_STR_Race, One_STR_Race, Two_DEX_Race, One_DEX_Race, Two_CON_Race, One_CON_Race, Two_WIS_Race, One_WIS_Race, Two_INT_Race, One_INT_Race, Two_CAR_Race, One_CAR_Race, Two_RAN_One_Race, One_RAN_One_Race, One_All_Race
    global NPCrace

    races = ['Dwarf', 'Elf', 'Human', 'Gnome', 'Half-Elf', 'Half-Orc', 'Halfling', 'Dragonborn', 'Tiefling',
             'Orc of Exandria',
             'Aarakocra', 'Genasi', 'Goliath', 'Goliath', 'Bugbear', 'Aasimar', 'Firbolg', 'Goblin', 'Hobgoblin',
             'Kenku', 'Kobold', 'Lizardfolk', 'Orc', 'Triton', 'Yuan-ti Pureblood', 'Feral Tiefling', 'Tortle',
             'Changeling', 'Kalashtar', 'Orc of Eberron', 'Shifter', 'Warforged', 'Gith', 'Centaur', 'Loxodon',
             'Minotaur', 'Simic Hybrid', 'Vedalken', 'Verdan', 'Locathah', 'Grung', 'Tabaxi']
    try:
        NPCrace = choice(races)
    except ValueError:
        NPCrace = 'error with NPCrace Gen'
    except IndexError:
        NPCrace = 'error with NPCrace Gen'

    Two_STR_Race = (
        'Dragonborn', 'Half-Orc', 'Orc of Exandria', 'Goliath', 'Bugbear', 'Orc', 'Tortle', 'Orc of Eberron', 'Centaur',
        'Minotaur', 'Locathah')
    One_STR_Race = ('Firbolg', 'Triton')
    Two_DEX_Race = ('Elf', 'Halfling', 'Aarakocra', 'Goblin', 'Kenku', 'Kobold', 'Tabaxi', 'Feral Tiefling', 'Grung')
    One_DEX_Race = ('Bugbear', 'Locathah')
    Two_CON_Race = ('Dwarf', 'Genasi', 'Hobgoblin', 'Lizardfolk', 'Warforged', 'Loxodon', 'Simic Hybrid')
    One_CON_Race = (
        'Half-Orc', 'Orc of Exandria', 'Goliath', 'Goblin', 'Orc', 'Triton', 'Orc of Eberron', 'Minotaur', 'Verdan',
        'Grung')
    Two_WIS_Race = ('Firbolg', 'Kalashtar')
    One_WIS_Race = ('Aarakocra', 'Kenku', 'Lizardfolk', 'Tortle', 'Centaur', 'Loxodon', 'Vedalken')
    Two_INT_Race = ('Gnome', 'Vedalken')
    One_INT_Race = ('Tiefling', 'Hobgoblin', 'Yuan-ti Pureblood', 'Feral Tiefling', 'Gith')
    Two_CAR_Race = ('Half-Orc', 'Tiefling', 'Aasimar', 'Yuan-ti Pureblood', 'Changeling', 'Verdan')
    One_CAR_Race = ('Dragonborn', 'Tabaxi', 'Triton', 'Kalashtar')
    Two_RAN_One_Race = ('Half-Elf')
    One_RAN_One_Race = ('War-Forged', 'Simic Hybrid')
    One_All_Race = ('Human')
    #
    return NPCrace


def generateCLASS():
    global classFlag
    i = randint(0, 13)
    if i == 0:
        NPCclass = 'Barbarian'
        classFlag = 0
    elif i == 1:
        NPCclass = 'Bard'
        classFlag = 1
    elif i == 2:
        NPCclass = 'Cleric'
        classFlag = 2
    elif i == 3:
        NPCclass = 'Druid'
        classFlag = 3
    elif i == 4:
        NPCclass = 'Fighter'
        classFlag = 4
    elif i == 5:
        NPCclass = 'Monk'
        classFlag = 5
    elif i == 6:
        NPCclass = 'Paladin'
        classFlag = 6
    elif i == 7:
        NPCclass = 'Ranger'
        classFlag = 7
    elif i == 8:
        NPCclass = 'Rouge'
        classFlag = 8
    elif i == 9:
        NPCclass = 'Sorcerer'
        classFlag = 9
    elif i == 10:
        NPCclass = 'Warlock'
        classFlag = 10
    elif i == 11:
        NPCclass = 'Wizard'
        classFlag = 11
    elif i == 12:
        NPCclass = 'Artificer'
        classFlag = 12
    elif i == 13:
        NPCclass = 'Blood Hunter'
        classFlag = 13
    else:
        NPCclass = 'error'
    return NPCclass


def generateGENDER():
    gender = randint(0, 1)
    global GENDERFlag
    if gender == 0:
        gender = 'Male'
        GENDERFlag = 0
    elif gender == 1:
        gender = 'Female'
        GENDERFlag = 1
    else:
        'error'
    return gender


def subClasses():
    global subClassFlag
    if classFlag == 0:
        subClassBarb = (
            'Path of the Berserker', 'Path of the Zealot', 'Path of the Battlerager', 'Path of the Storm Herald',
            'Path of the Ancestral Guardian', 'Path of the Totem Warrior')
        subClassFlag = choice(subClassBarb)
    elif classFlag == 1:
        subClassBard = (
            'College Of Swords', 'College Of Whispers', 'College Of Glamour', 'College Of Valor', 'College Of Lore')
        subClassFlag = choice(subClassBard)
    elif classFlag == 2:
        subClassCleric = (
            'Arcana Domain', 'Death Domain', 'Forge Domain', 'Grave Domain', 'Knowledge Domain', 'Life Domain',
            'Light Domain', 'Nature Domain', 'Order Domain', 'Tempest Domain', 'Trickery Domain', 'War')
        subClassFlag = choice(subClassCleric)
    elif classFlag == 3:
        subClassDruid = (
            'Circle of Dreams', 'Circle of Moon', 'Circle of Land', 'Circle of Shepherd', 'Circle of Spores',
            'Circle of Stars', 'Circle of Twilight', 'Circle of Wildfire')
        subClassFlag = choice(subClassDruid)
    elif classFlag == 4:
        subClassFighter = (
            'Arcane Archer', 'Banneret', 'Battle Master', 'Brute (UA)', 'Cavalier', 'Champion', 'Eldritch Knight',
            'Knight (UA)', 'Monster Hunter (UA)', 'Psychic Warrior (UA)', 'Rune Knight (UA)', 'Samurai,Scout (UA)',
            'Sharpshooter (UA)')
        subClassFlag = choice(subClassFighter)
    elif classFlag == 5:
        subClassMonk = ('Way of the Sun Soul', 'Way of the Kensei', 'Way of the Four Elements', 'Way of the Shadow',
                        'Way of the Open Hand', 'Way of the Long Death', 'Way of the Drunken Master')
        subClassFlag = choice(subClassMonk)
    elif classFlag == 6:
        subClassPaladin = (
            'Oath Of The Crown', 'Oath Of Redemption', 'Oath Of Vengeance', 'Oath Of The Ancients', 'Oath Of Conquest',
            'Oath Of Devotion')
        subClassFlag = choice(subClassPaladin)
    elif classFlag == 7:
        subClassRanger = ('Test', 'Test')
        subClassFlag = choice(subClassRanger)
    elif classFlag == 8:
        subClassRouge = ('Test', 'Test')
        subClassFlag = choice(subClassRouge)
    elif classFlag == 9:
        subClassSorcerer = ('Test', 'Test')
        subClassFlag = choice(subClassSorcerer)
    elif classFlag == 10:
        subClassWarlock = ('Test', 'Test')
        subClassFlag = choice(subClassWarlock)
    elif classFlag == 11:
        subClassWizard = ('Test', 'Test')
        subClassFlag = choice(subClassWizard)
    elif classFlag == 12:
        subClassArtificer = ('Test', 'Test')
        subClassFlag = choice(subClassArtificer)
    elif classFlag == 13:
        subClassBloodHunter = ('Test', 'Test')
        subClassFlag = choice(subClassBloodHunter)
    return subClassFlag


def generateCHARStats():
    # CHECK OUT JUSTISAURU'S METHODS https://sites.google.com/site/justisaursdd/tar-pit-dugout/justisaurs27-25
    # -23abilityscoregeneration
    dice = 0
    flag = 0
    STR = 0
    DEX = 0
    COS = 0
    INT = 0
    WIS = 0
    CAR = 0
    # DWARF = 1 ELF = 2 HUMAN = 3 GNOME = 4 HALF ELF = 5 HALF ORC = 6 HALFLING = 7
    # STR generation
    for dice in range(0, 3):
        diceroll = randint(1, 6)
        if diceroll == 1 and flag == 0:
            diceroll = randint(1, 6)
            STR = STR + diceroll
            flag == 1
        else:
            STR = STR + diceroll
        # Race modificator (+Half orc(6), -Halfling(7), -Gnome(4))
        if NPCrace in Two_STR_Race:
            STR = STR + 2
        elif NPCrace in One_STR_Race:
            STR = STR + 1
        else:
            pass

    # DEX generation
    for dice in range(0, 3):
        diceroll = randint(1, 6)
        if diceroll == 1 and flag == 0:
            diceroll = randint(1, 6)
            DEX = DEX + diceroll
            flag == 1
        else:
            DEX = DEX + diceroll
        # Race modificator (+Elf(2), +Halfling(7))
        if NPCrace in Two_DEX_Race:
            DEX = DEX + 2
        elif NPCrace in One_DEX_Race:
            DEX = DEX + 1
        else:
            pass

    # COS generation
    for dice in range(0, 3):
        diceroll = randint(1, 6)
        if diceroll == 1 and flag == 0:
            diceroll = randint(1, 6)
            COS = COS + diceroll
            flag == 1
        else:
            COS = COS + diceroll
        # Race modificator (+Dwarf(1), +Gnome(4), -Elf(2))
        if NPCrace in Two_CON_Race:
            COS = COS + 2
        elif NPCrace in One_CON_Race:
            COS = COS + 1
        else:
            pass

    # INT generation
    for dice in range(0, 3):
        diceroll = randint(1, 6)
        if diceroll == 1 and flag == 0:
            diceroll = randint(1, 6)
            INT = INT + diceroll
            flag == 1
        else:
            INT = INT + diceroll
        # Race modificator (-Half Orc(6))
        if NPCrace in Two_INT_Race:
            INT = INT + 2
        elif NPCrace in One_INT_Race:
            INT = INT + 1
        else:
            pass

    # WIS generator
    for dice in range(0, 3):
        diceroll = randint(1, 6)
        if diceroll == 1 and flag == 0:
            diceroll = randint(1, 6)
            WIS = WIS + diceroll
            flag == 1
        else:
            WIS = WIS + diceroll
        # Race modificator (NULL)
        if NPCrace in Two_WIS_Race:
            WIS = WIS + 2
        elif NPCrace in One_WIS_Race:
            WIS = WIS + 1
        else:
            pass

    # CAR generator
    for dice in range(0, 3):
        diceroll = randint(1, 6)
        if diceroll == 1 and flag == 0:
            diceroll = randint(1, 6)
            CAR = CAR + diceroll
            flag == 1
        else:
            CAR = CAR + diceroll
        # Race modification(-Dwarf(1), -Half-Orc(6))
        if NPCrace in Two_CAR_Race:
            CAR = CAR + 2
        elif NPCrace in One_CAR_Race:
            CAR = CAR + 1
        else:
            pass

    if NPCrace in Two_RAN_One_Race:
        randnum1 = randint(1, 6)
        randnum2 = randint(1, 6)
        while randnum2 == randnum1:
            randnum2 = randint(1, 6)

        if randnum1 == 1:
            STR = STR + 1
        elif randnum1 == 2:
            DEX = DEX + 1
        elif randnum1 == 3:
            COS = COS + 1
        elif randnum1 == 4:
            WIS = WIS + 1
        elif randnum1 == 5:
            INT = INT + 1
        elif randnum1 == 6:
            CAR = CAR + 1

        if randnum2 == 1:
            STR = STR + 1
        elif randnum2 == 2:
            DEX = DEX + 1
        elif randnum2 == 3:
            COS = COS + 1
        elif randnum2 == 4:
            WIS = WIS + 1
        elif randnum2 == 5:
            INT = INT + 1
        elif randnum2 == 6:
            CAR = CAR + 1

    if NPCrace in One_RAN_One_Race:
        randnum1 = randint(1, 6)
        if randnum1 == 1:
            STR = STR + 1
        elif randnum1 == 2:
            DEX = DEX + 1
        elif randnum1 == 3:
            COS = COS + 1
        elif randnum1 == 4:
            WIS = WIS + 1
        elif randnum1 == 5:
            INT = INT + 1
        elif randnum1 == 6:
            CAR = CAR + 1

    if NPCrace in One_All_Race:
        STR = STR + 1
        DEX = DEX + 1
        COS = COS + 1
        WIS = WIS + 1
        INT = INT + 1
        CAR = CAR + 1

    if classFlag == 0:  # Barb
        STR = STR + 2
    elif classFlag == 1:  # Bard
        CAR = CAR + 2
    elif classFlag == 2:  # Cleric
        WIS = WIS + 2
    elif classFlag == 3:  # Druid
        WIS = WIS + 2
    elif classFlag == 4:  # Fighter
        fighterPro = randint(1, 2)
        if fighterPro == 1:
            STR = STR + 2
        elif fighterPro == 2:
            DEX = DEX + 2
    elif classFlag == 5:  # Monk
        DEX = DEX + 1
        WIS = WIS + 1
    elif classFlag == 6:  # Paladin
        STR = STR + 1
        CAR = CAR + 1
    elif classFlag == 7:  # Ranger
        WIS = WIS + 1
        DEX = DEX + 1
    elif classFlag == 8:  # Rogue
        DEX = DEX + 2
    elif classFlag == 9:  # Sorcerer
        CAR = CAR + 2
    elif classFlag == 10:  # Warlock
        CAR = CAR + 2
    elif classFlag == 11:  # Wizard
        INT = INT + 2
    elif classFlag == 12:  # Artificer
        INT = INT + 2
    elif classFlag == 13:  # Blood Hunter
        bloodPro = randint(1, 2)
        if bloodPro == 1:
            STR = STR + 1
        elif bloodPro == 2:
            DEX = DEX + 1
        INT = INT + 1

    characteristics = 'STR: %d, DEX: %d, CON: %d, INT: %d, WIS: %d, CHA: %d' % (STR, DEX, COS, INT, WIS, CAR)
    return characteristics


