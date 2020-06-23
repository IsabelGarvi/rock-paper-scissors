from computer_selection import ComputerSelection
from game_logic import GameLogic
import inquirer as inquirer
import os


class Main:
    def __init__(self):
        self._rand_sel = ComputerSelection()
        self._game_logic = GameLogic()
        self.mainFunction()

    def mainFunction(self):
        """ Initiates the program asking the user to select an option.
            Calls for the random_selection function on computer_selection.
            Compares both choices and gets a winner.
        """
        print("")
        print("WELCOME TO ROCK-PAPER-SCISSORS")
        print("------------------------------")
        question = [
            inquirer.List(
                "action",
                "Make your choice",
                ["rock", "paper", "scissors", "lizard", "spock"],
            )
        ]
        user_choice = inquirer.prompt(question)["action"]
        computer_choice = self._rand_sel.random_selection()
        print("YOU:  " + user_choice + " vs COMPUTER:  " + computer_choice)
        rps_winner = self._game_logic.winner(
            user_choice=user_choice, machine_choice=computer_choice
        )
        print(rps_winner)


my_test = Main()
