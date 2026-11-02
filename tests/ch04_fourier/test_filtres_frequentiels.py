"""Tests de timg.ch04_fourier.filtres_frequentiels (M08). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch04_fourier.filtres_frequentiels as m
from tests.conftest import implemente


@implemente(m.masque_passe_bas_ideal)
def test_masque_passe_bas_ideal_existe():
    assert callable(m.masque_passe_bas_ideal)
    # TODO M08: remplacer par un test réel


@implemente(m.masque_passe_haut_ideal)
def test_masque_passe_haut_ideal_existe():
    assert callable(m.masque_passe_haut_ideal)
    # TODO M08: remplacer par un test réel


@implemente(m.masque_gaussien)
def test_masque_gaussien_existe():
    assert callable(m.masque_gaussien)
    # TODO M08: remplacer par un test réel


@implemente(m.filtrer_frequentiel)
def test_filtrer_frequentiel_existe():
    assert callable(m.filtrer_frequentiel)
    # TODO M08: remplacer par un test réel


@implemente(m.energie_par_rayon)
def test_energie_par_rayon_existe():
    assert callable(m.energie_par_rayon)
    # TODO M08: remplacer par un test réel


@implemente(m.filtre_notch)
def test_filtre_notch_existe():
    assert callable(m.filtre_notch)
    # TODO M08: remplacer par un test réel


@implemente(m.rehaussement_frequentiel)
def test_rehaussement_frequentiel_existe():
    assert callable(m.rehaussement_frequentiel)
    # TODO M08: remplacer par un test réel

