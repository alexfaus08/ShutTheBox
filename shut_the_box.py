from game import Game

def main():
    game = Game()
    while not game.get_game_over():
        print(game)

        boxes_to_shut = []
        invalid_input = True
        while invalid_input:
            try:
                boxes_to_shut = list(int(num) for num in input("Roll: " + str(game.get_roll()) + " -- boxes to shut >> ").strip().split())
                game.shut_boxes(boxes_to_shut)
                invalid_input = False
            except ValueError as err:
                print(err)

        game.tick()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
