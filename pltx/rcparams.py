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

# LaTeX document style settings
LATEX_FONT_SIZE = 10
LATEX_SMALL_FONT_SIZE = 9
LATEX_LARGE_FONT_SIZE = 11
LATEX_FIGURE_WIDTH = 5.5  # inches (standard \textwidth for article class)

StylePreset = Literal["default", "nature", "latex", "presentation", "poster"]


def _palette_to_cycler(palette_name: str, n: int = 10):
    """Return a matplotlib cycler built from a named palette.

    Works with seaborn palettes, matplotlib colormaps, and custom
    colormaps registered via pltx (e.g. 'pasqal').

    Parameters
    ----------
    palette_name : str
        Name of the palette / colormap.
    n : int
        Number of colors to sample.

    Returns
    -------
    cycler.Cycler
        A color cycler ready for use as ``axes.prop_cycle``.
    """
    from cycler import cycler
    import matplotlib.pyplot as plt

    try:
        import seaborn as sns
        colors = sns.color_palette(palette_name, n)
        # Convert to hex strings for clean rcParams storage
        hex_colors = [
            "#{:02x}{:02x}{:02x}".format(
                int(r * 255), int(g * 255), int(b * 255)
            )
            for r, g, b in colors
        ]
    except Exception:
        # Fall back to sampling a matplotlib colormap
        try:
            cmap = plt.get_cmap(palette_name)
        except (ValueError, KeyError):
            cmap = plt.get_cmap("viridis")
        hex_colors = []
        for i in range(n):
            r, g, b, _ = cmap(i / max(n - 1, 1))
            hex_colors.append(
                "#{:02x}{:02x}{:02x}".format(
                    int(r * 255), int(g * 255), int(b * 255)
                )
            )

    return cycler("color", hex_colors)


def get_default_rcparams(
    font_size_medium: int = FONT_SIZE_MEDIUM,
    font_size_large: int = FONT_SIZE_LARGE,
    use_tex: bool = False,
    palette: str = AXES_PROP_CYCLE_PALETTE,
    n_colors: int = AXES_PROP_CYCLE_SIZE,
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
    palette : str
        Color palette / colormap name for ``axes.prop_cycle``
    n_colors : int
        Number of colors to sample from the palette
    **kwargs
        Additional rcParams to override

    Returns
    -------
    Dict[str, Any]
        Dictionary of rcParams
    """
    params = {
        # Color cycle
        "axes.prop_cycle": _palette_to_cycler(palette, n_colors),
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


def get_latex_rcparams(**kwargs) -> Dict[str, Any]:
    """Get LaTeX document style rcParams.

    Designed for figures embedded in LaTeX documents (articles, theses,
    reports). Uses Computer Modern fonts via ``text.usetex = True`` so
    figure text matches the surrounding LaTeX document.

    Requirements:
    - A working LaTeX installation (pdflatex + cm-super or lmodern)
    - Font size 9-11 pt to match typical ``\\normalsize`` in article class
    - Standard textwidth ~5.5 inches (single column article class)

    Parameters
    ----------
    **kwargs
        Additional rcParams to override

    Returns
    -------
    Dict[str, Any]
        Dictionary of rcParams optimized for LaTeX documents
    """
    params = {
        # Font settings - Computer Modern via LaTeX
        "font.size": LATEX_FONT_SIZE,
        "font.family": "serif",
        "font.serif": ["Computer Modern Roman", "cmr10", "DejaVu Serif"],
        "axes.titlesize": LATEX_LARGE_FONT_SIZE,
        "axes.labelsize": LATEX_FONT_SIZE,
        "xtick.labelsize": LATEX_SMALL_FONT_SIZE,
        "ytick.labelsize": LATEX_SMALL_FONT_SIZE,
        "legend.fontsize": LATEX_SMALL_FONT_SIZE,
        "figure.titlesize": LATEX_LARGE_FONT_SIZE,
        "text.usetex": True,
        "text.latex.preamble": r"\usepackage{amsmath}\usepackage{amssymb}",
        "axes.formatter.use_mathtext": True,
        # Figure settings - standard article class textwidth
        "figure.dpi": 150,
        "figure.figsize": (LATEX_FIGURE_WIDTH, LATEX_FIGURE_WIDTH * 0.618),
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.format": "pdf",
        "savefig.transparent": False,
        # Line settings
        "lines.linewidth": 1.5,
        "lines.markersize": 5,
        # Tick settings
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.major.size": 4,
        "ytick.major.size": 4,
        "xtick.minor.size": 2.5,
        "ytick.minor.size": 2.5,
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,
        "xtick.minor.width": 0.4,
        "ytick.minor.width": 0.4,
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
        "axes.linewidth": 0.6,
        "axes.edgecolor": "black",
        "axes.labelcolor": "black",
        "axes.labelpad": 3.0,
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
    palette: str = AXES_PROP_CYCLE_PALETTE,
    n_colors: int = AXES_PROP_CYCLE_SIZE,
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
    palette : str
        Color palette / colormap name for ``axes.prop_cycle``
    n_colors : int
        Number of colors to sample from the palette
    **kwargs
        Additional rcParams to override
    """
    import matplotlib.pyplot as plt

    params = get_default_rcparams(
        font_size_medium=font_size_medium,
        font_size_large=font_size_large,
        use_tex=use_tex,
        palette=palette,
        n_colors=n_colors,
        **kwargs,
    )

    for key, value in params.items():
        plt.rcParams[key] = value


def apply_style_preset(preset: StylePreset = "default", **kwargs) -> None:
    """Apply a predefined style preset.

    Parameters
    ----------
    preset : {'default', 'nature', 'latex', 'presentation', 'poster'}
        Style preset to apply
    **kwargs
        Additional rcParams to override

    Examples
    --------
    >>> apply_style_preset('nature')
    >>> apply_style_preset('latex')
    >>> apply_style_preset('presentation', font_size_medium=18)
    """
    import matplotlib.pyplot as plt

    if preset == "default":
        params = get_default_rcparams(**kwargs)
    elif preset == "nature":
        params = get_nature_rcparams(**kwargs)
    elif preset == "latex":
        params = get_latex_rcparams(**kwargs)
    elif preset == "presentation":
        params = get_presentation_rcparams(**kwargs)
    elif preset == "poster":
        params = get_poster_rcparams(**kwargs)
    else:
        raise ValueError(
            f"Unknown preset '{preset}'. "
            "Choose from: 'default', 'nature', 'latex', "
            "'presentation', 'poster'"
        )

    for key, value in params.items():
        plt.rcParams[key] = value
