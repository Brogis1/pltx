"""pltx - Enhanced Matplotlib for Scientific Visualization."""

from typing import Optional, Tuple
from .cmap import register_pasqal_cmap as _register_pasqal_cmap
from .rcparams import (
    apply_style_preset,
    StylePreset,
    AXES_PROP_CYCLE_PALETTE,
    AXES_PROP_CYCLE_SIZE,
    _palette_to_cycler,
)

__version__ = "0.1.3"

# Auto-register pasqal colormaps on import
_register_pasqal_cmap()
del _register_pasqal_cmap


def use(
    palette: str = AXES_PROP_CYCLE_PALETTE,
    n_colors: int = AXES_PROP_CYCLE_SIZE,
    style: StylePreset = "default",
    minor_ticks: bool = False,
    tight_spines: bool = False,
    figsize: Optional[Tuple[float, float]] = None,
    dpi: Optional[int] = None,
    **rcparams,
) -> None:
    """Apply pltx style globally so plain plt.plot() looks great.

    Call once at the top of your script or notebook. After this, all
    matplotlib figures automatically use the chosen color cycle and
    styling — no need to touch PlotStyle or setup_axis.

    Parameters
    ----------
    palette : str
        Color palette for the automatic color cycle.
        Any matplotlib colormap or seaborn palette name works,
        e.g. ``'plasma_r'``, ``'tab10'``, ``'pasqal'``, ``'viridis'``.
    n_colors : int
        Number of colors to sample from the palette.
    style : {'default', 'nature', 'latex', 'presentation', 'poster'}
        Base style preset (sets fonts, line widths, etc.).
    minor_ticks : bool
        If True, enable minor ticks on both axes globally.
    tight_spines : bool
        If True, use thinner axis borders (linewidth 0.8).
    figsize : tuple of float, optional
        Default figure size as (width, height) in inches.
    dpi : int, optional
        Default figure DPI.
    **rcparams
        Any additional matplotlib rcParams to override, e.g.
        ``lines.linewidth=1.5``.

    Examples
    --------
    Minimal — just fix the color cycle:

    >>> import pltx
    >>> pltx.use()

    Physics-paper style:

    >>> pltx.use(
    ...     palette='plasma_r',
    ...     style='nature',
    ...     minor_ticks=True,
    ...     tight_spines=True,
    ... )

    Custom palette:

    >>> pltx.use(palette='tab10', n_colors=10)
    """
    import matplotlib.pyplot as plt

    # 1. Apply base style preset (fonts, tick direction, etc.)
    apply_style_preset(style)

    # 2. Override color cycle with chosen palette
    plt.rcParams["axes.prop_cycle"] = _palette_to_cycler(palette, n_colors)

    # 3. Optional enhancements
    if minor_ticks:
        plt.rcParams["xtick.minor.visible"] = True
        plt.rcParams["ytick.minor.visible"] = True

    if tight_spines:
        plt.rcParams["axes.linewidth"] = 0.8

    if figsize is not None:
        plt.rcParams["figure.figsize"] = list(figsize)

    if dpi is not None:
        plt.rcParams["figure.dpi"] = dpi

    # 4. Any extra overrides
    for key, value in rcparams.items():
        plt.rcParams[key] = value
