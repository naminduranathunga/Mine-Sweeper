
import Grid

def play_game(self, game):
    print("\n\t\tWELCOME TO MINESWEEPER GAME\n")
    game.print_grid(self)

    while True:
        try:
            option = input("Enter your move (e.g., A1F for flag or B2R for reveal): ").upper()

            if len(option) != 3 or option[0] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or \
                option[1] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or option[2] not in 'FR':
                raise ValueError("Invalid input. Please enter a valid move.")

            row, col, command = ord(option[1]) - 65, int(option[0]) - 1, option[2]

            if command == 'F':
                game.place_flag(self,row,col)

            elif command == 'R':
                if game.reveal(row,col):
                    if game.revealed_cells == game.max_cells:
                        print("\nCONGRATULATION! YOU WON.\n")

                else:
                    print("Game Over! You uncovered a mine. Start a new game.")
                    break


        except ValueError as e:
            print(f"Error: {e}")

def menu():
    # Menu
    while True:

        print("\n\t\tWELCOME TO MINESWEEPER GAME\n")
        print("\nMinesweeper Menu:")
        print("\t1. 10x10 Field (12 Mines)")
        print("\t2. 15x15 Field (18 Mines)")
        print("\t3. 20x20 Field (24 Mines)")
        print("\t4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            game = Grid.Grid(10, 12)
            play_game(game)
        elif choice == '2':
            game = Grid.Grid(15, 18)
            play_game(game)
        elif choice == '3':
            game = Grid.Grid(20, 24)
            play_game(game)
        elif choice == '4':
            print("Exiting Minesweeper. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")



menu()