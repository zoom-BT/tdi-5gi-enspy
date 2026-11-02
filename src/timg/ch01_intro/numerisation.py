"""Ch1 - numerisation

Responsable : M01 (Membre 1)
Branche     : m01/ch01-numerisation
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def rgb_vers_gris(img, poids=(0.299, 0.587, 0.114)):
    """Convertit une image RVB (H,W,3) en niveaux de gris uint8."""
    raise NotImplementedError("M01: rgb_vers_gris")


def extraire_canal(img, canal):
    """Retourne le canal 'R', 'G' ou 'B' d'une image couleur."""
    raise NotImplementedError("M01: extraire_canal")


def echantillonner(img, facteur):
    """Réduit la résolution spatiale (garde 1 pixel sur `facteur`)."""
    raise NotImplementedError("M01: echantillonner")


def quantifier(img, k_bits):
    """Réduit la résolution tonale à L = 2**k_bits niveaux."""
    raise NotImplementedError("M01: quantifier")


def taille_stockage_bits(m, n, k):
    """b = M x N x K (formule du cours)."""
    raise NotImplementedError("M01: taille_stockage_bits")

