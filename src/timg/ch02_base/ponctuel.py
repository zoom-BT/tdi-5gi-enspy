"""Ch2 - ponctuel

Responsable : M03 (Membre 3)
Branche     : m03/ch02-ponctuel
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def appliquer_lut(img, lut):
    """Applique une table de correspondance (LUT) de 256 entrées."""
    raise NotImplementedError("M03: appliquer_lut")


def transformation_lineaire(img):
    """Etirement : I' = 255 (I - min) / (max - min), via LUT."""
    raise NotImplementedError("M03: transformation_lineaire")


def transformation_lineaire_saturation(img, s_min, s_max):
    """Linéaire avec saturation entre Smin et Smax."""
    raise NotImplementedError("M03: transformation_lineaire_saturation")


def transformation_par_morceaux(img, points):
    """Linéaire par morceaux, points = [(x0,y0),(x1,y1),...]."""
    raise NotImplementedError("M03: transformation_par_morceaux")


def correction_gamma(img, gamma):
    """Transformation non linéaire n' = n**(1/gamma) normalisée."""
    raise NotImplementedError("M03: correction_gamma")


def negatif(img):
    """I' = 255 - I."""
    raise NotImplementedError("M03: negatif")


def transformation_log(img):
    """I' = c log(1 + I)."""
    raise NotImplementedError("M03: transformation_log")

