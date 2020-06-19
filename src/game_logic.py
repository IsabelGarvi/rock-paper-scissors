class GameLogic:
    def winner(self, user_choice, machine_choice) -> str:
        """ Compares both options and gets a winner.
        :param user_choice: option selected by the user.
        :param machine_choice: option calculated by the random function.
        :return: String with the result
        """
        # rock > scissors > paper > lizard > spock
        result = "YOU TIED :|"
        if user_choice == "rock":
            if machine_choice == "paper":
                result = "YOU LOSE, SORRY"
            elif machine_choice == "scissors":
                result = "YOU WIN, YAY"
            elif machine_choice == "lizard":
                result = "YOU WIN, YAY"
            elif machine_choice == "spock":
                result = "YOU LOSE, SORRY"
        elif user_choice == "paper":
            if machine_choice == "scissors":
                result = "YOU LOSE, SORRY"
            elif machine_choice == "rock":
                result = "YOU WIN, YAY"
            elif machine_choice == "lizard":
                result = "YOU LOSE, SORRY"
            elif machine_choice == "spock":
                result = "YOU WIN, YAY"
        elif user_choice == "scissors":
            if machine_choice == "rock":
                result = "YOU LOSE, SORRY"
            elif machine_choice == "paper":
                result = "YOU WIN, YAY"
            elif machine_choice == "lizard":
                result = "YOU WIN, YAY"
            elif machine_choice == "spock":
                result = "YOU LOSE, SORRY"
        elif user_choice == "lizard":
            if machine_choice == "rock":
                result = "YOU LOSE, SORRY"
            elif machine_choice == "paper":
                result = "YOU WIN, YAY"
            elif machine_choice == "scissors":
                result = "YOU LOSE, SORRY"
            elif machine_choice == "spock":
                result = "YOU WIN, YAY"
        elif user_choice == "spock":
            if machine_choice == "rock":
                result = "YOU WIN, YAY"
            elif machine_choice == "paper":
                result = "YOU LOSE, SORRY"
            elif machine_choice == "scissors":
                result = "YOU WIN, YAY"
            elif machine_choice == "lizard":
                result = "YOU LOSE, SORRY"

        return result
