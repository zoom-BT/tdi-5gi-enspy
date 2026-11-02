"""Tests de timg.ch01_intro.numerisation (M01). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch01_intro.numerisation as m
from tests.conftest import implemente


@implemente(m.rgb_vers_gris)
def test_rgb_vers_gris_existe():
    assert callable(m.rgb_vers_gris)
    # TODO M01: remplacer par un test réel


@implemente(m.extraire_canal)
def test_extraire_canal_existe():
    assert callable(m.extraire_canal)
    # TODO M01: remplacer par un test réel


@implemente(m.echantillonner)
def test_echantillonner_existe():
    assert callable(m.echantillonner)
    # TODO M01: remplacer par un test réel


@implemente(m.quantifier)
def test_quantifier_existe():
    assert callable(m.quantifier)
    # TODO M01: remplacer par un test réel


@implemente(m.taille_stockage_bits)
def test_taille_stockage_bits_existe():
    assert callable(m.taille_stockage_bits)
    # TODO M01: remplacer par un test réel

