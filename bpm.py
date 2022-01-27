
import librosa
from librosa import core
from librosa.feature import tempogram
import numpy as np
import sys
import os
import tkinter as tk


def calcul_bpm(file_path):
    x, sr = librosa.load(file_path)
    print(x)
    bpm_initial = 120

    win_length = core.time_to_frames(8.0, sr = sr, hop_length = 512).item()

    tg = tempogram(y=x, sr=sr, onset_envelope=None, hop_length = 512, win_length=win_length)
    tg = np.mean(tg, axis=1, keepdims = True)

    bpms = core.tempo_frequencies(tg.shape[0], hop_length=512, sr = sr)

    logprior = -0.5 * (np.log2(bpms) - np.log2(120)) ** 2

    max_index = np.argmax(bpms < 320.0)
    logprior[:max_index] = - np.inf
    best_period = np.argmax(np.log1p(1000000 * tg) + logprior[:, np.newaxis], axis = 0)

    return bpms[best_period][0]


if __name__ == "__main__":
    cwd = os.getcwd()
    len_arguments = len(sys.argv)
    if len_arguments > 1:
        file = sys.argv[1]
    else:
        root = tk.Tk()
        root.withdraw()
        entry = tk.filedialog.askopenfile(initialdir=cwd)
        file = entry.name

    print("BPM calculé : ", calcul_bpm("12.wav"))

