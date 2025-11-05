import pyxel
import parametres as param

class Menu:
    def __init__(self, etat: str):
        """
            Initialise la classe menu en fonction de l'etat du menu
        """
        self.etat: str = etat # Etat du menu

    def update(self) -> str:
        """
            Changer de menu
        """
        if self.etat == "menu":
            if pyxel.btnp(param.TOUCHE_COMMENCER):
                self.etat = "jeu" # Lancement d'une partie si la touche entrer est enfoncee et qu'on est dans le menu
            elif pyxel.btnp(param.TOUCHE_QUITTER):
                return pyxel.quit() # Quitter le jeu si la touche Q est enfoncee et qu'on est dans le menu
        elif self.etat == "pause":
            if pyxel.btnp(param.TOUCHE_REPRENDRE):
                self.etat = "jeu" # Reprendre du la partie si la touche P est enfoncee et qu'on est en pause
            elif pyxel.btnp(param.TOUCHE_QUITTER):
                return pyxel.quit() # Quitter le jeu si la touche Q est enfoncee et qu'on est en pause

    def draw(self):
        """
            Afficher le menu actuel
        """
        pyxel.cls(param.FOND_COUL) # Effacer l'ecran avec la couleur noire

        if self.etat == "menu":
            # Texte de l'ecran d'accueil
            pyxel.text(param.MENU_TITRE_X, param.MENU_TITRE_Y, "Bienvenue dans Pong!", param.COUL_TXT)
            pyxel.text(param.MENU_INSTRUCTIONS_X, param.MENU_TXT_Y_JOUER, "Appuie sur ENTREE pour jouer", param.COUL_TXT_SECOND)
            pyxel.text(param.MENU_INSTRUCTIONS_X, param.MENU_TXT_Y_QUITTER, "Appuie sur Q pour quitter", param.COUL_TXT_SECOND)

        elif self.etat == "pause":
            # Texte de l'ecran de pause
            pyxel.text(param.MENU_TITRE_X, param.MENU_TITRE_Y, "Pause", param.COUL_TXT)
            pyxel.text(param.MENU_INSTRUCTIONS_X, param.MENU_TXT_Y_JOUER, "Appuie sur P pour reprendre", param.COUL_TXT_SECOND)
            pyxel.text(param.MENU_INSTRUCTIONS_X, param.MENU_TXT_Y_QUITTER, "Appuie sur Q pour quitter", param.COUL_TXT_SECOND)