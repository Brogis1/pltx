"""Enhanced pyplot interface for pltx.

This module provides a drop-in replacement for matplotlib.pyplot with
automatic styling and enhanced convenience functions.
"""

from typing import Optional, Tuple, List, Union
import numpy as np
from matplotlib.pyplot import *  # noqa: F403
from matplotlib.pyplot import gca  # noqa: F401

from .style import PlotStyle
from .rcparams import StylePreset, apply_style_preset

# Initialize default style
_default_style: Optional[PlotStyle] = None
_style_initialized = False


def initialize_style(
    palette_name: str = "plasma_r",
    palette_size: int = 10,
    font_size_medium: int = 12,
    font_size_large: int = 13,
    use_tex: bool = False,
    vary_linewidth: bool = False,
    base_linewidth: float = 2.0,
    linewidth_progression_factor: float = 1.3,
) -> PlotStyle:
    """Initialize the default plotting style for pltx.

    This function should be called once at the beginning of your script
    to set up the global plotting style.

    Parameters
    ----------
    palette_name : str
        Name of the seaborn color palette
    palette_size : int
        Number of colors in the palette
    font_size_medium : int
        Standard font size for labels, ticks
    font_size_large : int
        Font size for titles
    use_tex : bool
        Whether to use LaTeX rendering
    vary_linewidth : bool
        If True, automatically vary line widths for colorblind accessibility.
        Each line gets progressively thicker.
    base_linewidth : float
        Base line width when vary_linewidth is True
    linewidth_progression_factor : float
        Factor for progressive width increase (e.g., 1.2 = 20% increase per line)

    Returns
    -------
    PlotStyle
        The initialized plot style object
    """
    global _default_style, _style_initialized

    _default_style = PlotStyle(
        palette_name=palette_name,
        palette_size=palette_size,
        font_size_medium=font_size_medium,
        font_size_large=font_size_large,
        use_tex=use_tex,
        vary_linewidth=vary_linewidth,
        base_linewidth=base_linewidth,
        linewidth_progression_factor=linewidth_progression_factor,
        auto_apply=True,
    )
    _style_initialized = True

    return _default_style


def get_style() -> PlotStyle:
    """Get the current default plotting style.

    If no style has been initialized, creates one with default settings.

    Returns
    -------
    PlotStyle
        The current plot style object
    """
    global _default_style, _style_initialized

    if not _style_initialized or _default_style is None:
        _default_style = initialize_style()

    return _default_style


def style_context(preset: StylePreset, **kwargs):
    """Context manager for temporary style application.

    Parameters
    ----------
    preset : str
        Style preset name ('nature', 'presentation', 'poster', etc.)
    **kwargs
        Optional rcParams overrides
    """
    return get_style().style_context(preset, **kwargs)


def reset_color_cycle() -> None:
    """Reset the automatic color cycling index to zero."""
    get_style().reset_color_cycle()


def setup_axis(
    ax=None,
    xlim: Optional[Tuple[float, float]] = None,
    ylim: Optional[Tuple[float, float]] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    title: Optional[str] = None,
    xscale: str = "linear",
    yscale: str = "linear",
    xtick_spacing: Optional[float] = None,
    ytick_spacing: Optional[float] = None,
    grid: bool = False,
    grid_alpha: float = 0.3,
):
    """Setup axis with consistent styling.

    Parameters
    ----------
    ax : Axes, optional
        Axis to setup. If None, uses current axis.
    xlim, ylim : tuple, optional
        Axis limits
    xlabel, ylabel, title : str, optional
        Axis labels and title
    xscale, yscale : str
        Axis scales ('linear', 'log', etc.)
    xtick_spacing, ytick_spacing : float, optional
        Tick spacing
    grid : bool
        Whether to show grid
    grid_alpha : float
        Grid transparency
    """
    if ax is None:
        ax = gca()

    style = get_style()
    style.setup_axis(
        ax=ax,
        xlim=xlim,
        ylim=ylim,
        xlabel=xlabel,
        ylabel=ylabel,
        title=title,
        xscale=xscale,
        yscale=yscale,
        xtick_spacing=xtick_spacing,
        ytick_spacing=ytick_spacing,
        grid=grid,
        grid_alpha=grid_alpha,
    )


