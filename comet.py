import random

import pygame

# gere la comette
from monster import Mummy, Alien


class Commet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super(Commet, self).__init__()
        self.velocity = random.randint(2, 4 )
        self.image = pygame.image.load('./assets/comet.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 1000)
        self.rect.y = - random.randint(0, 1000)
        self.comet_event = comet_event  # ajout de cometevent

    def chuteComet(self):
        self.rect.y += self.velocity
        # si ca sort de l'ecran on supprime
        if self.rect.y >= 500:
            self.removeComet()

        # si il y a plus de boule de feu
        if len(self.comet_event.all_comets) == 0:
            # on relance les monstres et on remet à 0 le pourcentage de la barre
            self.comet_event.reset_percent()
            self.comet_event.game.comet_mode = False
        # si comet touche le joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_joueurs):
            # retirer comet
            self.removeComet()
            # mettre des degats au joueur
            self.comet_event.game.joueur.damage(20)

    # supprime la boule de feu
    def removeComet(self):
        self.comet_event.all_comets.remove(self)  # supprime la commet courante
        # on envoie le son de la comet
        self.comet_event.game.sound_manager.play('meteorite')
        # si il y a plus de comet on enleve le mode comet
        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_percent()
            # appraitre les 2 montres
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Alien)
            # ou self.comet_event.game.start()
