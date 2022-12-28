import random
import numpy as np
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


def make_qtable_choice(roll, board, qtable, columns):
    choices = get_possibilities(roll)
    valid_choices_values = []
    valid_choices = []
    for choice in choices:
        if all(elem in board for elem in choice):
            valid_choices_values.append(qtable[columns.index(choice)])
            valid_choices.append(choice)
    choice_index = np.argmax(valid_choices_values)
    return valid_choices[choice_index]


def main():
    qtable = build_q_table()
    columns = flatten(get_qtable_columns())

    # number of episode we will run
    n_episodes = 10000

    # maximum of iteration per episode
    max_iter_episode = 100

    # initialize the exploration probability to 1
    exploration_proba = 1

    # exploration decreasing decay for exponential decreasing
    exploration_decreasing_decay = 0.001

    # minimum of exploration proba
    min_exploration_proba = 0.01

    # discounted factor
    gamma = 0.99

    all_rewards = list()

    # learning rate
    lr = 0.1

    for e in range(n_episodes):
        print('Starting Game ', e)
        game = Game()
        print(game.get_board().state)
        current_state = 0
        total_episode_reward = 0

        while not game.get_game_over():
            if np.random.uniform(0, 1) < exploration_proba:
                choice = make_random_choice(game.get_roll(), game.get_board().state)
            else:
                choice = make_qtable_choice(game.get_roll(), game.get_board().state, qtable, columns)

            print(choice)
            game.shut_boxes(choice)

            game.tick()

            column_index = columns.index(choice)
            if game.get_game_over() and game.get_score() == 0: # Winner
                next_state = 1
                qtable[1][column_index] = game.get_score()
            elif game.get_game_over(): # Record Loss
                next_state = 2
                qtable[2][column_index] = game.get_score()
            else: # Keep Going
                next_state = 0
                qtable[0][column_index] = game.get_score()

            reward = game.get_score()
            # We update our Q-table using the Q-learning iteration
            qtable[current_state][column_index] = (1 - lr) * qtable[current_state][column_index] + lr * (
                    reward + gamma * max(qtable[next_state][:]))
            current_state = next_state

            total_episode_reward += reward
            # We update the exploration proba using exponential decay formula
            exploration_proba = max(min_exploration_proba, np.exp(-exploration_decreasing_decay * e))
            all_rewards.append(total_episode_reward)

        print("\nGame over. Final score: " + str(game.get_score()))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
