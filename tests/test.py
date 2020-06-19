from src.game_logic import GameLogic

# choices = ["rock", "paper", "scissors", "lizard", "spock"]


def test_no_inquirer_lose():
    game_logic = GameLogic()
    user = "rock"
    machine = "paper"

    assert game_logic.winner(user, machine) == "YOU LOSE, SORRY"


def test_no_inquirer_win():
    game_logic = GameLogic()
    user = "paper"
    machine = "rock"

    assert game_logic.winner(user, machine) == "YOU WIN, YAY"


def test_no_inquirer_tie():
    game_logic = GameLogic()
    user = "scissors"
    machine = "scissors"

    assert game_logic.winner(user, machine) == "YOU TIED :|"
