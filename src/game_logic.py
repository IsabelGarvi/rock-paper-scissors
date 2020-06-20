class GameLogic:

    def winner(self, user_choice, machine_choice) -> str:
        """ Compares both options and gets a winner.
        :param user_choice: option selected by the user.
        :param machine_choice: option calculated by the random function.
        :return: String with the result
        """
        choices = {"rock": ["scissors", "lizard"],
                   "paper": ["rock", "spock"],
                   "scissors": ["paper", "lizard"],
                   "lizard": ["paper", "spock"],
                   "spock": ["rock", "scissors"]}

        result = "YOU TIED :|"
        if choices[user_choice].__contains__(machine_choice):
            result = "YOU WIN, YAY"
        elif choices[machine_choice].__contains__(user_choice):
            result = "YOU LOSE, SORRY"

        return result
