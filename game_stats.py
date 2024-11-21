class GameStats:
    """Klasse der holder styr på statistikken for spillet"""

    def __init__(self, ai_game):
        """
        Initialiserer spillets statistik, når spillet starter
        """
        # Henter referencer til spillets indstillinger.
        self.settings = ai_game.settings
        # Initialiserer statistikker, der kan ændre sig under spillets gang.
        self.reset_stats()

        # Vi sætter highscore som 0 fra starten, indtil en ny opnås. 
        self.high_score = 0
        self.high_score = 0

    def reset_stats(self):
        """
        Nulstiller den statistik, der kan ændre sig under spillet
        """
        # Sætter antallet af tilbageværende liv baseret på spillets indstillinger.
        self.ships_left = self.settings.ship_limit
        # Nulstiller score til 0, når et nyt spil starter.
        self.score = 0
        # Sætter spillets startniveau til 1.
        self.level = 1