import random
from game import Game

from helpers import get_possibilities
from helpers import flatten


def get_qtable_columns():
    return list(map(get_possibilities, [x for x in range(1, 13)]))


def build_q_table():
    q_table = []
    for _ in range(0, 3):
        q_table.append([0.0 for _ in flatten(get_qtable_columns())])

    return q_table


def make_random_choice(roll, board):
    choices = get_possibilities(roll)
    valid_choices = []
    for choice in choices:
        if all(elem in board for elem in choice):
            valid_choices.append(choice)
    return valid_choices[random.randint(0, len(valid_choices) - 1)]


def main():
    qtable = build_q_table()
    columns = flatten(get_qtable_columns())
    game = Game()
    while not game.get_game_over():
        while True:
            try:
                choice = make_random_choice(game.get_roll(), game.get_board().state)
                game.shut_boxes(choice)
                break
            except ValueError as err:
                print(err)

        game.tick()

        column_index = columns.index(choice)

        if game.get_game_over() and game.get_score() == 0: # Winner
            qtable[1][column_index] = game.get_score()
        elif game.get_game_over(): # Record Loss
            qtable[2][column_index] = game.get_score()
        else: # Keep Going
            qtable[0][column_index] = game.get_score()

    print("\nGame over. Final score: " + str(game.get_score()))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
