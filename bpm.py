#coding: utf-8

import matplotlib.pyplot as plt
import aubio
import stats


def print_audio_track(audio_file):
    """
    Affiche la piste audio de la piste. Il y a deux types de paramètres possibles : soit un lien vers le fichier audio soit un objet aubio.
    """
    # Si le paramètre est un lien vers le fichier audio :
    if type(audio_file) == str:
        src = aubio_object(audio_file)
    else:
        src = audio_file
    samples, read = src()
    plt.plot(samples)
    plt.title("Piste audio du fichier")
    plt.xlabel("Temps (ms)")
    plt.ylabel("Fréquence (Hz) ?")
    plt.show()

def aubio_object(filepath, music_length = 4 * 60 * 1000):
    """ 
    Crée un fichier aubio à partir d'un lien vers un fichier audio et le temps à prendre en considération (en ms).
    TODO : améliorer cette fonction pour prendre exactement la longueur de la musique !
    """
    return aubio.source(filepath, 0, music_length)

def init_plage_bpm(bpm_debut, bpm_fin, pas):
    """
    Crée une plage allant de bpm_debut à bpm_fin en allant de pas en pas.
    """
    plage_bpm = [bpm_debut]
    while(plage_bpm[-1] < bpm_fin):
        plage_bpm.append(plage_bpm[-1]+pas)
    return plage_bpm
        

def calcul_bpm(son, fs, pas_fin = 0.05, bpm_debut = 85, bpm_fin = 160, pas_grossier = 1):
    """
    Calcule le BPM.
    """
    pas = pas_grossier
    trouve_grossier = False
    trouve_bpm = False
    while not(trouve_bpm):
        # Plage de BPM à parcourir :
        plage_bpm = init_plage_bpm(bpm_debut, bpm_fin, pas)
        print("Plage de BPM : ",plage_bpm)
        exit()

# TODO : demander à l'utilisateur de choisir un fichier ou prendre en compte le paramètre pris en compte
if __name__=="__main__":
    audio_file = "Never Gonna Give You Up.mp3"
    calcul_bpm(aubio_object(audio_file), 1)
"""
TODO : calculer le BPM
Ça marche pas du tout ptdr
max = 0
k = 0
barre = -10
print("Calcul en cours...")
for i in range(1, len(samples)//2, 240):
    autocorrelation_tmp = stats.autocorrelation(samples, i)
    if autocorrelation_tmp > max :
        max = autocorrelation_tmp
        k = i

print()
print(k)
print(max)
"""