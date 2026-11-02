"""Tests de timg.ch07_binaires.morphologie (M06). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch07_binaires.morphologie as m
from tests.conftest import implemente


@implemente(m.element_structurant)
def test_element_structurant_existe():
    assert callable(m.element_structurant)
    # TODO M06: remplacer par un test réel


@implemente(m.erosion)
def test_erosion_existe():
    assert callable(m.erosion)
    # TODO M06: remplacer par un test réel


@implemente(m.dilatation)
def test_dilatation_existe():
    assert callable(m.dilatation)
    # TODO M06: remplacer par un test réel


@implemente(m.ouverture)
def test_ouverture_existe():
    assert callable(m.ouverture)
    # TODO M06: remplacer par un test réel


@implemente(m.fermeture)
def test_fermeture_existe():
    assert callable(m.fermeture)
    # TODO M06: remplacer par un test réel


@implemente(m.gradient_interne)
def test_gradient_interne_existe():
    assert callable(m.gradient_interne)
    # TODO M06: remplacer par un test réel


@implemente(m.gradient_externe)
def test_gradient_externe_existe():
    assert callable(m.gradient_externe)
    # TODO M06: remplacer par un test réel


@implemente(m.gradient_morphologique)
def test_gradient_morphologique_existe():
    assert callable(m.gradient_morphologique)
    # TODO M06: remplacer par un test réel

