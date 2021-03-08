from random import choice

list_of_monsters = {"Abberation": ["Chuul", "Aboleth", "Cloaker", "Gibbering Mouther", "Otyugh"],
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


def monster_details():
    temp_encounter = MonsterNPC("temp")
    print(temp_encounter.get_monster())


class MonsterNPC:

    def __init__(self, monster):
        self.monster = monster

    def get_monster(self):
        monster_type = choice(list(list_of_monsters))
        monster = choice(list_of_monsters["Abberation"])

        print("Monster type is: ", monster_type)
        print("Monster is: ")
        return '%s' % (monster)


