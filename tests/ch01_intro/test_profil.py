"""Tests de timg.ch01_intro.profil (M01). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch01_intro.profil as m
from tests.conftest import implemente


@implemente(m.profil_ligne)
def test_profil_ligne_existe():
    assert callable(m.profil_ligne)
    # TODO M01: remplacer par un test réel


@implemente(m.profil_colonne)
def test_profil_colonne_existe():
    assert callable(m.profil_colonne)
    # TODO M01: remplacer par un test réel


@implemente(m.profil_segment)
def test_profil_segment_existe():
    assert callable(m.profil_segment)
    # TODO M01: remplacer par un test réel

