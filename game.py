from random import randint
from board import Board

def roll_die():
    return randint(1, 6)

class Game:
    def __init__(self):
        self.game_over = False
        self.board = Board()

    def check_game_over(self, roll):
        self.game_over = self.__is_subset_sum(self.board, len(self.board), roll)

    def is_valid_move(self, roll, doors_to_shut):
        doors_to_shut = set(doors_to_shut)
        if roll != sum(doors_to_shut):
            print('Doors do not add up to dice roll.')
            return False

        for door in doors_to_shut:
            if not door in self.board:
                print('At least one is not open.')
                return False

        return True

    def __is_subset_sum(self, set, n, sum) :
        # Base Cases
        if (sum == 0) :
            return True
        if (n == 0 and sum != 0) :
            return False

        # If last element is greater than
        # sum, then ignore it
        if (set[n - 1] > sum) :
            return self.is_subset_sum(set, n - 1, sum);

        # else, check if sum can be obtained
        # by any of the following
        # (a) including the last element
        # (b) excluding the last element
        return self.is_subset_sum(set, n-1, sum) or self.is_subset_sum(set, n-1, sum-set[n-1])

    def __str__(self):
        return self.board.__str__()

try:
    game = Game()
    while not game.game_over:
        print(game)

        roll = roll_die()
        if game.board.requires_two_dice():
            roll += roll_die()
        doors_to_shut = []
        invalid_input = True
        while invalid_input:
            try:
                doors_to_shut = list(int(num) for num in input("Roll: " + str(roll) + " -- doors to shut >> ").strip().split())
                if not game.is_valid_move(roll, doors_to_shut):
                    print('Invalid move')
                    continue

                invalid_input = False
            except:
               print("Invalid input. Please try again.\n\n")

        for door in doors_to_shut:
            game.board.shut_door(door)
except KeyboardInterrupt:
    exit()
