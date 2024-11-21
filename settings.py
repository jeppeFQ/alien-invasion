class Settings:
    """
    En klasse til at gemme alle indstillinger for Alien Invasionspillet
    """

    def __init__(self):
        """
        Initialiserer spillets statiske indstillinger
        """
        # Skærmindstillinger
        # Bredden af spillets vindue (i pixels).
        self.screen_width = 600
        # Højden af spillets vindue (i pixels).
        self.screen_height = 800
        # Baggrundsfarven (RGB-værdi: lys grå).
        self.bg_color = (230, 230, 230)
        # Rumskibsindstillinger
        # Antal liv (rumskibe) spilleren har i begyndelsen af spillet.
        self.ship_limit = 3
        # Skudindstillinger
        # Bredden af skud (i pixels).
        self.bullet_width = 3
        # Højden af skud (i pixels).
        self.bullet_height = 15
        # Farven på skud (RGB-værdi: mørkegrå).
        self.bullet_color = (60, 60, 60)
        # Maksimalt antal skud, som spilleren kan affyre samtidigt.
        self.bullets_allowed = 3
        # Alien (fjende) indstillinger
        # Hvor meget fjenderne rykker nedad, når de ændrer retning.
        self.fleet_drop_speed = 10
        # Hvor hurtigt spillets hastighed øges
        # Spilhastigheden øges med 10% hver gang tempoet stiger.
        self.speedup_scale = 1.1
        # Hvor hurtigt pointværdien af aliens øges
        # Alien-point øges med 50% hver gang spilleren går op i niveau.
        self.score_scale = 1.5
        # Kalder metoden til at initialisere dynamiske indstillinger.
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        Initialiserer de indstillinger, der ændrer sig gennem
        spillet
        """
        # Hastighedsindstillinger
        # Hastigheden for spillerens rumskib.
        self.ship_speed = 1.5
        # Hastigheden for skud affyret af rumskibet.
        self.bullet_speed = 2.5
        # Hastigheden for aliens bevægelse.
        self.alien_speed = 1.0
        # Flåderetning: 1 betyder, at fjenderne bevæger sig til højre;
        # -1 betyder, at de bevæger sig til venstre.
        # Initialiserer flådens retning til at bevæge sig til højre.
        self.fleet_direction = 1
        # Pointindstillinger
        # Antal point, spilleren får for at skyde en alien i starten af spillet.
        self.alien_points = 10

    def increase_speed(self):
        """
        Øger hastighedsindstillingerne og pointværdien af fjenderne
        """
        # Øger rumskibets hastighed.
        self.ship_speed *= self.speedup_scale
        # Øger skudhastigheden.
        self.bullet_speed *= self.speedup_scale
        # Øger fjendernes bevægelseshastighed.
        self.alien_speed *= self.speedup_scale
        # Øger pointværdien for aliens og afrunder til et helt tal.
        self.alien_points = int(self.alien_points *
        self.score_scale)   