import numpy as np

from timg.core.utils import normaliser_0_255, to_uint8


def test_to_uint8_sature():
    assert to_uint8([-5, 12.6, 300]).tolist() == [0, 13, 255]


def test_normaliser():
    out = normaliser_0_255(np.array([[2.0, 4.0], [6.0, 10.0]]))
    assert out.min() == 0 and out.max() == 255
