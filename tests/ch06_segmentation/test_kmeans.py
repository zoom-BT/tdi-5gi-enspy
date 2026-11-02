"""Tests de timg.ch06_segmentation.kmeans (M11). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch06_segmentation.kmeans as m
from tests.conftest import implemente


@implemente(m.kmeans)
def test_kmeans_existe():
    assert callable(m.kmeans)
    # TODO M11: remplacer par un test réel


@implemente(m.segmenter_kmeans_gris)
def test_segmenter_kmeans_gris_existe():
    assert callable(m.segmenter_kmeans_gris)
    # TODO M11: remplacer par un test réel


@implemente(m.segmenter_kmeans_couleur)
def test_segmenter_kmeans_couleur_existe():
    assert callable(m.segmenter_kmeans_couleur)
    # TODO M11: remplacer par un test réel

