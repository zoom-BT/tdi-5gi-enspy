"""Ch2 - arithmetique

Responsable : M03 (Membre 3)
Branche     : m03/ch02-arithmetique
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def et_logique(a, b):
    """ET pixel à pixel (binaires ou bit à bit)."""
    raise NotImplementedError("M03: et_logique")


def ou_logique(a, b):
    """OU pixel à pixel."""
    raise NotImplementedError("M03: ou_logique")


def xor_logique(a, b):
    """OU exclusif."""
    raise NotImplementedError("M03: xor_logique")


def non_logique(a):
    """Complément."""
    raise NotImplementedError("M03: non_logique")


def addition(f, g):
    """R = min(f + g, 255)."""
    raise NotImplementedError("M03: addition")


def soustraction(f, g):
    """S = max(f - g, 0)."""
    raise NotImplementedError("M03: soustraction")


def difference_absolue(f, g):
    """|f - g| (détection de mouvement)."""
    raise NotImplementedError("M03: difference_absolue")


def multiplication(f, ratio):
    """S = min(f * ratio, 255)."""
    raise NotImplementedError("M03: multiplication")


def combinaison_lineaire(f, g, alpha=0.5):
    """alpha f + (1 - alpha) g."""
    raise NotImplementedError("M03: combinaison_lineaire")

