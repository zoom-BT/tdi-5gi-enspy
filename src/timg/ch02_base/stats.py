"""Ch2 - stats

Responsable : M02 (Membre 2)
Branche     : m02/ch02-stats
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def luminance(img):
    """Moyenne de tous les pixels."""
    raise NotImplementedError("M02: luminance")


def contraste_ecart_type(img):
    """Contraste = écart-type des niveaux de gris."""
    raise NotImplementedError("M02: contraste_ecart_type")


def contraste_min_max(img):
    """Contraste = (max - min) / (max + min) ou max-min (documenter le choix)."""
    raise NotImplementedError("M02: contraste_min_max")


def dynamique(img):
    """Retourne (valeur_min, valeur_max)."""
    raise NotImplementedError("M02: dynamique")

