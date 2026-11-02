"""Ch3 - lissage

Responsable : M05 (Membre 5)
Branche     : m05/ch03-lissage
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def noyau_moyenneur(taille):
    """Noyau NxN de coefficients 1/N^2."""
    raise NotImplementedError("M05: noyau_moyenneur")


def filtre_moyenneur(img, taille=3):
    """Lissage par moyenne NxN."""
    raise NotImplementedError("M05: filtre_moyenneur")


def noyau_gaussien(taille, sigma):
    """Noyau gaussien normalisé (somme = 1)."""
    raise NotImplementedError("M05: noyau_gaussien")


def filtre_gaussien(img, taille=5, sigma=1.0):
    """Lissage gaussien."""
    raise NotImplementedError("M05: filtre_gaussien")

