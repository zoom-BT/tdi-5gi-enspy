"""Ch4 - spectre

Responsable : M07 (Membre 7)
Branche     : m07/ch04-spectre
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def module(F):
    """|F(u,v)| = sqrt(Re^2 + Im^2)."""
    raise NotImplementedError("M07: module")


def phase(F):
    """Phase arctan(Im/Re)."""
    raise NotImplementedError("M07: phase")


def spectre_log(F):
    """Spectre rehaussé log(1 + |F|), normalisé 0..255 pour affichage."""
    raise NotImplementedError("M07: spectre_log")


def image_sinus(taille, frequence, angle=0.0):
    """Image test sinusoïdale."""
    raise NotImplementedError("M07: image_sinus")


def image_carre(taille, cote):
    """Image test carré / rectangle centré."""
    raise NotImplementedError("M07: image_carre")


def image_impulsions(taille, pas):
    """Image test d'impulsions."""
    raise NotImplementedError("M07: image_impulsions")

