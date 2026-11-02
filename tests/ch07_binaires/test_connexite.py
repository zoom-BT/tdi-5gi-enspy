"""Tests de timg.ch07_binaires.connexite (M04). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch07_binaires.connexite as m
from tests.conftest import implemente


@implemente(m.voisins)
def test_voisins_existe():
    assert callable(m.voisins)
    # TODO M04: remplacer par un test réel


@implemente(m.distance_d4)
def test_distance_d4_existe():
    assert callable(m.distance_d4)
    # TODO M04: remplacer par un test réel


@implemente(m.distance_d8)
def test_distance_d8_existe():
    assert callable(m.distance_d8)
    # TODO M04: remplacer par un test réel


@implemente(m.carte_distances)
def test_carte_distances_existe():
    assert callable(m.carte_distances)
    # TODO M04: remplacer par un test réel

