"""Tests de timg.ch07_binaires.hysteresis (M10). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch07_binaires.hysteresis as m
from tests.conftest import implemente


@implemente(m.seuillage_hysteresis)
def test_seuillage_hysteresis_existe():
    assert callable(m.seuillage_hysteresis)
    # TODO M10: remplacer par un test réel

