class PartyAnimal:
    x = 0

    def __init__(self, name):
        self.name = name
        print(self.name, " Constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "Partied ,total party count ", self.x)


class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        print(self.name, "Scored, total points: ", self.points)
        self.party()


mike = FootballFan('Mike')
mike.party()
mike.touchdown()
