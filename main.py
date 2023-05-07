from src.Game import Game
import pygame

def main():
    game = Game()

    while game.is_running():
        game.display_screen()
        game.display_player()
        game.display_projectiles()
        game.display_aliens()
        game.update_screen()

if __name__ == "__main__":
    main()