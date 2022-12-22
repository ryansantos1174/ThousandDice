import random
import numpy as np


class Dice():
    def __init__(self, sides):
        self.sides = sides
        self.values = range(1, self.sides+1)
        print(list(self.values))
    def roll(self):
        return random.choice(self.values)

class Game():
    def __init__(self):
        self.onePoints = 100
        self.fivePoints = 50
        self.straightPoints = 1000
        self.threeOnes = 1000
        self.threeFives = 500

    def check_reroll(self, listOfDice):
        return (1 in listOfDice or 5 in listOfDice)

    # Check if any number occurs three times, or if you have a 1 or a 5
    def add_points(self, listOfDice):
        list_values = [dice.roll() for dice in listOfDice]
        print(list_values)
        countDict = {item: list_values.count(item) for item in list_values}
        print(countDict)


game = Game()
dice = [Dice(6), Dice(6), Dice(6), Dice(6), Dice(6)]
game.add_points(dice)
