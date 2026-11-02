"""Ch3 - convolution

Responsable : M05 (Membre 5)
Branche     : m05/ch03-convolution
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def pad(img, rayon, mode='zero'):
    """Gestion des bords : 'zero', 'miroir', 'replique'."""
    raise NotImplementedError("M05: pad")


def convolution2d(img, noyau, bord='miroir', normaliser=False):
    """Convolution discrète I'(i,j) = sum_u sum_v I(i-u,j-v) h(u,v) ; taille de sortie = taille d'entrée."""
    raise NotImplementedError("M05: convolution2d")


def convolution_partielle(img, noyau):
    """Convolution partielle au bord (portion du noyau, renormalisée)."""
    raise NotImplementedError("M05: convolution_partielle")


def convolution_separable(img, h_ligne, h_colonne, bord='miroir'):
    """Convolution par deux noyaux 1D (ex. Sobel, gaussien)."""
    raise NotImplementedError("M05: convolution_separable")