def plot_styled(
    x: np.ndarray,
    y: np.ndarray,
    label: Optional[str] = None,
    color: Optional[Union[str, tuple]] = None,
    color_idx: Optional[int] = None,
    color_intensity: Optional[float] = None,
    linestyle: str = "-",
    linewidth: float = 2,
    marker: Optional[str] = None,
    markersize: Optional[float] = None,
    alpha: Optional[float] = None,
    outline: bool = False,
    outline_color: str = "black",
    outline_width: Optional[float] = None,
    ax=None,
    **kwargs,
):
    """Plot with automatic color cycling and styling.

    This is an enhanced version of plt.plot that uses pltx color palettes
    and styling by default.

    Parameters
    ----------
    x, y : array-like
        Data to plot
    label : str, optional
        Label for legend
    color : str or tuple, optional
        Line color
    color_idx : int, optional
        Index into color palette
    color_intensity : float, optional
        Color intensity adjustment (0.0-1.0)
    linestyle, linewidth, marker, markersize :
        Line and marker style parameters
    alpha : float, optional
        Transparency
    outline : bool
        If True, adds a thin black outline for better visibility
    outline_color : str
        Color of the outline (default: 'black')
    outline_width : float, optional
        Width of the outline. If None, uses linewidth + 2
    ax : Axes, optional
        Axis to plot on. If None, uses current axis.
    **kwargs
        Additional arguments passed to plot

    Returns
    -------
    Line2D
        The plotted line object
    """
    if ax is None:
        ax = gca()

    style = get_style()
    return style.plot_curve(
        ax=ax,
        x=x,
        y=y,
        label=label,
        color=color,
        color_idx=color_idx,
        color_intensity=color_intensity,
        linestyle=linestyle,
        linewidth=linewidth,
        marker=marker,
        markersize=markersize,
        alpha=alpha,
        outline=outline,
        outline_color=outline_color,
        outline_width=outline_width,
        **kwargs,
    )


def scatter_styled(
    x: np.ndarray,
    y: np.ndarray,
    label: Optional[str] = None,
    color: Optional[Union[str, tuple]] = None,
    color_idx: Optional[int] = None,
    size: float = 20,
    marker: str = "o",
    alpha: Optional[float] = None,
    ax=None,
    **kwargs,
):
    """Scatter plot with automatic color cycling and styling.

    Parameters
    ----------
    x, y : array-like
        Data to plot
    label : str, optional
        Label for legend
    color : str or tuple, optional
        Point color
    color_idx : int, optional
        Index into color palette
    size : float
        Marker size
    marker : str
        Marker style
    alpha : float, optional
        Transparency
    ax : Axes, optional
        Axis to plot on. If None, uses current axis.
    **kwargs
        Additional arguments passed to scatter
    """
    if ax is None:
        ax = gca()

    style = get_style()
    return style.scatter_styled(
        ax=ax,
        x=x,
        y=y,
        label=label,
        color=color,
        color_idx=color_idx,
        size=size,
        marker=marker,
        alpha=alpha,
        **kwargs,
    )


def errorbar_styled(
    x: np.ndarray,
    y: np.ndarray,
    yerr: Optional[np.ndarray] = None,
    xerr: Optional[np.ndarray] = None,
    label: Optional[str] = None,
    color: Optional[Union[str, tuple]] = None,
    color_idx: Optional[int] = None,
    linewidth: float = 2,
    capsize: float = 3,
    fmt: str = "o",
    ax=None,
    **kwargs,
):
    """Plot error bars with automatic color cycling and styling.

    Parameters
    ----------
    x, y : array-like
        Data points
    yerr, xerr : array-like, optional
        Error values
    label : str, optional
        Label for legend
    color : str or tuple, optional
        Plot color
    color_idx : int, optional
        Index into color palette
    linewidth : float
        Line width
    capsize : float
        Cap size for error bars
    fmt : str
        Format string for markers/lines
    ax : Axes, optional
        Axis to plot on. If None, uses current axis.
    **kwargs
        Additional arguments passed to errorbar
    """
    if ax is None:
        ax = gca()

    style = get_style()
    return style.errorbar_styled(
        ax=ax,
        x=x,
        y=y,
        yerr=yerr,
        xerr=xerr,
        label=label,
        color=color,
        color_idx=color_idx,
        linewidth=linewidth,
        capsize=capsize,
        fmt=fmt,
        **kwargs,
    )


