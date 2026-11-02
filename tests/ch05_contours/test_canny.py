"""Tests de timg.ch05_contours.canny (M10). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch05_contours.canny as m
from tests.conftest import implemente


@implemente(m.suppression_non_maxima)
def test_suppression_non_maxima_existe():
    assert callable(m.suppression_non_maxima)
    # TODO M10: remplacer par un test réel


@implemente(m.canny)
def test_canny_existe():
    assert callable(m.canny)
    # TODO M10: remplacer par un test réel

