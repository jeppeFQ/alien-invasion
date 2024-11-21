import pygame.font # Importerer Pygame's font-modul til at håndtere tekst og skrifttyper.


class Button:
    """
    En klasse til at bygge og håndtere knapper i spillet
    """

    def __init__(self, ai_game, msg):
        """
        Initialiserer knappegenskaber
        """
        # Henter en reference til spillets skærm, hvor knappen skal vises.
        self.screen = ai_game.screen
        # Henter skærmens rektangel for at placere knappen korrekt.
        self.screen_rect = self.screen.get_rect()

        # Definerer dimensioner og egenskaber for knappen.
        # Sætter knapstørrelsen til 200x50 pixels.
        self.width, self.height = 200, 50
        # Knapfarve, sat til en grøn nuance.
        self.button_color = (0, 135, 0)
        # Tekstfarve, sat til hvid.
        self.text_color = (255, 255, 255)
        # Definerer skrifttypen og størrelsen (48) for teksten på knappen.
        self.font = pygame.font.SysFont(None, 48)

        # Opretter en rektangel for knappen og centrerer den på skærmen.
        # Opretter en rektangel med dimensionerne for knappen.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # Centrerer knappen midt på skærmen.
        self.rect.center = self.screen_rect.center

        # Forbereder den besked, der skal vises på knappen, og sørger for, at det kun sker én gang.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """
        Omdanner beskeden til et grafisk billede og centrerer teksten på knappen
        """
        # Renderer beskeden som et billede med den valgte skrifttype og farver.
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        # Får rektanglen omkring besked-billedet.
        self.msg_image_rect = self.msg_image.get_rect()
        # Centrerer beskeden på knappen.
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """
        Tegner en blank knap og derefter beskeden ovenpå
        """
        # Tegner en fyldt rektangel (knappen) med knapfarven.
        self.screen.fill(self.button_color, self.rect)
        # Tegner beskeden ovenpå knappen.
        self.screen.blit(self.msg_image, self.msg_image_rect)