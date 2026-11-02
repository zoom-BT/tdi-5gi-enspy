"""Ch3 - bruit

Responsable : M06 (Membre 6)
Branche     : m06/ch03-bruit
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def bruit_poivre_sel(img, proportion=0.05, graine=None):
    """Ajoute un bruit poivre et sel."""
    raise NotImplementedError("M06: bruit_poivre_sel")


def bruit_gaussien(img, sigma=10.0, graine=None):
    """Ajoute un bruit gaussien additif."""
    raise NotImplementedError("M06: bruit_gaussien")


def psnr(ref, img):
    """PSNR pour comparer les débruitages (moyenne vs gaussien vs médian)."""
    raise NotImplementedError("M06: psnr")

