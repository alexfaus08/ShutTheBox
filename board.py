class Board:
    def __init__(self):
        self.state = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def shut_door(self, n):
        self.state.remove(n)

    def get_score(self):
        return sum(self.state)

    def requires_two_dice(self):
        return 7 in self.state or 8 in self.state or 9 in self.state

    def __str__(self):
        return ' '.join(map(str, self.state))
