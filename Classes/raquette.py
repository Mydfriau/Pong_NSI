import pyxel
from Classes.balle import Balle

class Raquette:
    def __init__(self, x: int, y: int, l: int, h: int, coul: int, v_depart: int):
        """
            Initialise la raquette avec ses coordonnees, dimensions, couleur et vitesse.
        """
        self.x: int = x # Position x de la raquette
        self.y: int = y # Position y de la raquette
        self.l: int = l # Largeur de la raquette
        self.h: int = h # Hauteur de la raquette
        self.coul: int = coul # Couleur de la raquette
        self.v_depart: int = v_depart # Vitesse de la raquette

    def update(self, keys: dict[str, int]):
        """
            Mise a jour des deplacements verticaux de la raquette
        """
        if pyxel.btn(keys["up"]) and self.y > 0:
            self.y -= self.v_depart  # Monter la raquette si la touche du haut est enfoncee
        elif pyxel.btn(keys["down"]) and self.y + self.h < pyxel.height:
            self.y += self.v_depart  # Descendre la raquette si la touche du bas est enfoncee

    def colision(self, balle: Balle) -> None:
        """
            Gerer la collision entre la raquette et la balle
        """
        bord = {
            "balle": {
                "haut": balle.y - balle.r, # Bord haut de la balle
                "gauche": balle.x - balle.r, # Bord gauche de la balle
                "bas": balle.y + balle.r, # Bord bas de la balle
                "droite": balle.x + balle.r # Bord droit de la balle
            },
            "raquette": {
                "bas": self.y + self.h, # Bord bas de la raquette
                "droite": self.x + self.l # Bord droit de la raquette
            }
        }

        # Verifier si la balle entre en collision avec l'une des deux raquette
        if bord["balle"]["gauche"] <= bord["raquette"]["droite"] \
        and bord["balle"]["droite"] >= self.x \
        and bord["balle"]["bas"] >= self.y \
        and bord["balle"]["haut"] <= bord["raquette"]["bas"]:
            balle.vx = -balle.vx * balle.a  # Inverser la direction x de la balle avec une acceleration

    def draw(self) -> None:
        """
            Dessiner la raquette
        """
        pyxel.rect(self.x, self.y, self.l, self.h, self.coul) # Dessiner la raquette