from lib.packet.action.MoveActionPacket import MoveActionPacket
from src.Game import Game
import pygame

def main():
    pygame.init()
    game = Game()

    while game.is_running():
        game.update_all()
        print(str(game.entity_manager.projectiles))

        # Si le joueur a fermé la fenetre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.set_running(False)
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key in MoveActionPacket.MOVEMENT_FORWARD:
                    game.player.move('0xF')
                elif event.key in MoveActionPacket.MOVEMENT_BACKWARD:
                    game.player.move('0xB')
                elif event.key == pygame.K_SPACE:
                    game.player.shoot()

if __name__ == "__main__":
    main()