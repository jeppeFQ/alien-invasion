import pygame # Importerer "pygame": anvendes til håndtering af grafik, input og styring af spillet.
from pygame.sprite import Sprite# Importerer Sprite-klassen fra pygame for at håndtere spilobjekter som sprites.
                                # Læs her: https://www.pygame.org/docs/ref/sprite.html 


class Bullet(Sprite):
    """
    Klassen, der håndterer skuddende fra skibet
    """

    def __init__(self, ai_game):
        """
        Opretter et skud-object ud fra skibet aktuelle position
        """
        # Kører Sprite-klassens __init__-metode for at arve dens funktionalitet.
        super().__init__()
        # Reference til spillet skærm som defineret i ai-objectet.
        self.screen = ai_game.screen
        # Reference til spillet indstillinger som defineret i Settings-objectet.
        self.settings = ai_game.settings
        # Henter rektanglen (position samt dimensioner) for skib objectet. 
        self.color = self.settings.bullet_color

        # Opretter en rektangel-repræsentation af et skud ved positionen (0,0)
        # og justerer derefter position til at være ud fra skibets aktuelle position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Gemmer den vertikale (y) position som præcis decimaltal for præcis placering
        self.y = float(self.rect.y)

    def update(self):
        """
        Opdaterer skuddets position, når det bevæger sig opad.
        Denne metode kaldes for at opdatere skuddets position, hver gang skærmen opdateres.
        """
        # Flytter skuddet opad ved at reducere y-koordinaten baseret på skuddets hastighed.
        self.y -= self.settings.bullet_speed
        # Opdaterer rektanglen med den nye y-position.
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Tegner skuddet på skærmen.
        """
        # Tegner skuddet som en rektangel på skærmen.
        pygame.draw.rect(self.screen, self.color, self.rect)