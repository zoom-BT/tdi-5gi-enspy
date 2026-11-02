"""Tests de timg.ch07_binaires.fermeture_contours (M09). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch07_binaires.fermeture_contours as m
from tests.conftest import implemente


@implemente(m.fermer_contours)
def test_fermer_contours_existe():
    assert callable(m.fermer_contours)
    # TODO M09: remplacer par un test réel


@implemente(m.extremites)
def test_extremites_existe():
    assert callable(m.extremites)
    # TODO M09: remplacer par un test réel

