"""Tests de timg.ch03_convolution.lissage (M05). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch03_convolution.lissage as m
from tests.conftest import implemente


@implemente(m.noyau_moyenneur)
def test_noyau_moyenneur_existe():
    assert callable(m.noyau_moyenneur)
    # TODO M05: remplacer par un test réel


@implemente(m.filtre_moyenneur)
def test_filtre_moyenneur_existe():
    assert callable(m.filtre_moyenneur)
    # TODO M05: remplacer par un test réel


@implemente(m.noyau_gaussien)
def test_noyau_gaussien_existe():
    assert callable(m.noyau_gaussien)
    # TODO M05: remplacer par un test réel


@implemente(m.filtre_gaussien)
def test_filtre_gaussien_existe():
    assert callable(m.filtre_gaussien)
    # TODO M05: remplacer par un test réel

