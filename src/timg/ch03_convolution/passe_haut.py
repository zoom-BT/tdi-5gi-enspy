"""Ch3 - passe_haut

Responsable : M05 (Membre 5)
Branche     : m05/ch03-passe_haut
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def filtre_passe_haut(img, noyau=None):
    """Accentuation des détails (ex. noyau [[0,-1,0],[-1,5,-1],[0,-1,0]])."""
    raise NotImplementedError("M05: filtre_passe_haut")


def accentuation_unsharp(img, k=1.0, sigma=1.0):
    """Rehaussement I + k (I - lissé)."""
    raise NotImplementedError("M05: accentuation_unsharp")

