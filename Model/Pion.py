# Model/Pion.py

from Model.Constantes import *

#
# Ce fichier implémente les données/fonctions concernant le pion
# dans le jeu du Puissance 4
#
# Un pion est caractérisé par :
# - sa couleur (const.ROUGE ou const.JAUNE)
# - un identifiant de type int (pour l'interface graphique)
#
# L'identifiant sera initialisé par défaut à None
#

def type_pion(pion: dict) -> bool:
    """
    Détermine si le paramètre peut être ou non un Pion

    :param pion: Paramètre dont on veut savoir si c'est un Pion ou non
    :return: True si le paramètre correspond à un Pion, False sinon.
    """
    return type(pion) == dict and len(pion) == 2 and const.COULEUR in pion.keys() \
        and const.ID in pion.keys() \
        and pion[const.COULEUR] in const.COULEURS \
        and (pion[const.ID] is None or type(pion[const.ID]) == int)

def construirePion(couleur: int)-> dict:
    """
    Construit un pion selon la couleur reçu en paramètre

    :param couleur: entier qui vaut 1 ou 0
    :return: retourne un pion
    """
    if couleur == 1:
        pion = {const.COULEUR: const.COULEURS[1], const.ID: None}
    elif couleur == 0:
        pion = {const.COULEUR: const.COULEURS[0], const.ID: None}
    if type(couleur) != int:
        raise TypeError("construirePion : Le paramètre n'est pas de type entier")
    if couleur != 1 and couleur != 0:
        raise ValueError(f"construirePion : la couleur {couleur} n'est pas correct")
    return pion

def getCouleurPion(pion: dict)->int:
    """
    Cette fonction retourne la couleur d'un pion, '1' pour rouge, '0' pour jaune

    :param pion: dictionnaire représetant un pion
    :return: retourne une couleur
    """
    if not type_pion((pion)):
        raise TypeError("getCouleurPion : Le paramètre n'est pas un pion")
    else:
        couleur = pion[const.COULEUR]
    return couleur

def setCouleurPion(pion: dict, couleur: int)->None:
    """
    Modifie la couleur d'un pion par la couleur donner

    :param pion: dictionnaire représentant un pion
    :param couleur: '1' pour rouge, '0' pour jaune
    :return: Rien
    """
    if not type_pion(pion):
        raise TypeError("setCouleurPion : Le premier paramètre n'est pas un pion")
    if type(couleur) != int:
        raise TypeError("setCouleurPion : Le second paramètre n'est pas un entier")
    pion[const.COULEUR] = couleur
    if couleur != 1 and couleur != 0:
        raise ValueError(f"setCouleurPion : le second paramètre {couleur} n'est pas une couleur")
    return None

def getIdPion(pion: dict)->int:
    """
    Cette fonction retourne l'identifiant du pion en paramètre

    :param pion: dictionnaire représentant un pion
    :return: retourne l'Id du pion
    """
    id = pion[const.ID]
    if not type_pion(pion):
        raise TypeError("getIdPion : Le paramètre n'est pas un pion")
    return id

def setIdPion(pion: dict, id: int)->None:
    """
    Modifie l'identifiant d'un pion par la valeur 'id'

    :param pion: dictionnaire représentant un pion
    :param id: valeur représentant un identifiant de pion
    :return: retourne un pion
    """
    pion[const.ID] = id
    if not type_pion(pion):
        raise TypeError("setIdPion : Le premier paramètre n'est pas un pion")
    if type(id) != int:
        raise TypeError("setIdPion : Le second paramètre n'est pas un entier")
    return None