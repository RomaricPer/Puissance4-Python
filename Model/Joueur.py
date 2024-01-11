from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *



#
# Ce fichier contient les fonctions gérant le joueur
#
# Un joueur sera un dictionnaire avec comme clé :
# - const.COULEUR : la couleur du joueur entre const.ROUGE et const.JAUNE
# - const.PLACER_PION : la fonction lui permettant de placer un pion, None par défaut,
#                       signifiant que le placement passe par l'interface graphique.
# - const.PLATEAU : référence sur le plateau de jeu, nécessaire pour l'IA, None par défaut
# - d'autres constantes nécessaires pour lui permettre de jouer à ajouter par la suite...
#

def type_joueur(joueur: dict) -> bool:
    """
    Détermine si le paramètre peut correspondre à un joueur.

    :param joueur: Paramètre à tester
    :return: True s'il peut correspondre à un joueur, False sinon.
    """
    if type(joueur) != dict:
        return False
    if const.COULEUR not in joueur or joueur[const.COULEUR] not in const.COULEURS:
        return False
    if const.PLACER_PION not in joueur or (joueur[const.PLACER_PION] is not None
            and not callable(joueur[const.PLACER_PION])):
        return False
    if const.PLATEAU not in joueur or (joueur[const.PLATEAU] is not None and
        not type_plateau(joueur[const.PLATEAU])):
        return False
    return True

def construireJoueur(couleur: int)-> dict:
    """
    Construit une dictionnaire représentant un joueur par une couleur qui lui est attribué,
    un plateau qui lui est associé et une fonction qui lui permet de jouer

    :param couleur: entier entre 1 ou 0
    :return: retourne le dictionnaire représetant un joueur
    """
    if type(couleur) != int:
        raise TypeError("construireJoueur: Le paramètre n'est pas un entier")
    if couleur != 1 and couleur != 0:
        raise ValueError(f"construireJoueur: L'entier donné {couleur} n'est pas une couleur")

    if couleur == const.JAUNE:
        joueur = {const.COULEUR: const.JAUNE, const.PLATEAU : None, const.PLACER_PION : None}
    if couleur == const.ROUGE:
        joueur = {const.COULEUR: const.ROUGE, const.PLATEAU: None, const.PLACER_PION: None}
    return joueur


