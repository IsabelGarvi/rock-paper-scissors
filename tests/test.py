from logging import log

from src.game_logic import GameLogic

winning_choices = [{"rock": ["scissors", "lizard"]},
               {"paper": ["rock", "spock"]},
               {"scissors": ["paper", "lizard"]},
               {"lizard": ["paper", "spock"]},
               {"spock": ["rock", "scissors"]}]
losing_choices = [{"rock": ["paper", "spock"]},
               {"paper": ["scissors", "lizard"]},
               {"scissors": ["rock", "spock"]},
               {"lizard": ["rock", "scissors"]},
               {"spock": ["paper", "lizard"]}]


def test_no_inquirer_lose():
    game_logic = GameLogic()
    for d in losing_choices:
        for key, values in d.items():
            for value in values:
                assert game_logic.winner(key, value) == "YOU LOSE, SORRY"


def test_no_inquirer_win():
    game_logic = GameLogic()
    for d in winning_choices:
        for key, values in d.items():
            for value in values:
                assert game_logic.winner(key, value) == "YOU WIN, YAY"


def test_no_inquirer_tie():
    game_logic = GameLogic()
    for d in winning_choices:
        for key in d.keys():
            assert game_logic.winner(key, key) == "YOU TIED :|"
