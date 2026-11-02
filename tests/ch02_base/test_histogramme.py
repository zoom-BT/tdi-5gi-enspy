"""Tests de timg.ch02_base.histogramme (M02). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch02_base.histogramme as m
from tests.conftest import implemente


@implemente(m.histogramme)
def test_histogramme_existe():
    assert callable(m.histogramme)
    # TODO M02: remplacer par un test réel


@implemente(m.histogramme_normalise)
def test_histogramme_normalise_existe():
    assert callable(m.histogramme_normalise)
    # TODO M02: remplacer par un test réel


@implemente(m.histogramme_cumule)
def test_histogramme_cumule_existe():
    assert callable(m.histogramme_cumule)
    # TODO M02: remplacer par un test réel


@implemente(m.egalisation)
def test_egalisation_existe():
    assert callable(m.egalisation)
    # TODO M02: remplacer par un test réel


@implemente(m.egalisation_locale)
def test_egalisation_locale_existe():
    assert callable(m.egalisation_locale)
    # TODO M02: remplacer par un test réel


@implemente(m.specification_histogramme)
def test_specification_histogramme_existe():
    assert callable(m.specification_histogramme)
    # TODO M02: remplacer par un test réel


@implemente(m.histogramme)
def test_histogramme_vs_bincount(rampe):
    h = m.histogramme(rampe)
    assert np.array_equal(h, np.bincount(rampe.ravel(), minlength=256))
