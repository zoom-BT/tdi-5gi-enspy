# tdi-5gi-enspy — Traitement d'images (5GI, ENSPY)

Ce dépôt réimplémente **en Python + numpy** les algorithmes des 7 chapitres du cours de traitement d'images. Il contient un module par personne, des tests pytest et une CI GitHub Actions.

> Nom suggéré pour le dépôt GitHub : `tdi-5gi-enspy`. Autres choix possibles : `traitement-images-5gi`, `pixelab-5gi`.
> Le paquet Python s'appelle `timg`.

## 1. Installation

```bash
git clone <url>/tdi-5gi-enspy.git && cd tdi-5gi-enspy
python -m venv .venv && source .venv/bin/activate   # Windows : .venv\Scripts\activate
pip install -e ".[dev]"
pytest -q            # les fonctions non encore codées sont "skipped"
```

## 2. Arborescence

```
tdi-5gi-enspy/
├── README.md
├── pyproject.toml            # paquet "timg", config pytest et ruff
├── requirements.txt          # numpy, pillow
├── requirements-dev.txt      # + pytest, ruff, matplotlib, scipy/skimage/opencv (références de TEST uniquement)
├── .github/
│   ├── workflows/ci.yml      # ruff + pytest + interdiction de cv2/skimage/scipy dans src/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── CODEOWNERS            # relecteur automatique par fichier
├── data/                     # images de test partagées (data/out/ ignoré)
├── docs/repartition.md       # qui fait quoi (détail)
├── notebooks/  scripts/      # démos avant/après par chapitre
├── src/timg/
│   ├── core/                 io.py (PGM/PPM, M01) · utils.py (fourni : as_float, to_uint8, normaliser_0_255)
│   ├── ch01_intro/           numerisation.py · profil.py
│   ├── ch02_base/            histogramme.py · stats.py · ponctuel.py · arithmetique.py · interpolation.py
│   ├── ch03_convolution/     convolution.py · lissage.py · passe_haut.py · ordre.py · bruit.py
│   ├── ch04_fourier/         fft.py · spectre.py · filtres_frequentiels.py
│   ├── ch05_contours/        gradient.py · laplacien.py · hough.py · canny.py
│   ├── ch06_segmentation/    seuillage.py · kmeans.py · split_merge.py · croissance.py
│   └── ch07_binaires/        connexite.py · etiquetage.py · freeman.py · morphologie.py · hysteresis.py · fermeture_contours.py
└── tests/                    même arborescence : tests/chXX_.../test_<module>.py + conftest.py (fixtures damier, rampe, carre_binaire)
```

Chaque fichier de `src/` contient déjà :
- les **signatures** ;
- une **docstring** avec la formule du cours ;
- un `raise NotImplementedError("Mxx: ...")`.

Tu n'as plus qu'à remplir.

## 3. Répartition (12 membres)

Remplacer `Mxx` par le prénom. La colonne charge est une estimation : 1 point vaut environ 1 h. Le détail est dans `docs/repartition.md`.

| Membre | Chapitre(s) | Fichiers | Charge |
|---|---|---|---|
| M01 | Ch1 + interpolation (Ch2) | `core/io.py`, `ch01_intro/*`, `ch02_base/interpolation.py` | ~8 |
| M02 | Ch2 histogrammes | `ch02_base/histogramme.py`, `stats.py` | ~8 |
| M03 | Ch2 point à point + arithmétique | `ch02_base/ponctuel.py`, `arithmetique.py` | ~7 |
| M04 | Ch7 connexité, étiquetage, Freeman | `ch07_binaires/connexite.py`, `etiquetage.py`, `freeman.py` | ~8.5 |
| M05 | Ch3 convolution linéaire | `ch03_convolution/convolution.py`, `lissage.py`, `passe_haut.py` | ~7.5 |
| M06 | Ch3 non linéaire + Ch7 morphologie | `ch03_convolution/ordre.py`, `bruit.py`, `ch07_binaires/morphologie.py` | ~8 |
| M07 | Ch4 FFT | `ch04_fourier/fft.py`, `spectre.py` | ~8 |
| M08 | Ch4 filtrage fréquentiel | `ch04_fourier/filtres_frequentiels.py` | ~7.5 |
| M09 | Ch5 gradient/Laplacien + fermeture de contours | `ch05_contours/gradient.py`, `laplacien.py`, `ch07_binaires/fermeture_contours.py` | ~8 |
| M10 | Ch5 Hough + Canny + hystérésis | `ch05_contours/hough.py`, `canny.py`, `ch07_binaires/hysteresis.py` | ~8.5 |
| M11 | Ch6 seuillage + k-means | `ch06_segmentation/seuillage.py`, `kmeans.py` | ~8 |
| M12 | Ch6 régions | `ch06_segmentation/split_merge.py`, `croissance.py` | ~8 |

**Dépendances à livrer en premier (semaine 1) :**
- M01 : `core/io.py` (tout le monde charge des images avec).
- M05 : `convolution2d` + `pad` (utilisés par M06, M09, M10).
- M07 : `fft2d`/`ifft2d` (utilisés par M08).

