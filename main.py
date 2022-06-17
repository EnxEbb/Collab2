"""
This class just calls other classes as necessary.
"""

from game import Game

g = Game()

def main():
    while g.running:
        g.curr_menu.display_menu()
        g.game_loop()


if __name__ == "__main__":
    main()