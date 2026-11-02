"""Tests de timg.ch02_base.stats (M02). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch02_base.stats as m
from tests.conftest import implemente


@implemente(m.luminance)
def test_luminance_existe():
    assert callable(m.luminance)
    # TODO M02: remplacer par un test réel


@implemente(m.contraste_ecart_type)
def test_contraste_ecart_type_existe():
    assert callable(m.contraste_ecart_type)
    # TODO M02: remplacer par un test réel


@implemente(m.contraste_min_max)
def test_contraste_min_max_existe():
    assert callable(m.contraste_min_max)
    # TODO M02: remplacer par un test réel


@implemente(m.dynamique)
def test_dynamique_existe():
    assert callable(m.dynamique)
    # TODO M02: remplacer par un test réel

