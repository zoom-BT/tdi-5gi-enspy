"""Ch5 - gradient

Responsable : M09 (Membre 9)
Branche     : m09/ch05-gradient
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def derivee_simple(img):
    """Dérivées [-1 1] en x et y."""
    raise NotImplementedError("M09: derivee_simple")


def roberts(img):
    """Retourne (Gx, Gy) avec les masques de Roberts."""
    raise NotImplementedError("M09: roberts")


def prewitt(img):
    """Retourne (Gx, Gy) avec Prewitt (moyenneur + dérivée)."""
    raise NotImplementedError("M09: prewitt")


def sobel(img):
    """Retourne (Gx, Gy) avec Sobel (gaussien + dérivée)."""
    raise NotImplementedError("M09: sobel")


def isotropique(img):
    """Retourne (Gx, Gy) avec le filtre isotropique (Frei-Chen)."""
    raise NotImplementedError("M09: isotropique")


def norme_gradient(gx, gy, approx=False):
    """sqrt(Gx^2+Gy^2) ou |Gx|+|Gy|."""
    raise NotImplementedError("M09: norme_gradient")


def direction_gradient(gx, gy):
    """theta = arctan2(Gy, Gx)."""
    raise NotImplementedError("M09: direction_gradient")


def seuiller_gradient(norme, seuil):
    """Pixels contours : |G| > S."""
    raise NotImplementedError("M09: seuiller_gradient")

