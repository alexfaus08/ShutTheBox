from board import Board
from random import randint

class Game:
    def __init__(self):
        self.__board = Board()
        self.__roll = 0
        self.__game_over = False
        self.tick()

    def get_board(self):
        return self.__board

    def get_game_over(self):
        return self.__game_over

    def get_roll(self):
        return self.__roll

    def get_score(self):
        return self.__board.get_score()

    def tick(self):
        """ Advance the game one turn. """
        self.__new_roll()
        self.__calculate_game_over()

    def shut_boxes(self, boxes_to_shut):
        self.__is_valid_move(boxes_to_shut)
        for box in boxes_to_shut:
            self.__board.shut_box(box)

    def __is_valid_move(self, boxes_to_shut):
        """ Raises an error to the caller if the move is invalid """
        if self.__roll != sum(set(boxes_to_shut)):
            raise ValueError('Boxes do not add up to dice roll.')

        for box in boxes_to_shut:
            if not box in self.__board.state:
                raise ValueError('Box ' + str(box) + ' is already closed.')

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
