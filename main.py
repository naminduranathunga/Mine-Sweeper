
from Grid import print_grid

def menu(self):
    # Menu
    while True:
        print("\nMinesweeper Menu:")
        print("1. 10x10 Field (12 Mines)")
        print("2. 15x15 Field (18 Mines)")
        print("3. 20x20 Field (24 Mines)")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            game = Grid.Grid(10, 12)
            game.start_game()
        elif choice == '2':
            game = print_grid(15, 18)
            game.start_game()
        elif choice == '3':
            game = print_grid(20, 24)
            game.start_game()
        elif choice == '4':
            print("Exiting Minesweeper. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
