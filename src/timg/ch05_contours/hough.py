"""Ch5 - hough

Responsable : M10 (Membre 10)
Branche     : m10/ch05-hough
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def hough_droites(contours, n_theta=180, pas_rho=1.0):
    """Accumulateur (rho, theta) avec rho = x cos(theta) + y sin(theta)."""
    raise NotImplementedError("M10: hough_droites")


def pics_hough(accumulateur, n_pics=5, seuil=None, voisinage=5):
    """Maxima locaux de l'accumulateur."""
    raise NotImplementedError("M10: pics_hough")


def tracer_droites(forme, droites):
    """Dessine les droites détectées sur une image."""
    raise NotImplementedError("M10: tracer_droites")

