"""Ch5 - canny

Responsable : M10 (Membre 10)
Branche     : m10/ch05-canny
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def suppression_non_maxima(norme, direction):
    """Amincissement : contours d'épaisseur 1 pixel."""
    raise NotImplementedError("M10: suppression_non_maxima")


def canny(img, sigma=1.4, seuil_bas=20, seuil_haut=50):
    """Pipeline : gaussien -> Sobel -> NMS -> hystérésis."""
    raise NotImplementedError("M10: canny")

