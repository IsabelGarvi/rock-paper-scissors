import random


class RockPaperScissors:
    def __init__(self):
        self._rock = "rock"
        self._paper = "paper"
        self._scissors = "scissors"

    def random_selection(self):
        switcher = {
            1: self._rock,
            2: self._paper,
            3: self._scissors
        }
        return switcher.get(random.randrange(1, 4))
