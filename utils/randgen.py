import random


class ProduceChars:
    """generator class to produce random numbers in a given range"""
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        current = self.start
        while current < 15:
            yield random.randrange(self.start, self.stop)
            current += 1


# class based generator to generate 3 random numbers in given range
class ThreeRandom:
    def __init__(self, range):
        self.start = range[0]
        self.stop = range[1]

    def __iter__(self):
        for i in range(3):
            yield random.randrange(self.start, self.stop + 1)
