from lib.packet.action.MoveActionPacket import MoveActionPacket
from src.Game import Game
import pygame

def main():
    pygame.init()
    game = Game()

    while game.is_running():
        game.update_all()

        for m_f in MoveActionPacket.MOVEMENT_FORWARD:
            if game.pressed_keys.get(m_f):
                game.player.move('0xF')
        for m_b in MoveActionPacket.MOVEMENT_BACKWARD:
            if game.pressed_keys.get(m_b):
                game.player.move('0xB')

        # Si le joueur a fermé la fenetre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.set_running(False)
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                game.pressed_keys[event.key] = True

                if event.key == pygame.K_SPACE:
                    game.player.shoot()
            elif event.type == pygame.KEYUP:
                game.pressed_keys[event.key] = False

if __name__ == "__main__":
    main()