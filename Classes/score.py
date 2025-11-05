import pyxel
import parametres as param

class Score:
    def __init__(self):
        """
            Initialise la classe Score
        """
        # Dictionnaire qui stocke les points des deux joueurs
        self.pt: dict[str, int] = {
            "gauche": param.SCORE_DEPART, # Points du joueur gauche
            "droite": param.SCORE_DEPART # Points du joueur droit
        }

    def add_point(self, cote: str) -> int:
        """
            Ajouter un point au joueur specifie.
        """
        if cote == "gauche":
            # Ajouter un point au joueur gauche
            self.pt["gauche"] += param.SCORE_I
        elif cote == "droite":
            # Ajouter un point au joueur droit
            self.pt["droite"] += param.SCORE_I

    def draw(self):
        """
            Affichage des scores des deux joueurs
        """
        # Affichage du score du joueur gauche
        pyxel.text(param.SCORE_X_G, param.SCORE_Y, f"{self.pt['gauche']}", param.SCORE_COUL)

        # Affichage du score du joueur droit
        pyxel.text(param.SCORE_X_D, param.SCORE_Y, f"{self.pt['droite']}", param.SCORE_COUL)
