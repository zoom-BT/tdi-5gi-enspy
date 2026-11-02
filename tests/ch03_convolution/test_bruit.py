"""Tests de timg.ch03_convolution.bruit (M06). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch03_convolution.bruit as m
from tests.conftest import implemente


@implemente(m.bruit_poivre_sel)
def test_bruit_poivre_sel_existe():
    assert callable(m.bruit_poivre_sel)
    # TODO M06: remplacer par un test réel


@implemente(m.bruit_gaussien)
def test_bruit_gaussien_existe():
    assert callable(m.bruit_gaussien)
    # TODO M06: remplacer par un test réel


@implemente(m.psnr)
def test_psnr_existe():
    assert callable(m.psnr)
    # TODO M06: remplacer par un test réel

