import pygame
from projectile import Projectile
import animation

class Player(animation.AnimateSprite):
    # faut transformer en sprite (composant graphique)
    # caracterise un joueur
    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.vie = 100  # vie courant
        self.vie_max = 100  # v ie max
        self.attaque = 17
        self.velocity = 3  # vitesse de deplacement
        self.all_projectiles = pygame.sprite.Group()  # pour lancer plusieurs projectiles
        # on a besoin de recup coordonnée car ca bouge dans la surface
        self.rect = self.image.get_rect()  # recup rectangle ici l'image
        # position absisse
        self.rect.x = 500
        # position ordonnée
        self.rect.y = 500

        # maj animation

    def update_animation(self):
        self.animate()

    def damage(self, vie_retier):
        if self.vie - vie_retier > vie_retier:
            self.vie -= vie_retier
        else:
            #si je joueur n'a plus de point de vie
            self.game.game_over()

    def launch_projectile(self):
        # creer nouvelle instance de projectile
        # ajout du self pour accer à tout le joueur dans ke projetile
        self.all_projectiles.add(Projectile(self))
        #on lance l'animation au moment de lancer le projectile
        self.start_animation()
        #on joue le son
        self.game.sound_manager.play("tir")


    # postion + maj jauge
    def maj_barre_de_vie(self, surface):
        # dessin barre de vie
        pygame.draw.rect(surface, (226, 224, 216), [self.rect.x + 50, self.rect.y + 20, self.vie_max, 5])
        pygame.draw.rect(surface, (39, 198, 41),
                         [self.rect.x + 50, self.rect.y + 20, self.vie, 5])  # pos x,y ; largeur ; hauteur bar

    def move_right(self):
        # si le joueur n'est pa en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

# region NOTE
# get_rect = recuperer cordonnée ici de l'image player.png sous la forme d'un rectangle
# SPRITE pour trnasformer une classe en composant graphique
# endregion
