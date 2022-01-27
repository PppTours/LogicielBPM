
import librosa
from librosa import core
from librosa.feature import tempogram
import numpy as np
import sys
import os
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment


def convert_mp3_to_wav(file_path):
    dst = "conversion.wav"
    aud_seg = AudioSegment.from_mp3(file_path)
    aud_seg.export(dst, format="wav")
    return dst


def is_not_wav(file_path):
    return file_path.split(".wav")[0] == file_path


def get_offset(file_path) :
    print()


def calcul_bpm(file_path):
    x, sr = librosa.load(file_path)
    print(x)
    bpm_initial = 120

    win_length = core.time_to_frames(8.0, sr=sr, hop_length=512).item()

    tg = tempogram(y=x, sr=sr, onset_envelope=None, hop_length=512, win_length=win_length)
    tg = np.mean(tg, axis=1, keepdims=True)

    bpms = core.tempo_frequencies(tg.shape[0], hop_length=512, sr=sr)

    logprior = -0.5 * (np.log2(bpms) - np.log2(120)) ** 2

    max_index = np.argmax(bpms < 320.0)
    logprior[:max_index] = - np.inf
    best_period = np.argmax(np.log1p(1000000 * tg) + logprior[:, np.newaxis], axis=0)

    return bpms[best_period][0]


if __name__ == "__main__":
    print("BPM calculé : ", calcul_bpm("12.wav"))

    """
    cwd = os.getcwd()
    len_arguments = len(sys.argv)
    if len_arguments > 1:
        file = sys.argv[1]
    else:
        root = tk.Tk()
        root.withdraw()
        entry = filedialog.askopenfile(initialdir=cwd)
        file = entry.name
        print(file)
        print(type(file))
"""



