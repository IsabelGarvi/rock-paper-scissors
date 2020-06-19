from computer_selection import RockPaperScissors
import inquirer as inquirer


class Main:

    def __init__(self):
        self.rand_sel = RockPaperScissors()
        self.mainFunction()

    def winner(self, user_choice, computer_choice) -> str:
        """ Compares both options and gets a winner.
        :param user_choice: option selected by the user.
        :param computer_choice: option calculated by the random function.
        :return: String with the result
        """
        # rock > scissors > paper > rock
        result = "YOU TIED :("
        if user_choice == "rock":
            if computer_choice == "paper":
                result = "YOU LOSE, SORRY"
            elif computer_choice == "scissors":
                result = "YOU WIN, YAY"
            elif computer_choice == "lizard":
                result = "YOU WIN, YAY"
            elif computer_choice == "spock":
                result = "YOU LOSE, SORRY"
        elif user_choice == "paper":
            if computer_choice == "scissors":
                result = "YOU LOSE, SORRY"
            elif computer_choice == "rock":
                result = "YOU WIN, YAY"
            elif computer_choice == "lizard":
                result = "YOU LOSE, SORRY"
            elif computer_choice == "spock":
                result = "YOU WIN, YAY"
        elif user_choice == "scissors":
            if computer_choice == "rock":
                result = "YOU LOSE, SORRY"
            elif computer_choice == "paper":
                result = "YOU WIN, YAY"
            elif computer_choice == "lizard":
                result = "YOU WIN, YAY"
            elif computer_choice == "spock":
                result = "YOU LOSE, SORRY"
        elif user_choice == "lizard":
            if computer_choice == "rock":
                result = "YOU LOSE, SORRY"
            elif computer_choice == "paper":
                result = "YOU WIN, YAY"
            elif computer_choice == "scissors":
                result = "YOU LOSE, SORRY"
            elif computer_choice == "spock":
                result = "YOU WIN, YAY"
        else:
            if computer_choice == "rock":
                result = "YOU WIN, YAY"
            elif computer_choice == "paper":
                result = "YOU LOSE, SORRY"
            elif computer_choice == "scissors":
                result = "YOU WIN, YAY"
            elif computer_choice == "lizard":
                result = "YOU LOSE, SORRY"
        return result

    def mainFunction(self):
        """ Initiates the program asking the user to select an option.
            Calls for the random_selection function on computer_selection.
            Compares both choices and gets a winner.
        """
        print("")
        print("WELCOME TO ROCK-PAPER-SCISSORS")
        print("------------------------------")
        question = [inquirer.List("action", "Make your choice",
                                  ["rock",
                                   "paper",
                                   "scissors",
                                   "lizard",
                                   "spock"])]
        user_choice = inquirer.prompt(question)["action"]
        computer_choice = self.rand_sel.random_selection()
        print("YOU:  " + user_choice + " vs COMPUTER:  " + computer_choice)
        # print("THE COMPUTER CHOSE: " + computer_choice)
        rps_winner = self.winner(user_choice=user_choice, computer_choice=computer_choice)
        print(rps_winner)


my_test = Main()
