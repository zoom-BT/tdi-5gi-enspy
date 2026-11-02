"""Ch7 - fermeture_contours

Responsable : M09 (Membre 9)
Branche     : m09/ch07-fermeture_contours
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def fermer_contours(contours, norme_gradient, distance_max=5):
    """Relie les extrémités de contours en suivant le chemin de gradient le plus fort."""
    raise NotImplementedError("M09: fermer_contours")


def extremites(contours):
    """Détecte les extrémités de contours (pixels avec un seul voisin 8-connexe)."""
    raise NotImplementedError("M09: extremites")

