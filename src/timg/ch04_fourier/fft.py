"""Ch4 - fft

Responsable : M07 (Membre 7)
Branche     : m07/ch04-fft
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def fft1d(x):
    """FFT radix-2 (Cooley-Tukey) d'un signal de taille puissance de 2. numpy.fft interdit ici."""
    raise NotImplementedError("M07: fft1d")


def ifft1d(X):
    """FFT inverse 1D."""
    raise NotImplementedError("M07: ifft1d")


def pad_puissance_de_2(img):
    """Complète l'image par des zéros jusqu'à des tailles puissances de 2."""
    raise NotImplementedError("M07: pad_puissance_de_2")


def fft2d(img):
    """FFT 2D (lignes puis colonnes) ; retourne un tableau complexe."""
    raise NotImplementedError("M07: fft2d")


def ifft2d(F):
    """FFT inverse 2D."""
    raise NotImplementedError("M07: ifft2d")


def fftshift(F):
    """Inversion des quadrants (composante continue au centre)."""
    raise NotImplementedError("M07: fftshift")


def ifftshift(F):
    """Inverse de fftshift."""
    raise NotImplementedError("M07: ifftshift")

