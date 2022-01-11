import pygame
import constants
from monster import Monster, Mummy, Alien
from cometEvent import CometFallEvent
from player import Player
from sound import SoundManager


class Game:
    def __init__(self):
        # defini si le jeu à commencer ou non
        self.is_playing = False
        # genere notre joueur
        self.all_joueurs = pygame.sprite.Group()
        self.joueur = Player(self)
        self.all_joueurs.add(self.joueur)  # pour stoper le monstre avec un groupe de personne
        self.all_monster = pygame.sprite.Group()  # pour regrouper plusieurs monstre
        self.pressed = {}  # sauvegarde touche
        self.evenementComet = CometFallEvent(self)  # genere event et on donne la classe game à commetEvent
        self.font = pygame.font.Font("assets/default_text.ttf", 25)
        self.score = 0  # score = 0
        self.sound_manager = SoundManager()

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)  # cree directement au demrage un monstre
        self.spawn_monster(Mummy)  # cree directement au demrage un monstre
        self.spawn_monster(Alien)  # cree directement au demrage un monstre

    def game_over(self):
        # remettre une nouvelle instace de jeu,retirer les monstres, remettre les jouerus à 100 de vie ,jeu en attente
        self.all_monster = pygame.sprite.Group()  # vide les monstres
        self.evenementComet.all_comets = pygame.sprite.Group()  # nouvelle instance pour vider le groupe
        self.evenementComet.reset_percent()  # on relance la barre
        self.joueur.vie = self.joueur.vie_max  # remet à 100% les vies
        self.is_playing = False  # permet de stopper le jeu
        self.score = 0  # on remet à 0
        self.sound_manager.play('game_over')

    def update(self, screen):
        # region score
        # affiche le score sur l'ecan 3 etapes
        # font = pygame.font.SysFont("monospace", 14)
        score_text = self.font.render(f"Score : {self.score}", True, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # endregion
        # region joueur
        # appliquer image joueur et position
        screen.blit(self.joueur.image, (self.joueur.rect))
        # actualiser barre de vie du joueur
        self.joueur.maj_barre_de_vie(screen)
        # animation joueur
        self.joueur.update_animation()

        # endregion
        # region projectile et monstre et comets
        # PROJECTILE
        # recup les projectiles du joueur
        for projectile in self.joueur.all_projectiles:
            projectile.move()
        # appliquer tous l"ensemble des images de mon groupe de projectiles
        self.joueur.all_projectiles.draw(screen)

        # MONSTRE
        # recupere la marche pour chaque monstre
        # recupere chauqe barre de vie
        # animation joueur
        for monstre in self.all_monster:
            monstre.walk()
            monstre.maj_barre_de_vie(screen)
            monstre.update_animation()
        # appliquer tous l"ensemble des images de mon groupe monstre
        self.all_monster.draw(screen)

        # COMETS
        # barre avancement du jeu
        self.evenementComet.update_bar(screen)
        # appliquer le groupe de commets
        self.evenementComet.all_comets.draw(screen)
        # recupre chaque comet
        for comet in self.evenementComet.all_comets:
            comet.chuteComet()
        # endregion
        # region touche
        # verifie si le joueur veut aller à gauche ou à droite et bloque gauche et droite
        if self.pressed.get(pygame.K_LEFT) and self.joueur.rect.x > 0:
            self.joueur.move_left()
        if self.pressed.get(pygame.K_RIGHT) and self.joueur.rect.x + self.joueur.rect.width < constants.CONST_LARGEUR:
            self.joueur.move_right()

        # endregion

        # endregion

    def add_score(self, points=1):
        self.score += points

    # param 1 element graphique à comparer
    # param 2 comparé à un groupe de sprite
    def check_collision(self, sprite, groupe):
        # check une entité avec un groupe mais ne permet pas la colision des monstres donc il faut aussi un groupe de jouerusv
        return pygame.sprite.spritecollide(sprite, groupe, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monstre_class_name):
        self.all_monster.add(monstre_class_name.__call__(self))