def bar_styled(
    x: Union[List, np.ndarray],
    height: Union[List, np.ndarray],
    label: Optional[str] = None,
    color: Optional[Union[str, tuple]] = None,
    color_idx: Optional[int] = None,
    edgecolor: str = "black",
    linewidth: float = 1,
    ax=None,
    **kwargs,
):
    """Plot bar chart with automatic color cycling and styling.

    Parameters
    ----------
    x : array-like
        x-coordinates of the bars
    height : array-like
        Heights of the bars
    label : str, optional
        Label for the legend
    color : str or tuple, optional
        Bar color
    color_idx : int, optional
        Index into the palette
    edgecolor : str
        Color of bar edges
    linewidth : float
        Width of bar edges
    ax : Axes, optional
        Axis to plot on. If None, uses current axis.
    **kwargs
        Additional arguments passed to bar
    """
    if ax is None:
        ax = gca()

    style = get_style()
    return style.bar_styled(
        ax=ax,
        x=x,
        height=height,
        label=label,
        color=color,
        color_idx=color_idx,
        edgecolor=edgecolor,
        linewidth=linewidth,
        **kwargs,
    )


def hist_styled(
    x: np.ndarray,
    bins: Optional[Union[int, np.ndarray]] = None,
    label: Optional[str] = None,
    color: Optional[Union[str, tuple]] = None,
    color_idx: Optional[int] = None,
    edgecolor: str = "white",
    alpha: float = 0.8,
    ax=None,
    **kwargs,
):
    """Plot histogram with automatic color cycling and styling.

    Parameters
    ----------
    x : array-like
        Data to histogram
    bins : int or array-like, optional
        Number of bins or bin edges
    label : str, optional
        Label for the legend
    color : str or tuple, optional
        Histogram color
    color_idx : int, optional
        Index into the palette
    edgecolor : str
        Color of bin edges
    alpha : float
        Transparency
    ax : Axes, optional
        Axis to plot on. If None, uses current axis.
    **kwargs
        Additional arguments passed to hist
    """
    if ax is None:
        ax = gca()

    style = get_style()
    return style.hist_styled(
        ax=ax,
        x=x,
        bins=bins,
        label=label,
        color=color,
        color_idx=color_idx,
        edgecolor=edgecolor,
        alpha=alpha,
        **kwargs,
    )


def add_reference_line(
    horizontal: Optional[Union[float, List[float]]] = None,
    vertical: Optional[Union[float, List[float]]] = None,
    color: str = "k",
    linestyle: str = "--",
    linewidth: float = 0.5,
    alpha: float = 0.3,
    label: Optional[str] = None,
    ax=None,
):
    """Add reference lines to current axis.

    Parameters
    ----------
    horizontal : float or list, optional
        y-values for horizontal lines
    vertical : float or list, optional
        x-values for vertical lines
    color, linestyle, linewidth, alpha :
        Line style parameters
    label : str, optional
        Label for legend
    ax : Axes, optional
        Axis to add lines to. If None, uses current axis.
    """
    if ax is None:
        ax = gca()

    style = get_style()
    style.add_reference_line(
        ax=ax,
        horizontal=horizontal,
        vertical=vertical,
        color=color,
        linestyle=linestyle,
        linewidth=linewidth,
        alpha=alpha,
        label=label,
    )


def add_highlight_region(
    xmin: Optional[float] = None,
    xmax: Optional[float] = None,
    ymin: Optional[float] = None,
    ymax: Optional[float] = None,
    color: str = "0.85",
    alpha: float = 0.5,
    label: Optional[str] = None,
    ax=None,
):
    """Add highlighted region to current axis.

    Parameters
    ----------
    xmin, xmax, ymin, ymax : float, optional
        Region boundaries
    color : str
        Region color
    alpha : float
        Transparency
    label : str, optional
        Label for legend
    ax : Axes, optional
        Axis to add region to. If None, uses current axis.
    """
    if ax is None:
        ax = gca()

    style = get_style()
    style.add_highlight_region(
        ax=ax,
        xmin=xmin,
        xmax=xmax,
        ymin=ymin,
        ymax=ymax,
        color=color,
        alpha=alpha,
        label=label,
    )


def format_legend(
    loc: str = "best",
    frameon: bool = True,
    framealpha: float = 0.8,
    ncol: int = 1,
    ax=None,
    **kwargs,
):
    """Format legend with consistent styling.

    Parameters
    ----------
    loc : str
        Legend location
    frameon : bool
        Whether to draw frame
    framealpha : float
        Frame transparency
    ncol : int
        Number of columns
    ax : Axes, optional
        Axis containing legend. If None, uses current axis.
    **kwargs
        Additional arguments passed to legend()
    """
    if ax is None:
        ax = gca()

    style = get_style()
    return style.format_legend(
        ax=ax,
        loc=loc,
        frameon=frameon,
        framealpha=framealpha,
        ncol=ncol,
        **kwargs,
    )


# Auto-initialize with default settings when module is imported
initialize_style()
