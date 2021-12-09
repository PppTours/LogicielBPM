# LogicielBPM
Ceci est un projet de P++, une association de Polytech'Tours. Les chefs de projet sont Bastien Camembert et Thomas Ciron. Le but de ce projet est d'établir un code qui permet de détecter le BPM d'une musique.
Nous programmons en Python, plus précisément sous l'environnement Pycharm.

## Phase de recherche
Une grosse partie des premières séances est marquée par une phase de recherche. En effet, ce projet demande des compétences que nous n'avions pas. Nous ne savions pas manipuler les fichiers audio et ne connaissions pas les principes qui se cachaient derrière la notion de battements par minutes.

Nous avons trouvé plein de documentations intéressantes sur internet, notamment un compte-rendu d'élèves ayant travaillé sur le sujet et qui expliquaient très bien les équations et les techniques qui se cachaient derrière le principe de BPM. Plusieurs techniques s'offrent à nous, la plus intéressante semble être la méthode d'auto-corrélation qui fait appel à des notions de statistiques. Cette technique a l'avantage d'avoir un excellant rapport précision / temps de calcul.

## Librairie aubio
Nous mettons nos espoirs sur cette librairie, qui nous permet de manipuler tous les types de fichiers audio. En effet, nous avons trouvé des codes tout fait sur internet en Python, mais qui ne traitaient que le cas des fichiers .wav. Nous nous sommes imposés de ne pas se limiter à cela et de trouver un moyen de calculer le BPM pour tout de type de fichier audio (.wav mais aussi .mp3, .wma, .aac, ...).