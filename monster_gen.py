from random import randint, choice, randrange

ListMonsters = {"Abberation": ["Chuul", "Aboleth", "Cloaker", "Gibbering Mouther", "Otyugh"],
                "Beast": [],
                "Celestial": [],
                "Construct": [],
                "Dragon": [],
                "Elemental": [],
                "Fey": [],
                "Fiend": [],
                "Fiend (demon)": [],
                "Fiend (devil)": [],
                "Fiend (shapechanger)": [],
                "Giant": [],
                "Humanoid": [],
                "Humanoid (any race)": [],
                "Humanoid (dwarf)": [],
                "Humanoid (elf)": [],
                "Humanoid (gnoll)": [],
                "Humanoid (gnome)": [],
                "Humanoid (goblinoid)": [],
                "Humanoid (grimlock)": [],
                "Humanoid (human)": [],
                "Humanoid (human, shapechanger)": [],
                "Humanoid (kobold)": [],
                "Humanoid (lizardfolk)": [],
                "Humanoid (merfolk)": [],
                "Humanoid (orc)": [],
                "Humanoid (sahuagin)": [],
                "Monstrosity": [],
                "Monstrosity (shapechanger)": [],
                "Monstrosity (titan)": [],
                "Ooze": [],
                "Plant": [],
                "Swarm of tiny beasts": [],
                "Undead": [],
                "Undead (shapechanger)": ["Vampire"],
                }


def monsterDetails():
    temp_encounter = monsterNPC("temp")
    print(temp_encounter.getMonster())


class monsterNPC:

    def __init__(self, monster):
        self.monster = monster

    def getMonster(self):
        monsterType = choice(list(ListMonsters))
        monster = choice(ListMonsters["Abberation"])

        print("Monster type is: ", monsterType)
        print("Monster is: ")
        return '%s' % (monster)

