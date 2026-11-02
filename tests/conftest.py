"""Outils de test partagés."""
import inspect

import numpy as np
import pytest


def implemente(func):
    """Décorateur : saute le test tant que `func` lève NotImplementedError (stub non codé)."""
    def deco(test):
        try:
            src = inspect.getsource(func)
        except (OSError, TypeError):
            src = ""
        stub = "raise NotImplementedError" in src
        return pytest.mark.skipif(stub, reason=f"{func.__name__} pas encore implémentée")(test)
    return deco


@pytest.fixture
def damier():
    """Image 8x8 uint8 en damier 0/255."""
    return (np.indices((8, 8)).sum(axis=0) % 2 * 255).astype(np.uint8)


@pytest.fixture
def rampe():
    """Image 16x16 dégradé horizontal 0..240."""
    return np.tile(np.arange(16, dtype=np.uint8) * 16, (16, 1))


@pytest.fixture
def carre_binaire():
    """Image binaire 10x10 avec un carré 4x4 au centre."""
    b = np.zeros((10, 10), dtype=np.uint8)
    b[3:7, 3:7] = 1
    return b
