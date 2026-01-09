"""pltx - A matplotlib wrapper with custom styling and color palettes.

This package provides a drop-in replacement for matplotlib with automatic
styling, custom color palettes, and enhanced convenience functions for
creating publication-quality scientific visualizations.

Usage
-----
Basic usage (drop-in replacement for matplotlib.pyplot):
    import pltx.pyplot as plt

    plt.plot([1, 2, 3], [1, 4, 9])
    plt.show()

With enhanced styling:
    import pltx.pyplot as plt

    # Initialize with custom style
    plt.initialize_style(palette_name='viridis', use_tex=True)

    # Use enhanced plotting functions
    plt.plot_styled([1, 2, 3], [1, 4, 9], color_idx=0, label='Data')
    plt.add_reference_line(horizontal=5, label='Threshold')
    plt.setup_axis(xlabel='x', ylabel='y', grid=True)
    plt.show()

Direct style access:
    from pltx import PlotStyle
    import matplotlib.pyplot as plt

    style = PlotStyle(palette_name='plasma_r')
    fig, ax = plt.subplots()
    style.plot_curve(ax, [1, 2, 3], [1, 4, 9], color_idx=0)
    style.setup_axis(ax, xlabel='x', ylabel='y')
    plt.show()

Color utilities:
    from pltx.colors import get_color, cycle_color, ColorPalette

    # Get specific color
    color = get_color(0)  # First color from default palette

    # Cycle through colors automatically
    for i in range(20):
        c = cycle_color(i)  # Wraps around palette size

    # Custom palette
    palette = ColorPalette('viridis', 8)
    color = palette.get_color(3)
"""

__version__ = "0.1.0"
__author__ = "Igor Sokolov"

# Import main components
from .style import PlotStyle
from .colors import ColorPalette, get_color, cycle_color, set_default_palette
from .rcparams import apply_rcparams, get_default_rcparams

# Import pyplot interface (can be imported as: from pltx import pyplot)
from . import pyplot

__all__ = [
    # Main classes
    "PlotStyle",
    "ColorPalette",
    # Color utilities
    "get_color",
    "cycle_color",
    "set_default_palette",
    # RC params
    "apply_rcparams",
    "get_default_rcparams",
    # Pyplot module
    "pyplot",
]
