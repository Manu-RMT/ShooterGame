import pygame
import constants

# gere les projectiles
class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super(Projectile, self).__init__()
        self.velocity = 7
        self.image = pygame.image.load('./assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))  # transforme image
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.player = player
        self.image_origin = self.image
        self.angle = 0

    def rotate(self):
        # tourner quand on le lance
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.image_origin, self.angle, 1)
        self.rect = self.image.get_rect(
            center=self.rect.center)  # reassigne le rectangle -rotation par rapport au centre

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        # si le projectile entre en collision avec un monstre
        for monster in  self.player.game.check_collision(self, self.player.game.all_monster):
            self.remove()
            #infliger des degats
            monster.damage(self.player.attaque)
        # verif si plus present dans l'ecran
        if self.rect.x > constants.CONST_LARGEUR:
            # on supprime le projectile du joueur
            # recup groupe de sprite et supprime sprite courant
            self.remove()

    def remove(self):
        self.player.all_projectiles.remove(self)

    def gun_left(self):
        self.rect.x = self.rect.x
        self.rect.x -= self.velocity
