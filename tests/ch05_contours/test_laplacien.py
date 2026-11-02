"""Tests de timg.ch05_contours.laplacien (M09). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch05_contours.laplacien as m
from tests.conftest import implemente


@implemente(m.laplacien)
def test_laplacien_existe():
    assert callable(m.laplacien)
    # TODO M09: remplacer par un test réel


@implemente(m.passages_par_zero)
def test_passages_par_zero_existe():
    assert callable(m.passages_par_zero)
    # TODO M09: remplacer par un test réel


@implemente(m.log)
def test_log_existe():
    assert callable(m.log)
    # TODO M09: remplacer par un test réel

