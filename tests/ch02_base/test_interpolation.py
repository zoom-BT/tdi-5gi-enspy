"""Tests de timg.ch02_base.interpolation (M01). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch02_base.interpolation as m
from tests.conftest import implemente


@implemente(m.zoom_plus_proche_voisin)
def test_zoom_plus_proche_voisin_existe():
    assert callable(m.zoom_plus_proche_voisin)
    # TODO M01: remplacer par un test réel


@implemente(m.zoom_bilineaire)
def test_zoom_bilineaire_existe():
    assert callable(m.zoom_bilineaire)
    # TODO M01: remplacer par un test réel


@implemente(m.zoom_bicubique)
def test_zoom_bicubique_existe():
    assert callable(m.zoom_bicubique)
    # TODO M01: remplacer par un test réel


@implemente(m.redimensionner)
def test_redimensionner_existe():
    assert callable(m.redimensionner)
    # TODO M01: remplacer par un test réel

