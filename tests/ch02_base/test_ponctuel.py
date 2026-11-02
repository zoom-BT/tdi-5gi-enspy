"""Tests de timg.ch02_base.ponctuel (M03). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch02_base.ponctuel as m
from tests.conftest import implemente


@implemente(m.appliquer_lut)
def test_appliquer_lut_existe():
    assert callable(m.appliquer_lut)
    # TODO M03: remplacer par un test réel


@implemente(m.transformation_lineaire)
def test_transformation_lineaire_existe():
    assert callable(m.transformation_lineaire)
    # TODO M03: remplacer par un test réel


@implemente(m.transformation_lineaire_saturation)
def test_transformation_lineaire_saturation_existe():
    assert callable(m.transformation_lineaire_saturation)
    # TODO M03: remplacer par un test réel


@implemente(m.transformation_par_morceaux)
def test_transformation_par_morceaux_existe():
    assert callable(m.transformation_par_morceaux)
    # TODO M03: remplacer par un test réel


@implemente(m.correction_gamma)
def test_correction_gamma_existe():
    assert callable(m.correction_gamma)
    # TODO M03: remplacer par un test réel


@implemente(m.negatif)
def test_negatif_existe():
    assert callable(m.negatif)
    # TODO M03: remplacer par un test réel


@implemente(m.transformation_log)
def test_transformation_log_existe():
    assert callable(m.transformation_log)
    # TODO M03: remplacer par un test réel

