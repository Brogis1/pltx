import pytest
import numpy as np
import matplotlib.pyplot as plt
import pltx.pyplot as pltx_plt

def test_initialize_style():
    style = pltx_plt.initialize_style(palette_name="magma", vary_linewidth=True)
    assert pltx_plt._style_initialized == True
    assert pltx_plt._default_style.palette_name == "magma"
    assert pltx_plt._default_style.vary_linewidth == True

def test_plot_styled():
    pltx_plt.initialize_style()
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    line = pltx_plt.plot_styled(x, y, label="Test Line", outline=True)

    assert line.get_label() == "Test Line"
    # Check if we have two lines (one for main, one for outline)
    ax = plt.gca()
    assert len(ax.get_lines()) == 2
    plt.close('all')

def test_scatter_styled():
    pltx_plt.initialize_style()
    x = np.random.rand(10)
    y = np.random.rand(10)

    sc = pltx_plt.scatter_styled(x, y, label="Test Scatter")
    assert sc.get_label() == "Test Scatter"
    plt.close('all')

def test_bar_styled():
    pltx_plt.initialize_style()
    x = ['A', 'B', 'C']
    height = [1, 2, 3]

    bars = pltx_plt.bar_styled(x, height, label="Test Bar")
    assert len(bars) == 3
    plt.close('all')

def test_hist_styled():
    pltx_plt.initialize_style()
    data = np.random.randn(100)

    n, bins, patches = pltx_plt.hist_styled(data, bins=10, label="Test Hist")
    assert len(patches) == 10
    plt.close('all')

def test_setup_axis_wrapper():
    pltx_plt.initialize_style()
    pltx_plt.setup_axis(xlabel="X", ylabel="Y")
    ax = plt.gca()
    assert ax.get_xlabel() == "X"
    assert ax.get_ylabel() == "Y"
    plt.close('all')

def test_style_context():
    pltx_plt.initialize_style(font_size_medium=12)
    with pltx_plt.style_context('nature'):
        # Just check if it runs without error for now
        # Ideally check rcParams change
        pass
    # Should be back to 12? depends on how apply_style_preset works
    # If nature uses 8, then it should be 8 inside and 12 outside.
    pass
