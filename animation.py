import random

import pygame


# mecanique d'animation
class AnimateSprite(pygame.sprite.Sprite):
    # definir les choses à faire à la création de l'entité
    def __init__(self, sprite_name, taille=(200, 200)):
        super(AnimateSprite, self).__init__()
        self.taille = taille
        # self.image = pygame.image.load('assets/'+ sprite_name + '.png')
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, self.taille)
        self.current_image = 0  # commencer l'anim à 0
        self.images = animaton.get(sprite_name)
        self.animation_mode = False
        self.start_animation()

    # demarre l'animation
    def start_animation(self):
        self.animation_mode = True

    # methoe pour animer le sprite
    def animate(self, loop=False):
        # verif anim actif
        if self.animation_mode:
            # passer à image suivante
            self.current_image += random.randint(0, 1)
            # verif si on a atteint la fin
            if self.current_image >= len(self.images):
                self.current_image = 0  # remet anim au depart

                if loop is False:
                    self.animation_mode = False  # desactive l'animation
            # modif image precedente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.taille)


# charger les images d'un sprite
def load_animations_images(sprite_name):
    # charge les 24 images de ce sprite dans le dossier correspondant
    images = []
    # recup le chemin
    path = f"assets/{sprite_name}/{sprite_name}"

    # boucle sur chq image dans le dossier
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
    # renvoi le contenu liste image
    return images


# defnir un dico qui contient image chargées de chaque sprite ( on regroupe pour gagner en perf )
animaton = {
    "mummy": load_animations_images('mummy'),
    "player": load_animations_images("player"),
    "alien": load_animations_images("alien")
}
