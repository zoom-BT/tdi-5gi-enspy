"""Tests de timg.ch05_contours.gradient (M09). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch05_contours.gradient as m
from tests.conftest import implemente


@implemente(m.derivee_simple)
def test_derivee_simple_existe():
    assert callable(m.derivee_simple)
    # TODO M09: remplacer par un test réel


@implemente(m.roberts)
def test_roberts_existe():
    assert callable(m.roberts)
    # TODO M09: remplacer par un test réel


@implemente(m.prewitt)
def test_prewitt_existe():
    assert callable(m.prewitt)
    # TODO M09: remplacer par un test réel


@implemente(m.sobel)
def test_sobel_existe():
    assert callable(m.sobel)
    # TODO M09: remplacer par un test réel


@implemente(m.isotropique)
def test_isotropique_existe():
    assert callable(m.isotropique)
    # TODO M09: remplacer par un test réel


@implemente(m.norme_gradient)
def test_norme_gradient_existe():
    assert callable(m.norme_gradient)
    # TODO M09: remplacer par un test réel


@implemente(m.direction_gradient)
def test_direction_gradient_existe():
    assert callable(m.direction_gradient)
    # TODO M09: remplacer par un test réel


@implemente(m.seuiller_gradient)
def test_seuiller_gradient_existe():
    assert callable(m.seuiller_gradient)
    # TODO M09: remplacer par un test réel

