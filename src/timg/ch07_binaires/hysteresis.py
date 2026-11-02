"""Ch7 - hysteresis

Responsable : M10 (Membre 10)
Branche     : m10/ch07-hysteresis
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def seuillage_hysteresis(norme, seuil_bas, seuil_haut):
    """(1) seuil haut ; (2) ajout des pixels > seuil bas connectés (8-connexité)."""
    raise NotImplementedError("M10: seuillage_hysteresis")

