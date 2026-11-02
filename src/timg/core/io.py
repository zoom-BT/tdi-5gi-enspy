"""Ch1 - Entrées/sorties d'images.

Responsable : M01 (Membre 1)
Branche     : m01/core-io
PGM/PPM : à coder à la main (formats P2/P5 et P3/P6, cf. cours ch.1).
Pillow est toléré UNIQUEMENT dans lire_image/ecrire_image pour PNG/JPG.
"""
from __future__ import annotations

import numpy as np  # noqa: F401


def lire_pgm(chemin):
    """Lit un PGM (P2 ASCII ou P5 binaire) -> ndarray uint8 (H, W)."""
    raise NotImplementedError("M01: lire_pgm")


def ecrire_pgm(chemin, img, binaire=True):
    """Ecrit un PGM (P5 si binaire=True, sinon P2)."""
    raise NotImplementedError("M01: ecrire_pgm")


def lire_ppm(chemin):
    """Lit un PPM (P3 / P6) -> ndarray uint8 (H, W, 3)."""
    raise NotImplementedError("M01: lire_ppm")


def ecrire_ppm(chemin, img, binaire=True):
    """Ecrit un PPM (P6 si binaire=True, sinon P3)."""
    raise NotImplementedError("M01: ecrire_ppm")


def lire_image(chemin, gris=False):
    """Lit PGM/PPM (fonctions ci-dessus) ou PNG/JPG (Pillow)."""
    raise NotImplementedError("M01: lire_image")


def ecrire_image(chemin, img):
    """Ecrit selon l'extension."""
    raise NotImplementedError("M01: ecrire_image")
