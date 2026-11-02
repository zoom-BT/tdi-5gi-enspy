"""Tests de timg.ch06_segmentation.croissance (M12). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch06_segmentation.croissance as m
from tests.conftest import implemente


@implemente(m.croissance_region)
def test_croissance_region_existe():
    assert callable(m.croissance_region)
    # TODO M12: remplacer par un test réel


@implemente(m.croissance_multi_germes)
def test_croissance_multi_germes_existe():
    assert callable(m.croissance_multi_germes)
    # TODO M12: remplacer par un test réel


@implemente(m.germes_automatiques)
def test_germes_automatiques_existe():
    assert callable(m.germes_automatiques)
    # TODO M12: remplacer par un test réel

