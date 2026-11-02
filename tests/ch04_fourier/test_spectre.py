"""Tests de timg.ch04_fourier.spectre (M07). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch04_fourier.spectre as m
from tests.conftest import implemente


@implemente(m.module)
def test_module_existe():
    assert callable(m.module)
    # TODO M07: remplacer par un test réel


@implemente(m.phase)
def test_phase_existe():
    assert callable(m.phase)
    # TODO M07: remplacer par un test réel


@implemente(m.spectre_log)
def test_spectre_log_existe():
    assert callable(m.spectre_log)
    # TODO M07: remplacer par un test réel


@implemente(m.image_sinus)
def test_image_sinus_existe():
    assert callable(m.image_sinus)
    # TODO M07: remplacer par un test réel


@implemente(m.image_carre)
def test_image_carre_existe():
    assert callable(m.image_carre)
    # TODO M07: remplacer par un test réel


@implemente(m.image_impulsions)
def test_image_impulsions_existe():
    assert callable(m.image_impulsions)
    # TODO M07: remplacer par un test réel

