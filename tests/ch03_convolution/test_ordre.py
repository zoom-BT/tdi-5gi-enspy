"""Tests de timg.ch03_convolution.ordre (M06). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch03_convolution.ordre as m
from tests.conftest import implemente


@implemente(m.filtre_median)
def test_filtre_median_existe():
    assert callable(m.filtre_median)
    # TODO M06: remplacer par un test réel


@implemente(m.filtre_min)
def test_filtre_min_existe():
    assert callable(m.filtre_min)
    # TODO M06: remplacer par un test réel


@implemente(m.filtre_max)
def test_filtre_max_existe():
    assert callable(m.filtre_max)
    # TODO M06: remplacer par un test réel

