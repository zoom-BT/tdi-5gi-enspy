"""Tests de timg.ch04_fourier.fft (M07). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch04_fourier.fft as m
from tests.conftest import implemente


@implemente(m.fft1d)
def test_fft1d_existe():
    assert callable(m.fft1d)
    # TODO M07: remplacer par un test réel


@implemente(m.ifft1d)
def test_ifft1d_existe():
    assert callable(m.ifft1d)
    # TODO M07: remplacer par un test réel


@implemente(m.pad_puissance_de_2)
def test_pad_puissance_de_2_existe():
    assert callable(m.pad_puissance_de_2)
    # TODO M07: remplacer par un test réel


@implemente(m.fft2d)
def test_fft2d_existe():
    assert callable(m.fft2d)
    # TODO M07: remplacer par un test réel


@implemente(m.ifft2d)
def test_ifft2d_existe():
    assert callable(m.ifft2d)
    # TODO M07: remplacer par un test réel


@implemente(m.fftshift)
def test_fftshift_existe():
    assert callable(m.fftshift)
    # TODO M07: remplacer par un test réel


@implemente(m.ifftshift)
def test_ifftshift_existe():
    assert callable(m.ifftshift)
    # TODO M07: remplacer par un test réel


@implemente(m.fft2d)
def test_fft2d_vs_numpy():
    x = np.random.default_rng(0).random((16, 8))
    assert np.allclose(m.fft2d(x), np.fft.fft2(x))  # numpy.fft autorisé ici comme référence
