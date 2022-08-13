from board import Board
from random import randint

class Game:
    __game_over = False
    __board = Board()
    __roll = 0

    def __init__(self):
        self.tick()

    def get_board(self):
        return self.__board

    def get_game_over(self):
        return self.__game_over

    def get_roll(self):
        return self.__roll

    def tick(self):
        """ Advance the game one turn. """
        self.__new_roll()
        self.__calculate_game_over()

    def is_valid_move(self, roll, boxes_to_shut):
        # Use 'set' to remove duplicate entries and then sum them to make sure it's a valid move
        if roll != sum(set(boxes_to_shut)):
            print('Boxes do not add up to dice roll.')
            return False

        for box in boxes_to_shut:
            if not box in self.__board.state:
                print('At least one box is not open.')
                return False

        return True

    def __roll_die(self):
        return randint(1, 6)

    def __new_roll(self):
        self.__roll = self.__roll_die()
        if self.__board.requires_two_dice():
            self.__roll += self.__roll_die()

    def __calculate_game_over(self):
        self.__game_over = not self.__is_subset_sum(self.__board.state, len(self.__board.state), self.__roll)

    def __is_subset_sum(self, set, n, sum) :
        # Base Cases
        if (sum == 0) :
            return True
        if (n == 0 and sum != 0) :
            return False

        # If last element is greater than
        # sum, then ignore it
        if (set[n - 1] > sum) :
            return self.__is_subset_sum(set, n - 1, sum);

        # else, check if sum can be obtained
        # by any of the following
        # (a) including the last element
        # (b) excluding the last element
        return self.__is_subset_sum(set, n-1, sum) or self.__is_subset_sum(set, n-1, sum-set[n-1])

    def __str__(self):
        return self.__board.__str__()
