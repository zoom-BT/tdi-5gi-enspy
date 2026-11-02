"""Ch5 - laplacien

Responsable : M09 (Membre 9)
Branche     : m09/ch05-laplacien
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def laplacien(img, connexite=4):
    """Masques [[0,1,0],[1,-4,1],[0,1,0]] (4) ou [[1,1,1],[1,-8,1],[1,1,1]] (8)."""
    raise NotImplementedError("M09: laplacien")


def passages_par_zero(lap, seuil=0):
    """Contours = changements de signe du laplacien."""
    raise NotImplementedError("M09: passages_par_zero")


def log(img, sigma=1.4):
    """Bonus : Laplacien de gaussienne."""
    raise NotImplementedError("M09: log")

