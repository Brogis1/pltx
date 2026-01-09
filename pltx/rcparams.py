"""Default matplotlib rcParams for pltx."""

from typing import Dict, Any, Literal

# Default font sizes
FONT_SIZE_SMALL = 10
FONT_SIZE_MEDIUM = 12
FONT_SIZE_LARGE = 13

# Default figure settings
FIGURE_DPI = 100
FIGURE_FIGSIZE = (6, 4)

# Default line settings
LINE_WIDTH = 2
MARKER_SIZE = 6

# Default color settings
AXES_PROP_CYCLE_PALETTE = "plasma_r"
AXES_PROP_CYCLE_SIZE = 10

# Nature journal style settings
NATURE_FONT_SIZE = 8
NATURE_SMALL_FONT_SIZE = 7
NATURE_LARGE_FONT_SIZE = 9
NATURE_FIGURE_WIDTH = 3.5  # inches (single column)
NATURE_FIGURE_WIDTH_DOUBLE = 7.0  # inches (double column)

StylePreset = Literal["default", "nature", "presentation", "poster"]


def get_default_rcparams(
    font_size_medium: int = FONT_SIZE_MEDIUM,
    font_size_large: int = FONT_SIZE_LARGE,
    use_tex: bool = False,
    **kwargs,
) -> Dict[str, Any]:
    """Get default matplotlib rcParams for pltx.

    Parameters
    ----------
    font_size_medium : int
        Standard font size for labels, ticks
    font_size_large : int
        Font size for titles
    use_tex : bool
        Whether to use LaTeX rendering
    **kwargs
        Additional rcParams to override

    Returns
    -------
    Dict[str, Any]
        Dictionary of rcParams
    """
    params = {
        # Font settings
        "font.size": font_size_medium,
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "axes.titlesize": font_size_large,
        "axes.labelsize": font_size_medium,
        "xtick.labelsize": font_size_medium,
        "ytick.labelsize": font_size_medium,
        "legend.fontsize": font_size_medium,
        "figure.titlesize": font_size_medium,
        "text.usetex": use_tex,
        # Figure settings
        "figure.dpi": FIGURE_DPI,
        "figure.figsize": FIGURE_FIGSIZE,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.format": "pdf",
        # Line settings
        "lines.linewidth": LINE_WIDTH,
        "lines.markersize": MARKER_SIZE,
        # Tick settings
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.major.size": 5,
        "ytick.major.size": 5,
        "xtick.minor.size": 3,
        "ytick.minor.size": 3,
        "xtick.top": True,
        "ytick.right": True,
        # Grid settings
        "grid.alpha": 0.3,
        "grid.linestyle": "--",
        # Legend settings
        "legend.framealpha": 0.8,
        "legend.frameon": True,
        "legend.fancybox": False,
        "legend.edgecolor": "0.8",
        # Axes settings
        "axes.grid": False,
        "axes.axisbelow": True,
        "axes.linewidth": 1.0,
        "axes.edgecolor": "black",
        "axes.labelcolor": "black",
        # Image settings
        "image.cmap": "viridis",
        "image.interpolation": "nearest",
    }

    # Update with any custom parameters
    params.update(kwargs)

    return params


def get_nature_rcparams(**kwargs) -> Dict[str, Any]:
    """Get Nature journal style rcParams.

    Nature journal requirements:
    - Sans-serif fonts (Arial preferred)
    - Font size 7-9 pt
    - Single column width: 89 mm (3.5 inches)
    - Double column width: 183 mm (7.2 inches)
    - Maximum height: 247 mm (9.7 inches)
    - 300+ DPI for final figures

    Parameters
    ----------
    **kwargs
        Additional rcParams to override

    Returns
    -------
    Dict[str, Any]
        Dictionary of rcParams optimized for Nature journal
    """
    params = {
        # Font settings - Nature prefers Arial
        "font.size": NATURE_FONT_SIZE,
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "axes.titlesize": NATURE_LARGE_FONT_SIZE,
        "axes.labelsize": NATURE_FONT_SIZE,
        "xtick.labelsize": NATURE_SMALL_FONT_SIZE,
        "ytick.labelsize": NATURE_SMALL_FONT_SIZE,
        "legend.fontsize": NATURE_SMALL_FONT_SIZE,
        "figure.titlesize": NATURE_LARGE_FONT_SIZE,
        "text.usetex": False,  # Nature prefers native fonts
        # Figure settings - single column width
        "figure.dpi": 150,
        "figure.figsize": (NATURE_FIGURE_WIDTH, NATURE_FIGURE_WIDTH * 0.75),
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.format": "pdf",
        "savefig.transparent": False,
        # Line settings - thinner for smaller figures
        "lines.linewidth": 1.0,
        "lines.markersize": 4,
        # Tick settings
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.major.size": 3,
        "ytick.major.size": 3,
        "xtick.minor.size": 2,
        "ytick.minor.size": 2,
        "xtick.major.width": 0.5,
        "ytick.major.width": 0.5,
        "xtick.top": True,
        "ytick.right": True,
        # Grid settings
        "grid.alpha": 0.3,
        "grid.linestyle": "--",
        "grid.linewidth": 0.5,
        # Legend settings
        "legend.framealpha": 1.0,
        "legend.frameon": True,
        "legend.fancybox": False,
        "legend.edgecolor": "black",
        "legend.borderpad": 0.4,
        "legend.labelspacing": 0.3,
        # Axes settings
        "axes.grid": False,
        "axes.axisbelow": True,
        "axes.linewidth": 0.5,
        "axes.edgecolor": "black",
        "axes.labelcolor": "black",
        "axes.labelpad": 2.0,
        # Image settings
        "image.cmap": "viridis",
        "image.interpolation": "nearest",
    }

    # Update with any custom parameters
    params.update(kwargs)

    return params