En attendant, chacun peut tester avec `numpy`, ou avec `scipy.ndimage.convolve` / `np.fft` **dans ses tests seulement**.

## 4. Conventions de code

- **numpy uniquement dans `src/`**. OpenCV, scikit-image et scipy ne sont autorisés que dans `tests/`, comme référence de comparaison. Dans `ch04_fourier/fft.py`, `np.fft` est interdit : la FFT est codée à la main. La CI le vérifie.
- **Images** : `np.ndarray`, avec les formes suivantes.
  - Niveaux de gris : `(H, W)` en `uint8` [0..255].
  - Couleur : `(H, W, 3)` RVB.
  - Binaire : `(H, W)` en `uint8` {0,1}.
- **Calculs** : faire les calculs en `float64` avec `as_float`. Renvoyer en `uint8` avec `to_uint8`, qui arrondit et sature, sauf pour les sorties « signées » : gradients, laplacien, spectre complexe.
- **Indexation** : `img[y, x]`, soit ligne puis colonne. L'origine est en haut à gauche.
- **Ne jamais modifier l'image d'entrée** : travailler sur une copie.
- **Nommage** : snake_case en français, sans accents, comme dans les stubs. Les signatures existantes ne changent pas sans accord (issue + PR).
- **Docstrings** : formule, paramètres, retour et référence au cours (ex. `Cours 03-Convolution, p.12`).
- **Vectoriser quand c'est raisonnable**. Une boucle Python reste acceptable pour les algorithmes séquentiels : étiquetage, croissance de régions, suivi de contours.
- **Style** : `ruff check src tests` doit passer, avec des lignes de 100 caractères maximum.

## 5. Tests

- Un fichier de test par module : `tests/chXX_.../test_<module>.py`.
- Le décorateur `@implemente(m.fonction)` saute le test tant que la fonction est un stub. Il passe automatiquement dès qu'elle est codée.
- **Minimum par fonction** :
  - un cas calculé à la main sur une petite matrice (3×3 à 8×8) ;
  - un cas limite : image constante, bords, image vide ;
  - si possible, une comparaison à une référence. Exemples : `np.bincount`, `np.fft.fft2`, `scipy.ndimage.median_filter`, `skimage.filters.threshold_otsu`, `skimage.measure.label`, `skimage.morphology.binary_erosion`.
- Lancer avant chaque push : `pytest -q` ; pour un module : `pytest tests/ch03_convolution -q`.

## 6. Branches

| Branche | Rôle |
|---|---|
| `main` | version rendue / démontrée. Protégée : merge uniquement depuis `develop` par le chef de projet. |
| `develop` | intégration. Protégée : PR obligatoire, 1 approbation et CI verte. |
| `mXX/<chapitre>-<sujet>` | branche de travail d'un membre, partie de `develop` |

Exemples de branches de travail :
- `m05/ch03-convolution`
- `m07/ch04-fft`
- `m11/ch06-otsu`
- `m04/ch07-etiquetage`

Avec les prénoms, on peut aussi écrire `<prenom>/<chapitre>-<sujet>`, par exemple `paul/ch05-hough`. Correctifs : `mXX/fix-<sujet>`. Docs : `mXX/docs-<sujet>`.

**Commits** (Conventional Commits) :
- `feat(ch03): convolution2d avec bords miroir`
- `test(ch06): otsu sur image bimodale`
- `fix(ch02): saturation dans addition`
- `docs: ...`

## 7. Workflow Pull Request

1. Créer la branche à jour :
   ```bash
   git switch develop && git pull
   git switch -c m05/ch03-convolution
   ```
2. Coder la fonction et ses tests, puis vérifier en local :
   ```bash
   pytest -q && ruff check src tests
   ```
3. Committer petit et souvent :
   ```bash
   git push -u origin m05/ch03-convolution
   ```
4. Ouvrir une **PR vers `develop`**. Le modèle de PR s'affiche ; une PR = un module ou un groupe de fonctions cohérent.
5. **Relecture** par 1 membre, assigné automatiquement via CODEOWNERS ou choisi dans un chapitre voisin. Le relecteur vérifie la formule du cours, les tests et l'absence de bibliothèques interdites.
6. CI verte et 1 approbation : **Squash & merge**, puis suppression de la branche.
7. Avant de merger, si `develop` a avancé :
   ```bash
   git fetch && git rebase origin/develop
   ```
   On ne force-push que sur sa propre branche.
8. En fin de chapitre, le chef de projet ouvre une PR `develop → main` et tague la version (`v0.3-ch03`, …).

Pour les bugs, questions ou demandes de changement de signature : ouvrir une **issue** avec le label `chXX`.

## 8. Calendrier indicatif

| Semaine | Objectif |
|---|---|
| S1 | io, convolution et FFT de base mergés. Les autres membres écrivent leurs tests. |
| S2 | Ch2, Ch3 et Ch4 complets. |
| S3 | Ch5, Ch6 et Ch7 complets. |
| S4 | Démos (`scripts/demo_chXX.py`), nettoyage, rendu (`main`, tag `v1.0`). |
