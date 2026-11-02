"""Tests de timg.ch07_binaires.freeman (M04). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch07_binaires.freeman as m
from tests.conftest import implemente


@implemente(m.code_freeman)
def test_code_freeman_existe():
    assert callable(m.code_freeman)
    # TODO M04: remplacer par un test réel


@implemente(m.decoder_freeman)
def test_decoder_freeman_existe():
    assert callable(m.decoder_freeman)
    # TODO M04: remplacer par un test réel


@implemente(m.suivi_contour)
def test_suivi_contour_existe():
    assert callable(m.suivi_contour)
    # TODO M04: remplacer par un test réel

