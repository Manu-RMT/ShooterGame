import pygame.display
from pygame import *
from game import Game
import constants
import math

pygame.init()

# definir une clock
clock = pygame.time.Clock()
FPS = 120

# region param element ecran
# generer la fenetre de jeu
pygame.display.set_caption("Shooter Game")
# surface
print(constants.CONST_LARGEUR)
screen = pygame.display.set_mode((constants.CONST_LARGEUR, constants.CONST_LONGEUR))
# arriere plan
background = pygame.image.load("./assets/bg.jpg")
# region importer banniere
banner = pygame.image.load('./assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
# import bouton pour jouer
button_player = pygame.image.load('./assets/button.png')
button_player = pygame.transform.scale(button_player, (400, 150))
button_player_rect = button_player.get_rect()  # composant pour repositionnement
button_player_rect.x = math.ceil(screen.get_width() / 3)
button_player_rect.y = math.ceil(screen.get_height() / 1.75)
# region jeu
# charge le jeu
game = Game()
# endregion

# endregion

# region run fenetre
# maintien fenetre
running = True
# boucle pour rester ouvert la page
while running:
    # appliquer arriere plan
    screen.blit(background, (0, -200))
    # gesion du jeu
    # si le jeu est lancé
    if game.is_playing:
        game.update(screen)
    # verifier si le jeu n'a pas commencé
    else:
        # ajout ecfan de bienvenue
        screen.blit(banner, (math.ceil(constants.CONST_LARGEUR / 3.5), 0))
        # bouton de demarrage
        screen.blit(button_player, button_player_rect)
    # mise à jour de l'ecran
    pygame.display.flip()

    # region EVENEMENT DANS LE JEU
    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # si l"evenement est de fermer la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture de Shooter Game")

        # on sait en temps reel quelle touche et appuyer par le joueur
        # dico qui met à true la touche selemectionné
        # quand on appuie sur une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True  # touche active
            # appuie sur espace
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.joueur.launch_projectile()
                else:  # sinon le bouton espace lance le jeu
                    game.start()
                    # on lance le son du jeu
                    game.sound_manager.play('click')

        # quand on lache une touche
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # si le bouton est en collision avece le bouton
            if button_player_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancer
                game.start()
                # on lance le son du jeu
                game.sound_manager.play('click')
    # fixe FPS
    clock.tick(FPS)

    # endregion

# endregion


# region NOTE
# pour generer une image  : 3 etapes : on import l'image - on l'applique à la surface - on met à jour la surface
# BLIT : injecte image dans la surface
# GESTION DES COLLISION : FAUT CREER UN GROUPE DE CHAQYE COTE POUR COMPRARER
# endregion

# region idees ameliorations
# ajouter un coup special quand un jour à atteint un nb de points suffisants
# barre de spé à rajouter
# endregion
