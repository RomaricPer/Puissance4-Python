from Model.Constantes import *
from Model.Pion import *
import numpy as np


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not(c is None) and not type_pion(c)), True) == wrong:
        return False
    return True

def construirePlateau()->list:
    """
    Cette fonction crée un tableau 2D vide avec const.NB_LINES et const.NB_COLUMNS

    :return: retourne le tableau 2D crée
    """
    plateau = []
    for i in range(const.NB_LINES):
        plateau2=[]
        for j in range(const.NB_COLUMNS):
            plateau2.append(None)
        plateau.append(plateau2)
    return plateau
def placerPionPlateau(plateau: list, pion: dict, num_col: int)->int:
    """
    Place un pion dans la colonne préciser, le pion tombe jusqu'à ce qu'il rencontre une
    autre pion ou si il rencontre la dernière ligne, la fonction renvoie la ligne à laquelle le pion est placer

    :param plateau: tableau 2D contenant const.NB_LINES et const.NB_COLUMNS
    :param pion: dictionnaire représentant un pion
    :param num_col: entier compris entre 0 et const.NB_COLUMNS-1
    :return: retourne le numéro de la ligne où est placer le pion
    """
    if not type_plateau(plateau):
        raise TypeError("placerPionPlateau : Le premier paramètre ne correspond pas à un plateau")
    if not type_pion(pion):
        raise TypeError("placerPionPlateau : Le second paramètre n'est pas un pion")
    if type(num_col) != int:
        raise TypeError("placePionPlateau : Le troisième paramètre n'est pas un entier")
    if num_col < 0 or num_col >= const.NB_COLUMNS:
        raise ValueError(f"placerPionPlateau : La valeur de la colonne {num_col} n'est pas correcte")

    num_ligne = -1
    if plateau[0][num_col] != None:
        return num_ligne
    else:
        num_ligne = 0
    pionPlacer = False
    while num_ligne <= 5 and not pionPlacer:
        if plateau[num_ligne][num_col] != None:
            plateau[num_ligne-1][num_col] = pion
            ligne = num_ligne - 1
            pionPlacer = True
        else:
            num_ligne += 1
    if pionPlacer == False and plateau[5][num_col] == None:
        plateau[5][num_col] = pion
        ligne = 5
        pionPlacer = True
    return ligne