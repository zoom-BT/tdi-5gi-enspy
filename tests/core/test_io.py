import numpy as np

import timg.core.io as m
from tests.conftest import implemente


@implemente(m.ecrire_pgm)
def test_aller_retour_pgm(tmp_path, damier):
    p = tmp_path / "x.pgm"
    m.ecrire_pgm(p, damier)
    assert np.array_equal(m.lire_pgm(p), damier)
