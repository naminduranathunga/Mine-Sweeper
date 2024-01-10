"""
main.py

Author:
D.R.K. DISANAYAKA - 21/ENG/022
"""
import Grid

def play_game(game):
    print("\n\t\tWELCOME TO MINESWEEPER GAME\n")
    
    while True:
        try:
            game.print_grid()

            option = input("\nEnter your move (e.g., AAF for flag or BBR for reveal): ").upper()

            if len(option) == 3 and \
                option[0].isalpha() and option[1].isalpha() and option[2] in 'FR':
                col, row, command = ord(option[0].upper()) - 65, ord(option[1].upper()) - 65, option[2]
            else:
                raise ValueError("\nInvalid input. Please enter a valid move.")

            if command == 'F':
                game.place_flag(col,row)

            elif command == 'R':
                if game.reveal(col,row):
                    if game.revealed_cells == game.max_cells:
                        print("\nCONGRATULATION! YOU WON.\n")


                else:
                    print("\nGame Over! You uncovered a mine. Start a new game.")
                    break


        except ValueError as e:
            print(f"Error: {e}")

def menu():
    # Menu
    while True:

        print("\n======================================================================")
        print("\n\t\t\tMINESWEEPER GAME\n")
        print("======================================================================")
        print("\nMinesweeper Menu:")
        print("\t1. 10x10 Field (12 Mines)")
        print("\t2. 15x15 Field (18 Mines)")
        print("\t3. 20x20 Field (24 Mines)")
        print("\t4. Quit")

        choice = input("\nEnter your choice (1-4): ")

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
            print("\nExiting Minesweeper... \n\n\t\tGoodbye!\n\n")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")



menu()