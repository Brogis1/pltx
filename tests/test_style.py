import pytest
import matplotlib.pyplot as plt
from pltx.style import PlotStyle
import numpy as np

def test_plot_style_initialization():
    style = PlotStyle(palette_name="viridis", palette_size=5)
    assert style.palette_name == "viridis"
    assert style.palette_size == 5
    assert len(style.palette) == 5

def test_get_linewidth():
    # Test without varying linewidth
    style = PlotStyle(vary_linewidth=False, base_linewidth=2.0)
    assert style.get_linewidth(0) == 2.0
    assert style.get_linewidth(5) == 2.0

    # Test with varying linewidth
    style = PlotStyle(vary_linewidth=True, base_linewidth=2.0, linewidth_progression_factor=1.3)
    assert style.get_linewidth(0) == 2.0
    assert pytest.approx(style.get_linewidth(1)) == 2.6
    assert pytest.approx(style.get_linewidth(2)) == 3.38

def test_setup_axis():
    style = PlotStyle()
    fig, ax = plt.subplots()
    style.setup_axis(ax, xlabel="Test X", ylabel="Test Y", title="Test Title", grid=True)

    assert ax.get_xlabel() == "Test X"
    assert ax.get_ylabel() == "Test Y"
    assert ax.get_title() == "Test Title"
    # Check if grid is on
    assert any(line.get_visible() for line in ax.xaxis.get_gridlines()) == True
    plt.close(fig)

def test_color_cycling():
    style = PlotStyle(palette_size=3)
    c0 = style.cycle_color(0)
    c1 = style.cycle_color(1)
    c2 = style.cycle_color(2)
    c3 = style.cycle_color(3) # Should wrap

    assert c0 != c1
    assert c3 == c0

    style.reset_color_cycle()
    assert style._color_cycle_idx == 0

def test_add_reference_line():
    style = PlotStyle()
    fig, ax = plt.subplots()
    style.add_reference_line(ax, horizontal=1.0, vertical=[2.0, 3.0])

    # axhline and axvline add lines to the axis
    assert len(ax.get_lines()) == 3
    plt.close(fig)

def test_add_highlight_region():
    style = PlotStyle()
    fig, ax = plt.subplots()
    style.add_highlight_region(ax, ymin=0, ymax=1)
    # axhspan adds a Polygon to ax.patches
    assert len(ax.patches) == 1
    plt.close(fig)
