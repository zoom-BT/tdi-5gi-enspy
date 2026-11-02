"""Tests de timg.ch03_convolution.convolution (M05). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch03_convolution.convolution as m
from tests.conftest import implemente


@implemente(m.pad)
def test_pad_existe():
    assert callable(m.pad)
    # TODO M05: remplacer par un test réel


@implemente(m.convolution2d)
def test_convolution2d_existe():
    assert callable(m.convolution2d)
    # TODO M05: remplacer par un test réel


@implemente(m.convolution_partielle)
def test_convolution_partielle_existe():
    assert callable(m.convolution_partielle)
    # TODO M05: remplacer par un test réel


@implemente(m.convolution_separable)
def test_convolution_separable_existe():
    assert callable(m.convolution_separable)
    # TODO M05: remplacer par un test réel


@implemente(m.convolution2d)
def test_identite(rampe):
    k = np.zeros((3, 3)); k[1, 1] = 1
    assert np.allclose(m.convolution2d(rampe, k), rampe)
