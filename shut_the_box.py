from game import Game

def main():
    game = Game()
    while not game.get_game_over():
        print(game)

        doors_to_shut = []
        invalid_input = True
        while invalid_input:
            try:
                doors_to_shut = list(int(num) for num in input("Roll: " + str(game.get_roll()) + " -- doors to shut >> ").strip().split())
                if not game.is_valid_move(game.get_roll(), doors_to_shut):
                    print('Invalid move')
                    continue

                invalid_input = False
            except:
                print("Invalid input. Please try again.\n\n")

        for door in doors_to_shut:
            game.get_board().shut_door(door)

        game.tick()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
