from board import Board

class Game:
    def __init__(self):
        self.__game_over = False
        self.__board = Board()

    def get_board(self):
        return self.__board

    def get_game_over(self):
        return self.__game_over

    def check_game_over(self, roll):
        self.__game_over = not self.__is_subset_sum(self.__board.state, len(self.__board.state), roll)
        return self.__game_over

    def is_valid_move(self, roll, doors_to_shut):
        doors_to_shut = set(doors_to_shut)
        s = sum(doors_to_shut)
        if roll != s:
            print('Doors do not add up to dice roll.')
            return False

        for door in doors_to_shut:
            if not door in self.__board.state:
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
            return self.__is_subset_sum(set, n - 1, sum);

        # else, check if sum can be obtained
        # by any of the following
        # (a) including the last element
        # (b) excluding the last element
        return self.__is_subset_sum(set, n-1, sum) or self.__is_subset_sum(set, n-1, sum-set[n-1])

    def __str__(self):
        return self.__board.__str__()
