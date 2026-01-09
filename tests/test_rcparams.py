import pytest
import matplotlib.pyplot as plt
from pltx.rcparams import (
    get_default_rcparams,
    get_nature_rcparams,
    get_presentation_rcparams,
    get_poster_rcparams,
    apply_style_preset
)

def test_get_default_rcparams():
    params = get_default_rcparams(font_size_medium=15)
    assert params["font.size"] == 15
    assert params["lines.linewidth"] == 2

def test_get_nature_rcparams():
    params = get_nature_rcparams()
    assert params["font.size"] == 8
    assert params["figure.figsize"][0] == 3.5
    assert params["lines.linewidth"] == 1.0

def test_get_presentation_rcparams():
    params = get_presentation_rcparams()
    assert params["font.size"] == 16
    assert params["lines.linewidth"] == 3

def test_get_poster_rcparams():
    params = get_poster_rcparams()
    assert params["font.size"] == 24
    assert params["lines.linewidth"] == 4

def test_apply_style_preset():
    apply_style_preset("nature")
    assert plt.rcParams["font.size"] == 8

    apply_style_preset("presentation")
    assert plt.rcParams["font.size"] == 16

    with pytest.raises(ValueError):
        apply_style_preset("non_existent_preset")

def test_apply_style_preset_overrides():
    apply_style_preset("nature", **{"font.size": 12})
    assert plt.rcParams["font.size"] == 12
