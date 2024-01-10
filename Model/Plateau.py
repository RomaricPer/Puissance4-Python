from Model.Constantes import *
from Model.Pion import *
import numpy as np
from random import randint, choice


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

def detecter4horizontalPlateau(plateau: list, couleur: int)-> list:
    """
    Fait une liste des pions qui sont alignés par 4, la liste peut être vide si il n'y a pas de série.
    Si 5 pions sont alignés : la fonction renverra les 4 premiers pions seulement (avec les plus petits indices)
    La liste retourner peut contenir plusieurs séries de 4 pions, et pas juste une seule.

    :param plateau: liste 2D représentant le plateau
    :param couleur: entier qui vaut 1 ou 0
    :return: retourne une liste contenant la ou les séries de 4 pions alignés, ou une liste vide si pas de série
    """

    if not type_plateau(plateau):
        raise TypeError("detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4horizontalPlateau : Le second paramètre n'est pas un entier")
    if couleur != 1 and couleur != 0:
        raise ValueError(f"detecter4horizontalPlateau : La valeur de la couleur {couleur} n'est pas correcte")

    liste_serie = []
    for lignes in plateau:
        for i in range(len(lignes)-3):
            if lignes[i] != None and lignes[i+1] != None and lignes[i+2] != None and lignes[i+3] != None:
                serie_pion = [lignes[i],lignes[i+1],lignes[i+2],lignes[i+3]]
                if getCouleurPion(serie_pion[0]) == couleur and  getCouleurPion(serie_pion[1]) == couleur and  getCouleurPion(serie_pion[2]) == couleur and  getCouleurPion(serie_pion[3]) == couleur:
                    liste_serie.extend(serie_pion)
                else:
                    del serie_pion
    return liste_serie

def detecter4verticalPlateau(plateau: list, couleur: int)-> list:
    """
    Fait une liste des pions qui sont alignés par 4 verticalement, la liste peut être vide si il n'y a pas de série.
    Si 5 pions sont alignés : la fonction renverra les 4 premiers pions seulement (avec les plus petits indices)
    La liste retourner peut contenir plusieurs séries de 4 pions, et pas juste une seule.

    :param plateau: liste 2D représentant le plateau
    :param couleur: entier qui vaut 1 ou 0
    :return: retourne une liste contenant la ou les séries de 4 pions alignés, ou une liste vide si pas de série
    """
    if not type_plateau(plateau):
        raise TypeError("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4verticalPlateau : Le second paramètre n'est pas un entier")
    if couleur != 1 and couleur != 0:
        raise ValueError(f"detecter4verticalPlateau : La valeur de la couleur {couleur} n'est pas correcte")

    liste_serie = []
    for colonnes in range(len(plateau)):
        for i in range(5):
            if plateau[i][colonnes] != None and plateau[i+1][colonnes] != None and  plateau[i+2][colonnes] != None and  plateau[i+3][colonnes] != None:
                serie_pion = [plateau[i][colonnes], plateau[i+1][colonnes], plateau[i+2][colonnes], plateau[i+3][colonnes]]
                if getCouleurPion(serie_pion[0]) == couleur and getCouleurPion(serie_pion[1]) == couleur and getCouleurPion(serie_pion[2]) == couleur and getCouleurPion(serie_pion[3]) == couleur:
                    liste_serie.extend(serie_pion)
                else:
                    del serie_pion
    return liste_serie

def detecter4diagonaleIndirectePlateau(plateau: list, couleur: int)-> list:
    """
    Fait une liste des pions qui sont alignés par 4 diagonalement (du bas vers le haut), la liste peut être vide si il n'y a pas de série.
    Si 5 pions sont alignés : la fonction renverra les 4 premiers pions seulement (avec les plus petits indices)
    La liste retourner peut contenir plusieurs séries de 4 pions, et pas juste une seule.

    :param plateau: liste 2D représentant le plateau
    :param couleur: entier qui vaut 1 ou 0
    :return: retourne une liste contenant la ou les séries de 4 pions alignés, ou une liste vide si pas de série
    """
    if not type_plateau(plateau):
        raise TypeError("detecter4diagonaleIndirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleIndirectePlateau : Le second paramètre n'est pas un entier")
    if couleur != 1 and couleur != 0:
        raise ValueError(f"detecter4diagonaleIndirectePlateau : La valeur de la couleur {couleur} n'est pas correcte")
    liste_serie = []
    for lignes in range(3,len(plateau)):
        for colonnes in range(lignes):
            if plateau[lignes][colonnes]!=None and plateau[lignes-1][colonnes+1] != None and plateau[lignes-2][colonnes+2] != None and plateau[lignes-3][colonnes+3] != None:
                serie_pion = [plateau[lignes][colonnes],plateau[lignes-1][colonnes+1],plateau[lignes-2][colonnes+2],plateau[lignes-3][colonnes+3]]
                if getCouleurPion(serie_pion[0]) == couleur and getCouleurPion(serie_pion[1]) == couleur and getCouleurPion(serie_pion[2]) == couleur and getCouleurPion(serie_pion[3]) == couleur:
                    liste_serie.extend(serie_pion)
                else:
                    del serie_pion
    return liste_serie