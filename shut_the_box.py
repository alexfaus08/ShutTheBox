from game import Game
from random import randint

def roll_die():
    return randint(1, 6)

def main():
    game = Game()
    while not game.game_over:
        print(game)

        roll = roll_die()
        if game.board.requires_two_dice():
            roll += roll_die()

        if game.check_game_over(roll):
            break

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

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
