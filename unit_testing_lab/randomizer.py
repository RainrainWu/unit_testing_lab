from random import random


class Randomizer:

    @staticmethod
    def pick():
        return random()

    @staticmethod
    def amplify(factor: int):

        return Randomizer.pick() * factor

    def shift(value: int):

        return Randomizer.pick() + value