import pygame
import random
import animation


class Monster(animation.AnimateSprite):

    def __init__(self, game, type_monstre, taille, offset=0):
        super(Monster, self).__init__(type_monstre, taille)
        self.game = game
        self.vie = 100
        self.max_vie = 100
        self.attaque = 0.3
        # self.image = pygame.image.load('./assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1100 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.start_animation()
        self.montant_point = 1

    def set_speed(self, vitesse):
        self.default_speed = vitesse
        self.velocity = random.randint(1, 3)

    def set_montant_point(self, point):
        self.montant_point = point

    def damage(self, attaque_subit):
        # inflier les degat
        self.vie -= attaque_subit
        # si la vie vaut 0 on supprimzz le monstre
        if self.vie <= 0:
            # reapparaitre ccomme un nouveau monstre
            self.rect.x = 1100 + random.randint(0, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.vie = self.max_vie

            # on rajoute 1 au score depuis game
            self.game.add_score(self.montant_point)

            # si la barre est à 100
            if self.game.evenementComet.is_full_loaded():
                print("barrre 100 %")
                # on supprime le mmonstre du jeu
                self.game.all_monster.remove(self)

                # appel de la methode pour declencher les commetes
                self.game.evenementComet.launch_comet()

    # maj animation
    def update_animation(self):
        self.animate(loop=True)

    # postion + maj jauge
    def maj_barre_de_vie(self, surface):
        # definir position jauge  + largeur + epaisseur
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.vie, 5]  # pos x,y ; largeur ; hauteur bar
        # position arriere plan jauge de vie
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_vie, 5]  # pos x,y ; largeur ; hauteur bar
        # dessin barre de vie
        pygame.draw.rect(surface, (226, 224, 216), back_bar_position)
        pygame.draw.rect(surface, (111, 210, 46), bar_position)

    def walk(self):
        # le deplacement ne se fait si pas collision avec un groupe de joueurs
        if not self.game.check_collision(self, self.game.all_joueurs):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # inflige degat
            self.game.joueur.damage(self.attaque)


# classe pour la momie
class Mummy(Monster):
    def __init__(self, game):
        super(Mummy, self).__init__(game, "mummy", (130, 130))
        self.set_speed(4)
        self.set_montant_point(5)


class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, 'alien', (300, 300), 140)
        self.vie = 300
        self.max_vie = 300
        self.attaque = 0.8
        self.set_speed(2)
        self.set_montant_point(15)
