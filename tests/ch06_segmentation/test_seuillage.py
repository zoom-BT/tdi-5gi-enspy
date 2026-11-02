"""Tests de timg.ch06_segmentation.seuillage (M11). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch06_segmentation.seuillage as m
from tests.conftest import implemente


@implemente(m.seuillage)
def test_seuillage_existe():
    assert callable(m.seuillage)
    # TODO M11: remplacer par un test réel


@implemente(m.multi_seuillage)
def test_multi_seuillage_existe():
    assert callable(m.multi_seuillage)
    # TODO M11: remplacer par un test réel


@implemente(m.seuil_moyenne)
def test_seuil_moyenne_existe():
    assert callable(m.seuil_moyenne)
    # TODO M11: remplacer par un test réel


@implemente(m.seuil_milieu_min_max)
def test_seuil_milieu_min_max_existe():
    assert callable(m.seuil_milieu_min_max)
    # TODO M11: remplacer par un test réel


@implemente(m.seuil_iteratif)
def test_seuil_iteratif_existe():
    assert callable(m.seuil_iteratif)
    # TODO M11: remplacer par un test réel


@implemente(m.seuil_otsu)
def test_seuil_otsu_existe():
    assert callable(m.seuil_otsu)
    # TODO M11: remplacer par un test réel


@implemente(m.seuillage_adaptatif)
def test_seuillage_adaptatif_existe():
    assert callable(m.seuillage_adaptatif)
    # TODO M11: remplacer par un test réel


@implemente(m.seuil_otsu)
def test_otsu_bimodal():
    img = np.r_[np.full(500, 50), np.full(500, 200)].astype(np.uint8).reshape(25, 40)
    assert 50 <= m.seuil_otsu(img) < 200
