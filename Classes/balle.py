from Classes.score import Score
from random import randint
import pyxel

class Balle:
    def __init__(self, x_depart: int, y_depart: int, r: int, coul: int, v_depart: float, a: float):
        """
            Initialise la balle en fonction de sa position, son rayon, sa couleur, ses vecteurs de deplacement (grace au vecteur de deplacement on a la vitesse), son acceleration et sa vitesse maximale.
        """
        self.score: Score = Score() # Creer le score
        self.x_depart: int = x_depart # Position x de depart
        self.y_depart: int = y_depart # Position y de depart
        self.x: int = x_depart # Position x actuelle
        self.y: int = y_depart # Position y actuelle
        self.r: int = r # Rayon de la balle
        self.coul: int = coul # Couleur de la balle
        self.v_depart: int = v_depart # Vitesse de depart
        self.vx: int = randint(-int(v_depart), int(v_depart)) # Vecteur vitesse x
        self.vy: int = randint(-int(v_depart), int(v_depart)) # Vecteur vitesse y
        self.a: float = a # Acceleration de la balle

        # Empecher que la balle s'arrete
        while self.vx == 0 or self.vy == 0:
            self.vx: int = randint(-int(v_depart), int(v_depart)) # Nouveau vecteur vitesse x si vecteur vitesse x nul
            self.vy: int = randint(-int(v_depart), int(v_depart)) # Nouveau vecteur vitesse y si vecteur vitesse y nul

    def update(self) -> float:
        """
            Gerer les deplacement et les collisions de la balle avec les bords inclus
        """
        self.x += self.vx # Deplacement en x de la balle
        self.y += self.vy # Deplacement en y de la balle

        # Dictionnaire des bords de la balle
        bord = {
            "haut": self.y - self.r, # Bord haut de la balle
            "gauche": self.x + self.r, # Bord gauche de la balle
            "bas": self.y + self.r, # Bord bas de la balle
            "droite": self.x - self.r # Bord droit de la balle
        }

        # Verifier si il y a une collision avec le haut ou le bas de l'ecran
        if bord["haut"] < 0 or bord["bas"] > pyxel.height:
            self.vy = -self.vy # Modifier la direction y a son oppose


        # Ajouter les points au joueur specifie si il reussi a faire passer la balle de l'autre cote
        elif bord["gauche"] < 0 or bord["droite"] > pyxel.width:
            if self.x < 0:
                self.score.add_point("droite") # Ajouter un point au joueur droit si la balle depasse le bord gauche
            elif self.x > pyxel.width:
                self.score.add_point("gauche") # Ajouter un point au joueur gauche si la balle depasse le bord droit
            self.reset() # Remettre la balle a sa position de depart


    def reset(self) -> None:
        """
            Remet en place la balle avec la vitesse augmentee.
        """
        self.v_depart: int = self.v_depart # Remettre la vitesse de depart a la valeur initiale

        self.x: int = self.x_depart # Remettre la la balle a sa position x de depart
        self.y: int = self.y_depart # Remettre la la balle a sa position y de depart

        self.vx: int = randint(-int(self.v_depart), int(self.v_depart)) # Nouveau vecteur vitesse x
        self.vy: int = randint(-int(self.v_depart), int(self.v_depart)) # Nouveau vecteur vitesse y

        # Empêcher que la balle s'arrete
        while self.vx == 0 or self.vy == 0:
            self.vx: int = randint(-int(self.v_depart), int(self.v_depart)) # Nouveau vecteur vitesse x si vecteur vitesse x nul
            self.vy: int = randint(-int(self.v_depart), int(self.v_depart)) # Nouveau vecteur vitesse y si vecteur vitesse y nul

    def draw(self):
        """
            Dessiner la balle et dessiner le score
        """
        pyxel.circ(self.x, self.y, self.r, self.coul) # Dessiner la balle
        return self.score.draw() # Dessiner le score