def get_presentation_rcparams(**kwargs) -> Dict[str, Any]:
    """Get presentation style rcParams (large fonts, thick lines).

    Parameters
    ----------
    **kwargs
        Additional rcParams to override

    Returns
    -------
    Dict[str, Any]
        Dictionary of rcParams optimized for presentations
    """
    params = get_default_rcparams(
        font_size_medium=16,
        font_size_large=18,
        **{
            "figure.figsize": (10, 6),
            "lines.linewidth": 3,
            "lines.markersize": 8,
            "axes.linewidth": 1.5,
            "xtick.major.size": 8,
            "ytick.major.size": 8,
            "xtick.minor.size": 4,
            "ytick.minor.size": 4,
            "legend.fontsize": 14,
        }
    )
    params.update(kwargs)
    return params


def get_poster_rcparams(**kwargs) -> Dict[str, Any]:
    """Get poster style rcParams (very large fonts and lines).

    Parameters
    ----------
    **kwargs
        Additional rcParams to override

    Returns
    -------
    Dict[str, Any]
        Dictionary of rcParams optimized for posters
    """
    params = get_default_rcparams(
        font_size_medium=24,
        font_size_large=28,
        **{
            "figure.figsize": (12, 8),
            "lines.linewidth": 4,
            "lines.markersize": 12,
            "axes.linewidth": 2.0,
            "xtick.major.size": 10,
            "ytick.major.size": 10,
            "xtick.minor.size": 6,
            "ytick.minor.size": 6,
            "legend.fontsize": 20,
        }
    )
    params.update(kwargs)
    return params


def apply_rcparams(
    font_size_medium: int = FONT_SIZE_MEDIUM,
    font_size_large: int = FONT_SIZE_LARGE,
    use_tex: bool = False,
    **kwargs,
) -> None:
    """Apply default rcParams to matplotlib.

    Parameters
    ----------
    font_size_medium : int
        Standard font size for labels, ticks
    font_size_large : int
        Font size for titles
    use_tex : bool
        Whether to use LaTeX rendering
    **kwargs
        Additional rcParams to override
    """
    import matplotlib.pyplot as plt

    params = get_default_rcparams(
        font_size_medium=font_size_medium,
        font_size_large=font_size_large,
        use_tex=use_tex,
        **kwargs,
    )

    for key, value in params.items():
        plt.rcParams[key] = value


def apply_style_preset(preset: StylePreset = "default", **kwargs) -> None:
    """Apply a predefined style preset.

    Parameters
    ----------
    preset : {'default', 'nature', 'presentation', 'poster'}
        Style preset to apply
    **kwargs
        Additional rcParams to override

    Examples
    --------
    >>> apply_style_preset('nature')
    >>> apply_style_preset('presentation', font_size_medium=18)
    """
    import matplotlib.pyplot as plt

    if preset == "default":
        params = get_default_rcparams(**kwargs)
    elif preset == "nature":
        params = get_nature_rcparams(**kwargs)
    elif preset == "presentation":
        params = get_presentation_rcparams(**kwargs)
    elif preset == "poster":
        params = get_poster_rcparams(**kwargs)
    else:
        raise ValueError(
            f"Unknown preset '{preset}'. "
            f"Choose from: 'default', 'nature', 'presentation', 'poster'"
        )

    for key, value in params.items():
        plt.rcParams[key] = value
