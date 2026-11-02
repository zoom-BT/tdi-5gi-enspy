"""Ch7 - morphologie

Responsable : M06 (Membre 6)
Branche     : m06/ch07-morphologie
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def element_structurant(forme='croix', taille=3):
    """'croix' (4-connexité), 'carre' (8-connexité), 'disque'."""
    raise NotImplementedError("M06: element_structurant")


def erosion(img, es=None):
    """Binaire : pixel conservé si tout l'ES est dans l'objet ; gris : minimum."""
    raise NotImplementedError("M06: erosion")


def dilatation(img, es=None):
    """Binaire : intersection ES/objet non vide ; gris : maximum."""
    raise NotImplementedError("M06: dilatation")


def ouverture(img, es=None):
    """Erosion puis dilatation."""
    raise NotImplementedError("M06: ouverture")


def fermeture(img, es=None):
    """Dilatation puis érosion."""
    raise NotImplementedError("M06: fermeture")


def gradient_interne(img, es=None):
    """Image - érodée (contour intérieur)."""
    raise NotImplementedError("M06: gradient_interne")


def gradient_externe(img, es=None):
    """Dilatée - image (contour extérieur)."""
    raise NotImplementedError("M06: gradient_externe")


def gradient_morphologique(img, es=None):
    """Dilatée - érodée."""
    raise NotImplementedError("M06: gradient_morphologique")

