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

def getCouleurJoueur(joueur: dict) -> int:
    """
    Renvoie la couleur du joueur en paramètre

    :param joueur: Dictionnaire représentant un joueur
    :return: retourne 1 ou 0
    """
    if not type_joueur(joueur):
        raise TypeError("getCouleurJoueur: Le paramètre ne correspond pas à joueur")
    return joueur[const.COULEUR]

def getPlateauJoueur(joueur: dict) -> list:
    """
    Renvoie le plateu lié au joueur

    :param joueur: Dictionnaire représentant un joueur
    :return: retourne le plateau lié au joueur en forme de liste 2D
    """
    if not type_joueur(joueur):
        raise TypeError("getPlateauJoueur: Le paramètre ne correspond pas à un joueur")
    return joueur[const.PLATEAU]

def getPlacerPionJoueur(joueur: dict)-> None:
    """
    Renvoie la fonction qui permet de savoir si le joueur peut jouer ou non

    :param joueur: dictionnaire représenant un joueur
    :return:
    """
    if not type_joueur(joueur):
        raise TypeError("getPlacerPionJoueur: Le paramètre ne correspond pas à joueur")
    return joueur[const.PLACER_PION]

def getPionJoueur(joueur: dict)-> dict:
    """
    Crée un pion ayant la meme couleur que le joueur

    :param joueur: dictionnaire représentant un joueur
    :return: retourne un pion
    """
    if not type_joueur(joueur):
        raise TypeError("getPionJoueur: Le paramètre ne correspond pas à joueur")
    pion = construirePion(joueur[const.COULEUR])
    return pion

def setPlateauJoueur(joueur: dict, plateau: list)-> None:
    """
    Affecte un plateau en paramètre à un joueur mis en paramètre

    :param joueur: dictionnaire représentant un dictionnaire
    :param plateau: liste 2D représentant un plateau
    :return: Rien
    """
    if not type_joueur(joueur):
        raise TypeError("setPlateauJoueur : Le premier paramètre ne correspond pas à joueur")
    if not type_plateau(plateau):
        raise TypeError("setPlateauJoueur : Le second paramètre ne correpond pas à un plateau")
    joueur[const.PLATEAU] = plateau
    return None

def setPlacerPionJoueur(joueur: dict, fn)->None:
    """
    Affecte une fonction mis en paramètre au joueur

    :param joueur: dictionnaire représentant un joueur
    :param fn: fonction appelable
    :return: Rien
    """
    if not type_joueur(joueur):
        raise TypeError("setPlacerPionJoueur : Le premier paramètre ne correspond pas à joueur")
    if not callable(fn):
        raise TypeError("setPlacerPionJoueur : Le second paramètre n'est pas une fonction")
    joueur[const.PLACER_PION] = fn
    return None

def _placerPionJoueur(joueur: dict)->int:
    """
    Place un pion aléatoirement dans une colonne entre 0 et const.NB_COLUMNS -1

    :param joueur: dictionnaire représentant un joueur
    :return: un entier représentant une colonne
    """
    num_col = randint(0,const.NB_COLUMNS-1)
    plateau = joueur[const.PLATEAU]
    while plateau[0][num_col] != None:
        num_col = randint(0, const.NB_COLUMNS - 1)
    return num_col

def initialiserIAJoueur(joueur: dict, booleen: bool)->None:
    """
    Initialise si un joueur joue en premier ou en second selon la valeur du booléen:
    True lorsqu'il commence, False lorsqu'il est second

    :param joueur: dictionnaire représentant un joueur
    :param booleen: True si le joueur commence, False sinon
    :return: Rien
    """
    if not type_joueur(joueur):
        raise TypeError("initialiserIAJoueur : Le premier paramètre ne correspond pas à joueur")
    if type(booleen) != bool:
        raise TypeError("initialiserIAJoueur : Le second paramètre n'est pas un booléen")
    if booleen:
        setPlacerPionJoueur(joueur,_placerPionJoueur)
    if not booleen:
        setPlacerPionJoueur(joueur,_placerPionJoueur)
    return None