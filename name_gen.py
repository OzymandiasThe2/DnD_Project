from random import randint, choice


def name_details():
    temp_name = Names("temp")
    print(get_name())


def get_name():
    human_names = {
        'First': ['Alex', 'Alexander'],
        # 'First': ['Shriji', 'James', 'Alex', 'Alexander', 'Umer', 'Yash', 'Jonah', 'Vincent', 'Rhys', 'Carson',
        #          'Cameron', 'Leonardo', 'Roswell'],
        'Middle': ['of the', 'Magic', 'Disco', 'Michael', 'Montgomery', 'da', 'le', 'of the', 'Matrox', 'Wesley'],
        'Last': ['Shah', 'Cooke', 'Edwards', 'Mirza', 'Dhume', 'Alexander', 'Galloro', 'Griffiths', 'Asmundson',
                 'Adams', 'Vinci', 'Stoker', 'Winters', 'Summers', 'Stokes'],
        'FirstTitle': ['Bane', 'Horror', 'Champion', 'Speaker', 'Hope', 'Legend', 'Treasure', 'Soul'],
        'LastTitle': ['Thousands', 'Malice', 'the Past', 'Myths', 'Innocence', 'the Future', 'Wisdom', 'Wealth',
                      'the Dead', 'Life', 'Honour', 'Justice', 'Gods', 'Heroes', 'the Wild', 'Villainy', 'Lolis',
                      'Anime', 'Edge', ]}

    # 'Sam Billy-Bob Char Mo Clam Ken Wal Tay Har Hank Pat Hen Bar Ben Lo Wal Bel For Ham Ors Pol Mil Mich Gor
    # Cliv Elm Gib Cham Gid Pur Ford Jon Rig Bil Mort Fis Ruther Free'.split()

    name_gen = randint(0, 1)
    if name_gen == 0:
        fn = choice(human_names['First'])
        md = choice(human_names['Middle'])
        ln = choice(human_names['Last'])
        ft = choice(human_names['FirstTitle'])
        lt = choice(human_names['LastTitle'])
        if md == 'of the':
            if ln[-1] == 's':
                # print("Found plural")
                ln = ln + "'"
            else:
                # print("NO plural")
                ln = ln + 's'
        return "%s %s %s \nTitle: %s of %s (Titles are just for background filler, use at own discretion)" % (
            fn, md, ln, ft, lt)
    else:
        fn = choice(human_names['First'])
        ln = choice(human_names['Last'])
        ft = choice(human_names['FirstTitle'])
        lt = choice(human_names['LastTitle'])

        return "%s %s \nTitle: %s of %s (Titles are just for background filler, use at own discretion)" % (
            fn, ln, ft, lt)


class Names:
    """"Will generate random character name from a file/web import of DnD first and last name """

    def __init__(self, player):
        self.player = player
        # self.NPC = NPC
