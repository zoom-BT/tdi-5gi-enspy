"""Ch7 - freeman

Responsable : M04 (Membre 4)
Branche     : m04/ch07-freeman
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def code_freeman(contour_binaire, connexite=8):
    """Code de chaîne depuis le pixel en haut à gauche, sens horaire."""
    raise NotImplementedError("M04: code_freeman")


def decoder_freeman(depart, code, forme):
    """Reconstruit le contour à partir du code."""
    raise NotImplementedError("M04: decoder_freeman")


def suivi_contour(binaire):
    """Suivi du contour extérieur d'un objet (liste ordonnée de pixels)."""
    raise NotImplementedError("M04: suivi_contour")

