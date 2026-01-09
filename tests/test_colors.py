import pytest
from pltx.colors import ColorPalette, get_color, cycle_color, set_default_palette

def test_color_palette_creation():
    palette = ColorPalette("viridis", 5)
    assert len(palette) == 5
    assert len(palette.palette) == 5

def test_get_color():
    palette = ColorPalette("viridis", 3)
    assert palette.get_color(0) == palette.palette[0]
    with pytest.raises(IndexError):
        palette.get_color(3)

def test_cycle_color():
    palette = ColorPalette("viridis", 3)
    assert palette.cycle_color(0) == palette.palette[0]
    assert palette.cycle_color(3) == palette.palette[0]
    assert palette.cycle_color(4) == palette.palette[1]

def test_adjust_intensity():
    color = (0.5, 0.5, 0.5)
    lighter = ColorPalette.adjust_intensity(color, 0.5)
    # lighter = color * intensity + (1 - intensity)
    # 0.5 * 0.5 + (1 - 0.5) = 0.25 + 0.5 = 0.75
    assert lighter == (0.75, 0.75, 0.75)

def test_adjust_alpha():
    color = (1.0, 0.5, 0.0)
    rgba = ColorPalette.adjust_alpha(color, 0.5)
    assert rgba == (1.0, 0.5, 0.0, 0.5)

def test_create_gradient():
    c1 = (0.0, 0.0, 0.0)
    c2 = (1.0, 1.0, 1.0)
    gradient = ColorPalette.create_gradient(c1, c2, 3)
    assert len(gradient) == 3
    assert gradient[0] == (0.0, 0.0, 0.0)
    assert gradient[1] == (0.5, 0.5, 0.5)
    assert gradient[2] == (1.0, 1.0, 1.0)

def test_default_palette_functions():
    set_default_palette("magma", 10)
    c = get_color(0)
    assert isinstance(c, tuple)
    assert len(c) == 3

    c_cycle = cycle_color(11)
    assert c_cycle == get_color(1)
