"""Tests de timg.ch06_segmentation.split_merge (M12). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch06_segmentation.split_merge as m
from tests.conftest import implemente


@implemente(m.est_homogene)
def test_est_homogene_existe():
    assert callable(m.est_homogene)
    # TODO M12: remplacer par un test réel


@implemente(m.division)
def test_division_existe():
    assert callable(m.division)
    # TODO M12: remplacer par un test réel


@implemente(m.fusion)
def test_fusion_existe():
    assert callable(m.fusion)
    # TODO M12: remplacer par un test réel


@implemente(m.split_and_merge)
def test_split_and_merge_existe():
    assert callable(m.split_and_merge)
    # TODO M12: remplacer par un test réel

