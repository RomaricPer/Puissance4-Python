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
    for colonne in range(len(plateau[0])):
        for ligne in range(len(plateau) - 3):
            if (plateau[ligne][colonne] != None and plateau[ligne + 1][colonne] != None and plateau[ligne + 2][colonne] != None and plateau[ligne + 3][colonne] != None):
                serie_pion = [plateau[ligne][colonne],plateau[ligne + 1][colonne],plateau[ligne + 2][colonne],plateau[ligne + 3][colonne]]
                if (getCouleurPion(serie_pion[0]) == couleur and getCouleurPion(serie_pion[1]) == couleur and getCouleurPion(serie_pion[2]) == couleur and getCouleurPion(serie_pion[3]) == couleur):
                    liste_serie.extend(serie_pion)
    return liste_serie


def detecter4diagonaleIndirectePlateau(plateau: list, couleur: int)-> list:
    """
    Fait une liste des pions qui sont alignés par 4 diagonalement (du bas vers le haut, de gauche à droite), la liste peut être vide si il n'y a pas de série.
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
        for colonnes in range(lignes-3):
            if plateau[lignes][colonnes]!=None and plateau[lignes-1][colonnes+1] != None and plateau[lignes-2][colonnes+2] != None and plateau[lignes-3][colonnes+3] != None:
                serie_pion = [plateau[lignes][colonnes],plateau[lignes-1][colonnes+1],plateau[lignes-2][colonnes+2],plateau[lignes-3][colonnes+3]]
                if getCouleurPion(serie_pion[0]) == couleur and getCouleurPion(serie_pion[1]) == couleur and getCouleurPion(serie_pion[2]) == couleur and getCouleurPion(serie_pion[3]) == couleur:
                    liste_serie.extend(serie_pion)
                else:
                    del serie_pion
    return liste_serie

def detecter4diagonaleDirectePlateau(plateau: list, couleur: int)->list:
    """
        Fait une liste des pions qui sont alignés par 4 diagonalement (du haut vers le bas, de gauche à droite), la liste peut être vide si il n'y a pas de série.
        Si 5 pions sont alignés : la fonction renverra les 4 premiers pions seulement (avec les plus petits indices)
        La liste retourner peut contenir plusieurs séries de 4 pions, et pas juste une seule.

        :param plateau: liste 2D représentant le plateau
        :param couleur: entier qui vaut 1 ou 0
        :return: retourne une liste contenant la ou les séries de 4 pions alignés, ou une liste vide si pas de série
        """
    if not type_plateau(plateau):
        raise TypeError("detecter4diagonaleDirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleDirectePlateau : Le second paramètre n'est pas un entier")
    if couleur != 1 and couleur != 0:
        raise ValueError(f"detecter4diagonaleDirectePlateau : La valeur de la couleur {couleur} n'est pas correcte")
    liste_serie = []
    for lignes in range(len(plateau)-3):
        for colonnes in range(len(plateau[lignes])-3):
            if plateau[lignes][colonnes] != None and plateau[lignes+1][colonnes+1] != None and plateau[lignes+2][colonnes+2] != None and plateau[lignes+3][colonnes+3] != None:
                serie_pion = [plateau[lignes][colonnes],plateau[lignes+1][colonnes+1],plateau[lignes+2][colonnes+2],plateau[lignes+3][colonnes+3]]
                if getCouleurPion(serie_pion[0]) == couleur and getCouleurPion(serie_pion[1]) == couleur and getCouleurPion(serie_pion[2]) == couleur and getCouleurPion(serie_pion[3]) == couleur:
                    liste_serie.extend(serie_pion)
                else:
                    del serie_pion
    return liste_serie

def getPionsGagnantsPlateau(plateau: list)->list:
    """
    Fait une liste de toutes les séries de 4 pions alignés en prenant en compte les deux couleur

    :param plateau: liste 2D représentant un plateau
    :return: retourne une liste des pions gagnants
    """
    if not type_plateau(plateau):
        raise TypeError("getPionsGagnantsPlateau : Le paramètre n'est pas un plateau")
    liste_pions_gagnants = []
    # on récupère les pions gagnants jaunes
    liste_pions_gagnants.extend(detecter4verticalPlateau(plateau, 0))
    liste_pions_gagnants.extend(detecter4horizontalPlateau(plateau, 0))
    liste_pions_gagnants.extend(detecter4diagonaleDirectePlateau(plateau, 0))
    liste_pions_gagnants.extend(detecter4diagonaleIndirectePlateau(plateau,0))
    # on récupère les pions gagnants rouges
    liste_pions_gagnants.extend(detecter4verticalPlateau(plateau, 1))
    liste_pions_gagnants.extend(detecter4horizontalPlateau(plateau, 1))
    liste_pions_gagnants.extend(detecter4diagonaleDirectePlateau(plateau, 1))
    liste_pions_gagnants.extend(detecter4diagonaleIndirectePlateau(plateau, 1))
    return liste_pions_gagnants

def isRempliPlateau(plateau: list)-> bool:
    """
    Renvoie True si le plateau est rempli, False si ce n'est pas le cas

    :param plateau: liste 2D représentant un plateau
    :return: un booléen
    """
    if not type_plateau(plateau):
        raise TypeError("isRempliPlateau : Le paramètre n'est pas un plateau")
    pions_premiere_ligne = []
    for col in range(len(plateau[0])):
        if plateau[0][col] != None:
            pions_premiere_ligne.append(plateau[0][col])
        else:
            pions_premiere_ligne = []
    return len(pions_premiere_ligne) == const.NB_COLUMNS

def placerPionLignePlateau(plateau: list, pion: dict,num_ligne : int, left: bool):
    """
    Cette fonction permet de placer des pions par la gauche ou la droite du plateau,
    elle place un pion à la ligne indiqué et par le côté indiqué

    :param plateau: liste 2D représentant un plateau
    :param pion: dictionnaire représentant un pion
    :param num_ligne: entier qui correspond à un numéro de ligne
    :param left: indique par où on insère le pion
    :return: retourne un tuple contenant la liste des pions poussés et un entier qui correspond
            à la ligne du dernier pion de la liste (None si pion change pas de ligne)
    """
    if not type_plateau(plateau):
        raise TypeError("placerPionLignePlateau : Le premier paramètre n'est pas un plateau")
    if not type_pion(pion):
        raise TypeError("placerPionLignePlateau : Le second paramètre n'est pas un pion")
    if type(num_ligne) != int:
        raise TypeError("placerPionLignePlateau : Le troisième paramètre n'est pas un entier")
    if num_ligne<0 or num_ligne>const.NB_LINES-1:
        raise ValueError(f"placerPionLignePlateau : Le troisième paramètre {num_ligne} ne désigne pas une ligne")
    if type(left) is not bool:
        raise TypeError("placerPionLignePlateau : Le quatrième paramètre n'est pas un booléen")

    liste_pion = [pion]
    ligne_dernier_pion = None

    if left:
        i = 0
        while i < const.NB_COLUMNS and plateau[num_ligne][i] is not None:
            liste_pion.append(plateau[num_ligne][i])
            i += 1

        for k in range(len(liste_pion) - 1):
            plateau[num_ligne][k] = liste_pion[k]
        del liste_pion[1]

        ligne_dernier_pion = num_ligne
        while ligne_dernier_pion + 1 < const.NB_LINES and plateau[ligne_dernier_pion + 1][len(liste_pion) - 1] is None:
            plateau[ligne_dernier_pion + 1][len(liste_pion) - 1] = plateau[ligne_dernier_pion][len(liste_pion) - 1]
            plateau[ligne_dernier_pion][len(liste_pion) - 1] = None
            ligne_dernier_pion += 1
    else:
        i = const.NB_COLUMNS - 1
        while i >= 0 and plateau[num_ligne][i] is not None:
            liste_pion.append(plateau[num_ligne][i])
            i -= 1

        for k in range(min(len(liste_pion), const.NB_COLUMNS)):
            plateau[num_ligne][const.NB_COLUMNS - 1 - k] = liste_pion[k]
        del liste_pion[-1]

        ligne_dernier_pion = num_ligne
        while ligne_dernier_pion + 1 < const.NB_LINES and plateau[ligne_dernier_pion + 1][const.NB_COLUMNS - 1 - len(liste_pion) + 1] is None:
            plateau[ligne_dernier_pion + 1][const.NB_COLUMNS - 1 - len(liste_pion) + 1] = plateau[ligne_dernier_pion][const.NB_COLUMNS - 1 - len(liste_pion) + 1]
            plateau[ligne_dernier_pion][const.NB_COLUMNS - 1 - len(liste_pion) + 1] = None
            ligne_dernier_pion += 1

    return liste_pion, ligne_dernier_pion
def encoderPlateau(plateau: list) -> str:
    """
    Cette fonction transforme le plateau en chaine de caractère, elle sert à stocker le plateau pour la fonction isPatPlateau

    :param plateau: liste 2D représentant un plateau
    :return: retourne une version str du plateau en paramètre
    """
    if not type_plateau(plateau) :
        raise TypeError("encoderPlateau : le paramètre ne correspond pas à un plateau.")

    encodage = ""

    for ligne in plateau:
        for case in ligne:
            if case is None:
                encodage += "_"
            elif case['Couleur'] == 0:
                encodage += "J"
            elif case['Couleur'] == 1:
                encodage += "R"

    return encodage
def isPatPlateau(plateau: list, histogramme_plateaux: dict) -> bool:
    """
    Définit si une partie est nulle ou non selon le nombre de fois que le plateau a été identique dans une partie

    :param plateau:
    :param histogramme_plateaux:
    :return: retourne True ou False selon si le plateau à déjà été similaire 5 fois ou non
    """

    if not(type_plateau(plateau)):
        raise TypeError("isPatPlateau : le paramètre ne correspond pas à un plateau.")
    if type(histogramme_plateaux) != dict:
        raise TypeError("isPatPlateau : Le second paramètre n’est pas un dictionnaire ")

    clef = encoderPlateau(plateau)

    if clef in histogramme_plateaux:
        histogramme_plateaux[clef] += 1
        return histogramme_plateaux[clef] >= 5
    else:
        histogramme_plateaux[clef] = 1
        return False