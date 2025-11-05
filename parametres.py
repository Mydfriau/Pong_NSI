import pyxel

# Configuration basique de Pong
LARGEUR_FENETRE: int = 160 # Largeur de la fenêtre
HAUTEUR_FENETRE: int = 120 # Hauteur de la fenêtre
TITRE_JEU: str = "Pong" # Titre affiche dans la fenêtre
ETAT_MENU_DEPART: str = "menu" # Menu de depart
FOND_COUL: int = 0 # Couleur du fond de l'ecran

# Raquette
RAQUETTE_G_X: int = 24 # Position X de la raquette gauche
RAQUETTE_G_Y: int = 70 # Position Y de la raquette gauche
RAQUETTE_D_X: int = 136 # Position X de la raquette droite
RAQUETTE_D_Y: int = 86 # Position Y de la raquette droite
RAQUETTE_LARGEUR: int = 2 # Largeur des raquettes
RAQUETTE_HAUTEUR: int = 8 # Hauteur des raquettes
RAQUETTE_COUL: int = 7 # COUL des raquettes
RAQUETTE_VITESSE: int = 3 # Vitesse des raquettes

# Balle
BALLE_X: int = 94 # Position X initiale de la balle
BALLE_Y: int = 66 # Position Y initiale de la balle
BALLE_RAYON: int = 2 # Rayon de la balle
BALLE_COUL: int = 7 # COUL de la balle
BALLE_VITESSE: int = 1 # Vitesse initiale de la balle
BALLE_ACCELERATION: float = 1.05 # Facteur d'acceleration apres collision

# Contrôles
TOUCHE_RAQUETTE_G_H: int = pyxel.KEY_Z # Monter raquette gauche
TOUCHE_RAQUETTE_G_B: int = pyxel.KEY_S # Descendre raquette gauche
TOUCHE_RAQUETTE_D_H: int = pyxel.KEY_UP # Monter raquette droite
TOUCHE_RAQUETTE_D_B: int = pyxel.KEY_DOWN # Descendre raquette droite
TOUCHE_QUITTER: int = pyxel.KEY_Q # Quitter le jeu
TOUCHE_COMMENCER: int = pyxel.KEY_RETURN # Commencer la partie
TOUCHE_PAUSE: int = pyxel.KEY_P # Mettre en pause
TOUCHE_REPRENDRE: int = pyxel.KEY_R # Reprendre la partie

# COULs des textes
COUL_TXT: int = 7 # COUL du texte 1
COUL_TXT_SECOND: int = 5 # COUL du texte 2

# Score
SCORE_X_G: int = 26 # Position X du score gauche
SCORE_X_D: int = 134 # Position X du score droit
SCORE_Y: int = 30 # Position Y du score
SCORE_COUL: int = 7 # COUL du score
SCORE_I: int = 1 # Incrementation du score
SCORE_DEPART: int = 0 # Score de depart

# Menu
MENU_TITRE_X: int = 50 # Position X du titre
MENU_TITRE_Y: int = 40 # Position Y du titre
MENU_INSTRUCTIONS_X: int = 40 # Position X des instructions
MENU_TXT_Y_JOUER: int = 60 # Position Y du texte "Jouer"
MENU_TXT_Y_QUITTER: int = 70 # Position Y du texte "Quitter"

# Filet
FILET_L: int = 2 # Largeur du filet
FILET_COUL: int = 7 # COUL du filet
