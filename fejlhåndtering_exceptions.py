import sys
import pygame

class AlienInvasion:
    """ xxx """

    def __init__(self):
        """ xxx """
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(sefl):
        """ xxx """
        while True:
            # xxx
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # xxx
            pygame.display.flip()

if __name__ == '__main__':
    # xxx
    ai = AlienInvasion()
    ai.run_game()