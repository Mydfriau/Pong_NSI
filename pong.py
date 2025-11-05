from Classes.raquette import Raquette
from Classes.filet import Filet
from Classes.balle import Balle
from Classes.menu import Menu
import pyxel
import parametres as param

class Pong:
    def __init__(self):
        """
            Initialise la classe Pong
        """
        pyxel.init(param.LARGEUR_FENETRE, param.HAUTEUR_FENETRE, title=param.TITRE_JEU)

        # Creer le menu
        self.menu: Menu = Menu(param.ETAT_MENU_DEPART)

        # Creer les raquettes gauche et droite
        self.raquette_gauche: Raquette = Raquette(param.RAQUETTE_G_X, param.RAQUETTE_G_Y, param.RAQUETTE_LARGEUR, param.RAQUETTE_HAUTEUR, param.RAQUETTE_COUL, param.RAQUETTE_VITESSE)
        self.raquette_droite: Raquette = Raquette(param.RAQUETTE_D_X, param.RAQUETTE_D_Y, param.RAQUETTE_LARGEUR, param.RAQUETTE_HAUTEUR, param.RAQUETTE_COUL, param.RAQUETTE_VITESSE)

        # Creer le filet
        self.filet: Filet = Filet()

        # Creer la balle
        self.balle: Balle = Balle(param.BALLE_X, param.BALLE_Y, param.BALLE_RAYON, param.BALLE_COUL, param.BALLE_VITESSE, param.BALLE_ACCELERATION)

        # Lancement de la boucle infinie de Pong en executant update et draw
        pyxel.run(self.update, self.draw)

    def update(self):
        """
            Mise a jour de chaque classe
        """
        if self.menu.etat in ["menu", "pause"]:
            return self.menu.update() # Mise a jour du menu si l'etat du menu est soit "menu" soit "pause"
        else:
            # Mettre en pause ou quitter en fonction des touches pressees
            if pyxel.btnp(param.TOUCHE_PAUSE):
                self.menu.etat = "pause"
            elif pyxel.btnp(param.TOUCHE_QUITTER):
                return pyxel.quit()

            # Deplacements des raquettes en fonction des touches pressees
            self.raquette_gauche.update({ "up": param.TOUCHE_RAQUETTE_G_H, "down": param.TOUCHE_RAQUETTE_G_B })
            self.raquette_droite.update({ "up": param.TOUCHE_RAQUETTE_D_H, "down": param.TOUCHE_RAQUETTE_D_B })

            # Deplacements de la balle et detections des collisions
            self.balle.update()
            self.raquette_gauche.colision(self.balle)
            self.raquette_droite.colision(self.balle)

    def draw(self):
        """
            Gerer l'affichage et les dessins
        """
        if self.menu.etat in ["menu", "pause"]:
            return self.menu.draw() # Dessiner le menu si l'etat du menu est soit "menu" soit "pause"
        else:
            pyxel.cls(param.FOND_COUL) # Effacer l'ecran en noire
            # Dessiner les elements du jeu
            self.raquette_gauche.draw()
            self.raquette_droite.draw()
            self.filet.draw()
            self.balle.draw()

# Demarrage du jeu
Pong()
