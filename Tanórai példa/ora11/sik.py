import math


class Pont:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def tavolsag1(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def tavolsag2(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Teglalap:
    """A téglalap pontjait az óramutatójárásával
     megegyező irányban jellemzi az s1, s2, s3, s4."""

    def __init__(self, s1: Pont, s2: Pont, s3: Pont, s4: Pont):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def oldalhosszak(self):
        return [self.s1.tavolsag1(self.s2), self.s1.tavolsag1(self.s4)]

    def kerulet(self):
        oldalak = self.oldalhosszak()
        return 2 * (oldalak[0] + oldalak[1])

    def terulet(self):
        oldalak = self.oldalhosszak()
        return oldalak[0] * oldalak[1]


class Negyzet(Teglalap):

    def __init__(self, s1: Pont, s2: Pont, s3: Pont, s4: Pont):
        super().__init__(s1, s2, s3, s4)

    def kerulet(self):
        return self.s1.tavolsag1(self.s2) * 4

    """def terulet(self):
        return self.s1.tavolsag1(self.s2) ** 2
    """