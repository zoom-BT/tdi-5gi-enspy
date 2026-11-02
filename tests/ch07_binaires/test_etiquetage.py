"""Tests de timg.ch07_binaires.etiquetage (M04). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch07_binaires.etiquetage as m
from tests.conftest import implemente


@implemente(m.etiqueter_multi_passes)
def test_etiqueter_multi_passes_existe():
    assert callable(m.etiqueter_multi_passes)
    # TODO M04: remplacer par un test réel


@implemente(m.etiqueter_une_passe)
def test_etiqueter_une_passe_existe():
    assert callable(m.etiqueter_une_passe)
    # TODO M04: remplacer par un test réel


@implemente(m.etiqueter_contours)
def test_etiqueter_contours_existe():
    assert callable(m.etiqueter_contours)
    # TODO M04: remplacer par un test réel


@implemente(m.proprietes_regions)
def test_proprietes_regions_existe():
    assert callable(m.proprietes_regions)
    # TODO M04: remplacer par un test réel


@implemente(m.etiqueter_une_passe)
def test_deux_objets():
    b = np.zeros((5, 7), np.uint8); b[1:3, 1:3] = 1; b[2:4, 4:6] = 1
    lab = m.etiqueter_une_passe(b, connexite=4)
    assert len(np.unique(lab[lab > 0])) == 2
