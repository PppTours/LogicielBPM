import numpy as np

def decalage(fs, bpm):
    """
    Calcule le decalage d'une courbe
    """
    return 240 * fs / bpm


def autocorrelation(liste, k):
    """
    Calcule l'autocorrelation d'une serie en fonction de son decalage k
    """
    return autocovariance(liste, k) / np.var(liste)


def autocovariance(liste, k):
    """
    Calcule l'autocovariance d'une serie en fonction de son decalage k
    """
    resultat = 0
    moyenne = np.mean(liste)
    for i in range(0, k):
        resultat += (liste[i] - moyenne) * (liste[i + k] - moyenne)
    return resultat / k