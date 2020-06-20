from src.game_logic import GameLogic
from .helpers import keys, feed_app_with_input
import inquirer as inquirer

winning_choices = {"rock": ["scissors", "lizard"],
                   "paper": ["rock", "spock"],
                   "scissors": ["paper", "lizard"],
                   "lizard": ["paper", "spock"],
                   "spock": ["rock", "scissors"]}
losing_choices = {"rock": ["paper", "spock"],
                  "paper": ["scissors", "lizard"],
                  "scissors": ["rock", "spock"],
                  "lizard": ["rock", "scissors"],
                  "spock": ["paper", "lizard"]}


def test_no_inquirer_lose():
    game_logic = GameLogic()
    for key, values in losing_choices.items():
        for value in values:
            assert game_logic.winner(key, value) == "YOU LOSE, SORRY"


def test_no_inquirer_win():
    game_logic = GameLogic()
    for key, values in winning_choices.items():
        for value in values:
            assert game_logic.winner(key, value) == "YOU WIN, YAY"


def test_no_inquirer_tie():
    game_logic = GameLogic()
    for key in winning_choices.keys():
        assert game_logic.winner(key, key) == "YOU TIED :|"


# def test_inquirer():
#     game_logic = GameLogic()
#
#     message = 'Make your choice'
#     name = 'action'
#     kwargs = {
#         'choices': ["rock", "paper", "scissors", "lizard", "spock"]
#     }
#     text = keys.ENTER
#
#     result, cli = feed_app_with_input('list', message, text, **kwargs)
#     assert result == 'rock'

