"""Tests de timg.ch05_contours.hough (M10). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch05_contours.hough as m
from tests.conftest import implemente


@implemente(m.hough_droites)
def test_hough_droites_existe():
    assert callable(m.hough_droites)
    # TODO M10: remplacer par un test réel


@implemente(m.pics_hough)
def test_pics_hough_existe():
    assert callable(m.pics_hough)
    # TODO M10: remplacer par un test réel


@implemente(m.tracer_droites)
def test_tracer_droites_existe():
    assert callable(m.tracer_droites)
    # TODO M10: remplacer par un test réel

