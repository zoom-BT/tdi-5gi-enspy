"""Ch6 - seuillage

Responsable : M11 (Membre 11)
Branche     : m11/ch06-seuillage
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def seuillage(img, seuil):
    """Binaire : 1 si f >= T sinon 0."""
    raise NotImplementedError("M11: seuillage")


def multi_seuillage(img, seuils):
    """n seuils -> n+1 classes."""
    raise NotImplementedError("M11: multi_seuillage")


def seuil_moyenne(img):
    """T = moyenne des niveaux de gris."""
    raise NotImplementedError("M11: seuil_moyenne")


def seuil_milieu_min_max(img):
    """T = (min + max) / 2."""
    raise NotImplementedError("M11: seuil_milieu_min_max")


def seuil_iteratif(img, eps=0.5):
    """Seuil qui 'balance' les deux classes (itératif)."""
    raise NotImplementedError("M11: seuil_iteratif")


def seuil_otsu(img):
    """Minimise la variance intra-classe P1 s1^2 + P2 s2^2."""
    raise NotImplementedError("M11: seuil_otsu")


def seuillage_adaptatif(img, taille_bloc=64, variance_min=100):
    """Seuil par sous-image ; blocs à variance < seuil non traités."""
    raise NotImplementedError("M11: seuillage_adaptatif")

