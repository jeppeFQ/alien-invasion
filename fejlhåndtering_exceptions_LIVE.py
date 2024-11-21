import sys
import pygame

class AlienInvasion:
    """ xxx """

    def __init__(self):
        """ xxx """
        pygame.init()

        try:
            self.screen = pygame.display.set_mode((-1200, 800))
            pygame.display.set_caption("Alien Invasion")
        except:
            print(f"\n\nFEJL: forkerte dimensioner på skærm.\n\n")
            sys.exit(1)  # Afslut programmet, hvis skærmen ikke kan initialiseres
    
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