"""Ch7 - connexite

Responsable : M04 (Membre 4)
Branche     : m04/ch07-connexite
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def voisins(p, connexite=4):
    """Coordonnées N4(p) ou N8(p)."""
    raise NotImplementedError("M04: voisins")


def distance_d4(p, q):
    """Distance de Manhattan."""
    raise NotImplementedError("M04: distance_d4")


def distance_d8(p, q):
    """Distance de l'échiquier."""
    raise NotImplementedError("M04: distance_d8")


def carte_distances(binaire, metrique='d4'):
    """Bonus : transformée de distance (2 passes)."""
    raise NotImplementedError("M04: carte_distances")

