import random
from game import Game

from helpers import get_possibilities
from helpers import flatten


def get_qtable_columns():
    return list(map(get_possibilities, [x for x in range(1, 13)]))


def build_q_table():
    q_table = []
    for i in range(0, 3):
        q_table.append([0.0 for _ in flatten(get_qtable_columns())])

    return q_table


def make_random_choice(roll, board):
    choices = get_possibilities(roll)
    for choice in choices:
        if choice not in board:
            choices.remove(choice)
    return choices[random.randint(0, len(choices) - 1)]


def main():
    qtable = build_q_table()
    game = Game()
    while not game.get_game_over():
        print(game)

        while True:
            try:
                boxes_to_shut = make_random_choice(game.get_roll(), game.get_board())
                game.shut_boxes(boxes_to_shut)
                break
            except ValueError as err:
                print(err)

        game.tick()

    print("\nGame over. Final score: " + str(game.get_score()))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()