"""Ch6 - croissance

Responsable : M12 (Membre 12)
Branche     : m12/ch06-croissance
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def croissance_region(img, germe, seuil=10, connexite=4):
    """Fait croître une région depuis un germe (critère |I - moyenne| < seuil)."""
    raise NotImplementedError("M12: croissance_region")


def croissance_multi_germes(img, germes, seuil=10, connexite=4):
    """Plusieurs germes -> image d'étiquettes."""
    raise NotImplementedError("M12: croissance_multi_germes")


def germes_automatiques(img, n=5):
    """Choix de germes en évitant les zones de fort gradient."""
    raise NotImplementedError("M12: germes_automatiques")

