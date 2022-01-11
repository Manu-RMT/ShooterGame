import pygame
from comet import Commet


# creer une classe pour gerer event
class CometFallEvent:
    # lors du chargement -> creer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 15
        # def un groupe pour lancer plusierus comettes
        self.all_comets = pygame.sprite.Group()
        self.game = game
        self.comet_mode = False

    # ajout pourcentage barre de progression + gestion rapidité
    def add_percent(self):
        self.percent += self.percent_speed / 100

    # si la barre est pleine
    def is_full_loaded(self):
        return self.percent >= 100

    # remet à 0 le pourcentage
    def reset_percent(self):
        self.percent = 0

    def launch_pluie_meteorite(self):
        # lancer plusieurs fois faut faire une boucle entre 1 et 10
        for i in range(1, 10):
            # on fait appraitre 1 commet
            self.all_comets.add(Commet(self))  # on lui passe la classe cometEvent pout l'utiliser dans commet

    # lance les comettes
    def launch_comet(self):
        # si c'est à 100 et qu'il y ai plus de monstre
        if self.is_full_loaded() and len(self.game.all_monster) == 0:
            self.launch_pluie_meteorite()
            self.comet_mode = True  # on lance event

    # geston comette
    def update_bar(self, surface):
        # ajout pourcentage à la barre
        self.add_percent()

        # barre de fond
        pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 15, surface.get_width(), 10])
        # barre courant
        pygame.draw.rect(surface,
                         (187, 11, 11), [0, surface.get_height() - 15, (surface.get_width() / 100) * self.percent, 10])
