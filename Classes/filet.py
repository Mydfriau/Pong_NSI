import pyxel
import parametres as param

class Filet:
    def __init__(self):
        """
            Initialise la classe Filet
        """
        self.x = pyxel.width // 2 # Position x du filet 

    def draw(self):
        """
            Dessiner le filet
        """
        # Dessiner le filet
        pyxel.rect(self.x, 0, param.FILET_L, pyxel.height, param.FILET_COUL)