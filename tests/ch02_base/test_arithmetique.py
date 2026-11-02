"""Tests de timg.ch02_base.arithmetique (M03). Ajoutez de vrais cas : petites matrices calculées à la main
et/ou comparaison avec une référence (OpenCV / scikit-image / scipy autorisés dans tests/ seulement)."""
import numpy as np  # noqa: F401
import pytest

import timg.ch02_base.arithmetique as m
from tests.conftest import implemente


@implemente(m.et_logique)
def test_et_logique_existe():
    assert callable(m.et_logique)
    # TODO M03: remplacer par un test réel


@implemente(m.ou_logique)
def test_ou_logique_existe():
    assert callable(m.ou_logique)
    # TODO M03: remplacer par un test réel


@implemente(m.xor_logique)
def test_xor_logique_existe():
    assert callable(m.xor_logique)
    # TODO M03: remplacer par un test réel


@implemente(m.non_logique)
def test_non_logique_existe():
    assert callable(m.non_logique)
    # TODO M03: remplacer par un test réel


@implemente(m.addition)
def test_addition_existe():
    assert callable(m.addition)
    # TODO M03: remplacer par un test réel


@implemente(m.soustraction)
def test_soustraction_existe():
    assert callable(m.soustraction)
    # TODO M03: remplacer par un test réel


@implemente(m.difference_absolue)
def test_difference_absolue_existe():
    assert callable(m.difference_absolue)
    # TODO M03: remplacer par un test réel


@implemente(m.multiplication)
def test_multiplication_existe():
    assert callable(m.multiplication)
    # TODO M03: remplacer par un test réel


@implemente(m.combinaison_lineaire)
def test_combinaison_lineaire_existe():
    assert callable(m.combinaison_lineaire)
    # TODO M03: remplacer par un test réel

