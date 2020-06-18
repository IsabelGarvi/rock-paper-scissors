from src.computer_selection import RockPaperScissors


class Main:

    def __init__(self):
        self.rand_sel = RockPaperScissors()
        self.mainFunction()

    def mainFunction(self):
        print("WELCOME TO ROCK-PAPER-SCISSORS")
        print("------------------------------")
        print("MAKE YOUR CHOICE:")
        print("Computers choice: " + self.rand_sel.random_selection())


my_test = Main()
