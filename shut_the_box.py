from random import randint

class Game:
    game_over = False
    board = { 1: True, 2: True, 3: True, 4: True,
    5: True, 6: True, 7: True, 8: True, 9: True }

    def dice_roll(self):
        if not self.board.get(7) and not self.board.get(8) and not self.board.get(9):
            return randint(1, 6)
        return randint(1,6) + randint(1,6)

    def shut_pieces(self, pieces):
        for piece in pieces:
            self.board[piece] = False

    def get_score(self):
        total = 0
        for key in self.board:
            if not self.board[key]:
                total += key
        return total

    def is_valid_move(self, pieces, dice_roll):
        if sum(pieces) != dice_roll:
            return False
        for piece in pieces:
            if not self.board[piece]:
                return False
        return True

    def shut_pieces(self, pieces):
        for piece in pieces:
            self.board[piece] = False

    def is_game_over(self, dice_roll, choice):
        if self.isSubsetSum(choice, len(choice), dice_roll):
            return True
        return False

    def isSubsetSum(self, set, n, sum) :

        # Base Cases
        if (sum == 0) :
            return True
        if (n == 0 and sum != 0) :
            return False

        # If last element is greater than
        # sum, then ignore it
        if (set[n - 1] > sum) :
            return self.isSubsetSum(set, n - 1, sum);

        # else, check if sum can be obtained
        # by any of the following
        # (a) including the last element
        # (b) excluding the last element
        return self.isSubsetSum(set, n-1, sum) or self.isSubsetSum(set, n-1, sum-set[n-1])

    def __str__(self):
        string = ''
        for piece in self.board:
            if self.board[piece]:
                string += str(piece) + ' '
        return string

game = Game()
while not game.game_over:
    roll = game.dice_roll()
    choice_invalid = True
    print(game.isSubsetSum(game.board, len(game.board), roll))
    while choice_invalid:
        print(game)
        print('Dice roll: ', roll)
        choice = list(map(int,input('Type which pieces you would like to shut separated by a space: ').split()))
        if game.is_valid_move(choice, roll):
            game.shut_pieces(choice)
            choice_invalid = False
        else:
            print('Invalid choice, please type again.')
