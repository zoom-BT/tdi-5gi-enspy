"""Ch7 - etiquetage

Responsable : M04 (Membre 4)
Branche     : m04/ch07-etiquetage
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def etiqueter_multi_passes(binaire, connexite=4):
    """Parcours aller/retour jusqu'à stabilité des étiquettes."""
    raise NotImplementedError("M04: etiqueter_multi_passes")


def etiqueter_une_passe(binaire, connexite=4):
    """Une passe + table d'équivalence (union-find)."""
    raise NotImplementedError("M04: etiqueter_une_passe")


def etiqueter_contours(contours):
    """Etiquetage en 8-connexité (4 voisins déjà vus)."""
    raise NotImplementedError("M04: etiqueter_contours")


def proprietes_regions(etiquettes):
    """Aire, boîte englobante, centroïde par étiquette."""
    raise NotImplementedError("M04: proprietes_regions")

