"""Ch6 - kmeans

Responsable : M11 (Membre 11)
Branche     : m11/ch06-kmeans
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def kmeans(donnees, k, max_iter=100, graine=None):
    """K-moyennes (4 étapes du cours) ; retourne (etiquettes, centres)."""
    raise NotImplementedError("M11: kmeans")


def segmenter_kmeans_gris(img, k):
    """K-moyennes sur l'intensité."""
    raise NotImplementedError("M11: segmenter_kmeans_gris")


def segmenter_kmeans_couleur(img, k):
    """K-moyennes sur la couleur (R,G,B)."""
    raise NotImplementedError("M11: segmenter_kmeans_couleur")

