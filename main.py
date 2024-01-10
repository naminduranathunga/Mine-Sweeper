
import Grid


def menu(self):
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
                if (row, col) in self.place_mines:
                    game.print_grid(self)
                    print("Game Over! You uncovered a mine. Start a new game.")
                    break
                else:
                    # updating the field when location is revealed 
                    print("Location revealed. Game logic update pending.")
                    game.print_grid(self)

        except ValueError as e:
            print(f"Error: {e}")


# import Grid
# from Grid import print_grid

# def menu(self):
#     # Menu
#     while True:

#         print("\n\t\tWELCOME TO MINESWEEPER GAME\n")
#         print("\nMinesweeper Menu:")
#         print("\t1. 10x10 Field (12 Mines)")
#         print("\t2. 15x15 Field (18 Mines)")
#         print("\t3. 20x20 Field (24 Mines)")
#         print("\t4. Quit")

#         choice = input("Enter your choice (1-4): ")

#         if choice == '1':
#             game = Grid.Grid(10, 12)
#             play_game(game)
#         elif choice == '2':
#             game = Grid.Grid(15, 18)
#             play_game(game)
#         elif choice == '3':
#             game = Grid.Grid(20, 24)
#             play_game(game)
#         elif choice == '4':
#             print("Exiting Minesweeper. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter a number between 1 and 4.")


# def play_game(self):
#     print("\n\t\tWELCOME TO MINESWEEPER GAME\n")
#     print_grid(self)

#     while True:
#         try:
#             option = input("Enter your move (e.g., A1F for flag or B2R for reveal): ").upper()

#             if len(option) != 3 or option[0] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or \
#                    option[1] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or option[2] not in 'FR':
#                     raise ValueError("Invalid input. Please enter a valid move.")

#             row, col, command = ord(option[1]) - 65, int(option[0]) - 1, option[2]

#             if command == 'F':
#                 if self.flags > 0 and self.field[row][col] == 'c':
#                     self.field[row][col] = 'F'
#                     self.flags -= 1
#                     print(f"Flag placed at {option[0]}{option[1]}")
#                 else:
#                     print("Invalid flag placement. Try again.")

#             elif command == 'R':
#                 if (row, col) in self.placed_mines:
#                     self.display_field()
#                     print("Game Over! You uncovered a mine. Start a new game.")
#                     break
#                 else:
#                     # Your logic to update the field when location is revealed goes here
#                     print("Location revealed. Game logic update pending.")
#                     self.display_field()

#         except ValueError as e:
#                 print(f"Error: {e}")
