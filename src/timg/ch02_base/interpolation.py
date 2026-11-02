"""Ch2 - interpolation

Responsable : M01 (Membre 1)
Branche     : m01/ch02-interpolation
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def zoom_plus_proche_voisin(img, facteur):
    """Agrandissement par copie des pixels (lignes et colonnes)."""
    raise NotImplementedError("M01: zoom_plus_proche_voisin")


def zoom_bilineaire(img, facteur):
    """Interpolation bilinéaire (4 voisins), extrapolation linéaire au bord."""
    raise NotImplementedError("M01: zoom_bilineaire")


def zoom_bicubique(img, facteur):
    """Interpolation bicubique (16 voisins), formules du cours pour facteur 2 et 3."""
    raise NotImplementedError("M01: zoom_bicubique")


def redimensionner(img, nouvelle_taille, methode='bilineaire'):
    """Redimensionnement général (H', W')."""
    raise NotImplementedError("M01: redimensionner")

