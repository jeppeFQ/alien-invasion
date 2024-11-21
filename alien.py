import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """
    Klassen der repræsenterer og styrer aliens (fjender)
    """

    def __init__(self, ai_game):
        """
        Initialiserer aliens og deres startpositioner
        """
        # Kører Sprite-klassens __init__-metode for at arve dens funktionalitet.
        super().__init__()
        # Reference til spillet skærm som defineret i ai-objectet.
        self.screen = ai_game.screen
        # Reference til spillet indstillinger som defineret i Settings-objectet.
        self.settings = ai_game.settings

        # Indlæser billedet af fjenden (alien) og definerer rektanglen (dimensioner og position).
        # Indlæser billede fra en fil.
        self.image = pygame.image.load('images/alien.bmp')
        # Får rektanglen for alien objectet (som bruges til at placere og tegne den).
        self.rect = self.image.get_rect()

        # Starter hver ny alien så tæt på skærmens øverste venstre hjørne som muligt
        # Placerer fjenden med lidt margin fra venstre kant af skærmen.
        self.rect.x = self.rect.width
        # Placerer fjenden lidt under toppen af skærmen.
        self.rect.y = self.rect.height

        # Placering som decimal koordinat
        self.x = float(self.rect.x)

    def check_edges(self):
        """
        Tjekker om alien objectet rammer kanten af skærmen. 
        Returnerer True, hvis de gør.
        """
        # Henter skærmens dimensioner.
        screen_rect = self.screen.get_rect()
        # Tjekker om aliens har ramt enten højre eller venstre kant af skærmen.
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """
        Opdaterer aliens position, så den bevæger sig til højre eller venstre.
        """
        # Bevæg aliens til højre eller venstre afhængigt af flådens retning.
        # Opdaterer aliens vandrette position.
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        # Opdaterer aliens rektanglens position, så den visuelle placering opdateres.
        self.rect.x = self.x