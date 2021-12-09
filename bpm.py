#coding: utf-8

import matplotlib.pyplot as plt
import aubio
import stats
import time
import librosa


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
        
def calcul_bpm(audio_file):
    """
    Calcule le BPM.
    """
    src = aubio_object(audio_file)
    x2, sr2 = src()
    return librosa.beat.tempo(x2, sr=sr2)[0]*0.8

def calcul_bpm2(src, fs, pas_fin = 0.05, bpm_debut = 85, bpm_fin = 160, pas_grossier = 1):
    """
    Calcule le BPM.
    """
    pas = pas_grossier
    trouve_grossier = False
    trouve_bpm = False
    son, read = src()
    while not(trouve_bpm):
        # Plage de BPM à parcourir :
        plage_bpm = init_plage_bpm(bpm_debut, bpm_fin, pas)
        decalage = [4./i*60*fs for i in plage_bpm]
        correl = [0 for i in range(len(decalage))]
        start_time = time.time()
        print("Parcours de la plage " + str(bpm_debut) + " : " + str(bpm_fin) + " en allant de "+str(pas) + " en "+str(pas) + " : ")
        print("Calcul de " + str(len(decalage)) + " autocorrélations en cours sur des vecteurs de taille " + str(len(son) - decalage[-1]))

        for i in range(0, len(decalage)):
            decal = int(decalage[i])
            extrait2 = son[min(1 + decal, son[-1])]
            print(decal, decalage[i])
        exit()
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

def compare_bpm(audio1, audio2):
    """
    Compare des BPM.
    """
    print("Calcul du BPM en cours . . .")
    x, sr = librosa.load(audio1)
    tempo = librosa.beat.tempo(x, sr=sr)
    time_start = time.time()
    bpm = calcul_bpm(audio2)
    duree = time.time() - time_start
    print("Vrai BPM : ", tempo[0])
    print("BPM de l'arnaque : ", bpm)
    print("Temps de calcul : " + str(duree) + "s")


# TODO : demander à l'utilisateur de choisir un fichier ou prendre en compte le paramètre pris en compte
if __name__=="__main__":
    audio_file2 = "Never Gonna Give You Up.mp3"
    audio_file = "12.wav"
    compare_bpm(audio_file, audio_file2)
