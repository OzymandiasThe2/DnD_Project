from random import randint, choice, randrange


def nameDetails():
    tempname = Names("temp")
    print(tempname.getName())


class Names:
    """"Will generate random character name from a file/web import of DnD first and last name """

    def __init__(self, player):
        self.player = player
        # self.NPC = NPC

    def getName(self):
        humanNames = {
            'First': ['Alex', 'Alexander'],
            #'First': ['Shriji', 'James', 'Alex', 'Alexander', 'Umer', 'Yash', 'Jonah', 'Vincent', 'Rhys', 'Carson',
            #          'Cameron', 'Leonardo', 'Roswell'],
            'Middle': ['of the', 'Magic', 'Disco', 'Michael', 'Montgomery', 'da', 'le', 'of the', 'Matrox', 'Wesley'],
            'Last': ['Shah', 'Cooke', 'Edwards', 'Mirza', 'Dhume', 'Alexander', 'Galloro', 'Griffiths', 'Asmundson',
                     'Adams', 'Vinci', 'Stoker', 'Winters', 'Summers', 'Stokes'],
            'FirstTitle': ['Bane', 'Horror', 'Champion', 'Speaker', 'Hope', 'Legend', 'Treasure', 'Soul'],
            'LastTitle':  ['Thousands', 'Malice', 'the Past', 'Myths', 'Innocence', 'the Future', 'Wisdom', 'Wealth', 'the Dead', 'Life', 'Honour', 'Justice', 'Gods', 'Heroes', 'the Wild', 'Villainy', 'Lolis', 'Anime', 'Edge',]}

        # 'Sam Billy-Bob Char Mo Clam Ken Wal Tay Har Hank Pat Hen Bar Ben Lo Wal Bel For Ham Ors Pol Mil Mich Gor
        # Cliv Elm Gib Cham Gid Pur Ford Jon Rig Bil Mort Fis Ruther Free'.split()

        nameGen = randint(0, 1)
        if nameGen == 0:
            fn = choice(humanNames['First'])
            md = choice(humanNames['Middle'])
            ln = choice(humanNames['Last'])
            fT = choice(humanNames['FirstTitle'])
            lT = choice(humanNames['LastTitle'])
            if md == 'of the':
                if ln[-1] == 's':
                    # print("Found plural")
                    ln = ln + "'"
                else:
                    # print("NO plural")
                    ln = ln + 's'
            return "%s %s %s \nTitle: %s of %s (Titles are just for background filler, use at own discretion)" % (fn, md, ln, fT, lT)
        else:
            fn = choice(humanNames['First'])
            ln = choice(humanNames['Last'])
            fT = choice(humanNames['FirstTitle'])
            lT = choice(humanNames['LastTitle'])

            return "%s %s \nTitle: %s of %s (Titles are just for background filler, use at own discretion)" % (fn, ln, fT, lT)


