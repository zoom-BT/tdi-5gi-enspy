"""Ch3 - ordre

Responsable : M06 (Membre 6)
Branche     : m06/ch03-ordre
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def filtre_median(img, taille=3):
    """Médiane du voisinage NxN (non linéaire)."""
    raise NotImplementedError("M06: filtre_median")


def filtre_min(img, taille=3):
    """Minimum du voisinage (V8 si 3x3)."""
    raise NotImplementedError("M06: filtre_min")


def filtre_max(img, taille=3):
    """Maximum du voisinage."""
    raise NotImplementedError("M06: filtre_max")

