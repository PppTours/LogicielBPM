# LogicielBPM
Ceci est un projet de P++, une association de Polytech'Tours. Les chefs de projet sont Bastien Camembert et Thomas Ciron. Le but de ce projet est d'établir un code qui permet de détecter le BPM d'une musique.
Ce projet a été réalisé en Python.

## Guide d'installation
Pour installer notre outil, il vous suffit de récupérer notre fichier bpm.py sur le Git (soit en clonant, soit en téléchargeant, soit en copiant collant le code). Nous avons un fichier .py, il vous faut donc un interpréteur Python pour exécuter notre code. Vous pouvez en télécharger un via ce lien : https://www.python.org/downloads/.

Certaines librairies seront peut-être à installer, voici celles qu'il nous faut : 
- librosa
- numpy

Nous utilisons aussi les librairies sys, os, tkinter et pydub, mais elles sont déjà installées avec Python3 il me semble. Pour voir s'il vous manque une librairie, essayez de compiler bpm.py et le compilateur vous affichera un joli message s'il ne trouve pas une librairie. Voici les commandes pour installer librosa et numpy : 

``pip install librosa``

``pip install numpy``

## Guide d'utilisation

Il est possible de lancer bpm.py avec ou sans argument. S'il y a un argument, alors vous verrez l'offset et le bpm du fichier audio (.mp3 ou .wav) du premier argument. Si vous n'avez pas spécifié d'argument, alors vous devrez choisir un fichier audio, puis vous verrez l'offset et le BPM qui s'affichent.

## Documentation

### convert_mp3_to_wav
Paramètre : file_path : chemin d'un fichier .mp3

Retourne : la version .wav de file_path

### is_not_wav
Paramètre : file_path : chemin d'un fichier

Retourne : 
- vrai si le fichier spécifié est un .wav
- faux sinon

### get_offset
Paramètre : file_path : chemin d'un fichier .wav

Retourne : l'offset en millisecondes

### calcul_bpm
Paramètre : file_path : chemin d'un fichier .wav

Retourne : le BPM du fichier



