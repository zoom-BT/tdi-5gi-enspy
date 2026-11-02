"""Ch4 - filtres_frequentiels

Responsable : M08 (Membre 8)
Branche     : m08/ch04-filtres_frequentiels
Règle       : numpy uniquement (pas d'OpenCV / scikit-image / scipy dans src/).
"""
from __future__ import annotations

import numpy as np  # noqa: F401

from timg.core.utils import as_float, to_uint8  # noqa: F401


def masque_passe_bas_ideal(forme, rayon):
    """Masque circulaire (1 dans le cercle)."""
    raise NotImplementedError("M08: masque_passe_bas_ideal")


def masque_passe_haut_ideal(forme, rayon):
    """Complément du passe-bas."""
    raise NotImplementedError("M08: masque_passe_haut_ideal")


def masque_gaussien(forme, sigma, passe_haut=False):
    """Masque gaussien (bonus : Butterworth)."""
    raise NotImplementedError("M08: masque_gaussien")


def filtrer_frequentiel(img, masque):
    """FFT -> multiplication -> FFT inverse (utilise ch04_fourier.fft)."""
    raise NotImplementedError("M08: filtrer_frequentiel")


def energie_par_rayon(img, pourcentages=(0.9,0.95,0.98,0.99,0.995,0.999)):
    """Rayons contenant x % de l'énergie du spectre."""
    raise NotImplementedError("M08: energie_par_rayon")


def filtre_notch(img, centres, rayon):
    """Supprime des pics de bruit périodique (et leurs symétriques)."""
    raise NotImplementedError("M08: filtre_notch")


def rehaussement_frequentiel(img, rayon, k=1.0):
    """Image + k * passe-haut, puis option égalisation."""
    raise NotImplementedError("M08: rehaussement_frequentiel")

