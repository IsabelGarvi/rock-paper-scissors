import random


class ComputerSelection:

    def random_selection(self) -> str:
        """ Randomly selects an int which can be
            Rock, Paper or Scissors.
        """
        switcher = {
            1: "rock",
            2: "paper",
            3: "scissors",
            4: "lizard",
            5: "spock"
        }
        return switcher.get(random.randrange(1, 6))
