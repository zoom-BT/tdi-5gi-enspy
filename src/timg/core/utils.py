"""Utilitaires partagés (déjà fournis : ne pas modifier sans PR validée par 2 membres)."""
from __future__ import annotations

import numpy as np


def as_float(img) -> np.ndarray:
    """Copie de l'image en float64 (pour les calculs intermédiaires)."""
    return np.asarray(img, dtype=np.float64)


def to_uint8(img) -> np.ndarray:
    """Arrondit et sature dans [0, 255], retourne un uint8."""
    return np.clip(np.rint(np.asarray(img, dtype=np.float64)), 0, 255).astype(np.uint8)


def normaliser_0_255(img) -> np.ndarray:
    """Etire linéairement une image quelconque vers [0, 255] (utile pour afficher un spectre, un gradient...)."""
    a = as_float(img)
    lo, hi = a.min(), a.max()
    if hi == lo:
        return np.zeros(a.shape, dtype=np.uint8)
    return to_uint8(255.0 * (a - lo) / (hi - lo))


def est_gris(img) -> bool:
    return np.asarray(img).ndim == 2


def est_binaire(img) -> bool:
    return bool(np.isin(np.unique(np.asarray(img)), [0, 1]).all())


def verifier_gris(img) -> np.ndarray:
    a = np.asarray(img)
    if a.ndim != 2:
        raise ValueError(f"image en niveaux de gris (H, W) attendue, reçu {a.shape}")
    return a
