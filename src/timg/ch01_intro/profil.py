"""Ch1 - profil

Responsable : M01 (Membre 1)
Branche     : m01/ch01-profil
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def profil_ligne(img, y):
    """Profil d'intensité 1D de la ligne y."""
    raise NotImplementedError("M01: profil_ligne")


def profil_colonne(img, x):
    """Profil d'intensité 1D de la colonne x."""
    raise NotImplementedError("M01: profil_colonne")


def profil_segment(img, p0, p1, n_points=None):
    """Profil d'intensité le long d'un segment p0->p1 (échantillonnage)."""
    raise NotImplementedError("M01: profil_segment")

