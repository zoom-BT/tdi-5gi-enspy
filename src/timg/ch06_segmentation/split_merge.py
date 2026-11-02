"""Ch6 - split_merge

Responsable : M12 (Membre 12)
Branche     : m12/ch06-split_merge
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def est_homogene(bloc, critere='variance', seuil=100):
    """Prédicat d'homogénéité (variance ou max-min)."""
    raise NotImplementedError("M12: est_homogene")


def division(img, taille_min=4, **critere):
    """Phase split : quadtree ; retourne la liste des feuilles (y, x, h, w)."""
    raise NotImplementedError("M12: division")


def fusion(img, feuilles, **critere):
    """Phase merge : regroupe les feuilles adjacentes homogènes ; retourne une image d'étiquettes."""
    raise NotImplementedError("M12: fusion")


def split_and_merge(img, **critere):
    """Division puis fusion."""
    raise NotImplementedError("M12: split_and_merge")

