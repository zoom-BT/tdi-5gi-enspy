"""Tests de timg.ch03_convolution.passe_haut (M05). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch03_convolution.passe_haut as m
from tests.conftest import implemente


@implemente(m.filtre_passe_haut)
def test_filtre_passe_haut_existe():
    assert callable(m.filtre_passe_haut)
    # TODO M05: remplacer par un test réel


@implemente(m.accentuation_unsharp)
def test_accentuation_unsharp_existe():
    assert callable(m.accentuation_unsharp)
    # TODO M05: remplacer par un test réel

