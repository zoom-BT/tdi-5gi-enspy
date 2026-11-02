"""Ch2 - histogramme

Responsable : M02 (Membre 2)
Branche     : m02/ch02-histogramme
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def histogramme(img, n_niveaux=256):
    """H(k) = nombre de pixels de valeur k (gris ou par canal)."""
    raise NotImplementedError("M02: histogramme")


def histogramme_normalise(img):
    """hn(k) = H(k) / Nbp."""
    raise NotImplementedError("M02: histogramme_normalise")


def histogramme_cumule(img):
    """C(i) = somme_{j<=i} hn(j)."""
    raise NotImplementedError("M02: histogramme_cumule")


def egalisation(img):
    """Egalisation globale : f'(x,y) = C(f(x,y)) * 255."""
    raise NotImplementedError("M02: egalisation")


def egalisation_locale(img, taille_fenetre=7):
    """Egalisation locale (fenêtre NxN autour de chaque pixel)."""
    raise NotImplementedError("M02: egalisation_locale")


def specification_histogramme(img, hist_cible):
    """Spécification (matching) d'histogramme vers un histogramme cible."""
    raise NotImplementedError("M02: specification_histogramme")

