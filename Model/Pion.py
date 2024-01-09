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
    #raise ValueError(f"construirePion : la couleur {couleur} n'est pas correct")
    #raise TypeError("construirePion : Le paramètre n'est pas de type entier")
    return pion







