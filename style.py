"""Enhanced PlotStyle class for pltx."""

from typing import Optional, Tuple, Union, List
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.ticker as mticker
import numpy as np

from .colors import ColorPalette, Color
from .rcparams import apply_rcparams, apply_style_preset, StylePreset
import contextlib


class PlotStyle:
    """Enhanced plotting style manager for scientific visualizations.

    This class provides a unified interface for creating publication-quality
    plots with consistent styling, color schemes, and formatting.
    """

    def __init__(
        self,
        palette_name: str = "plasma_r",
        palette_size: int = 10,
        font_size_medium: int = 12,
        font_size_large: int = 13,
        use_tex: bool = False,
        auto_apply: bool = True,
        vary_linewidth: bool = False,
        base_linewidth: float = 2.0,
        linewidth_progression_factor: float = 1.3,
    ):
        """Initialize plot style parameters.

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
        auto_apply : bool
            Whether to automatically apply global style settings
        vary_linewidth : bool
            If True, automatically vary line widths for colorblind accessibility
            Each line gets progressively thicker
        base_linewidth : float
            Base line width when vary_linewidth is True
        linewidth_progression_factor : float
            Factor for progressive width increase. Each line is multiplied by this factor.
            Examples: 1.2 (20% increase), 1.3 (30% increase), 1.5 (50% increase)
        """
        self.palette_name = palette_name
        self.palette_size = palette_size
        self.font_size_medium = font_size_medium
        self.font_size_large = font_size_large
        self.use_tex = use_tex
        self.vary_linewidth = vary_linewidth
        self.base_linewidth = base_linewidth
        self.linewidth_progression_factor = linewidth_progression_factor

        # Initialize color palette
        self.color_palette = ColorPalette(palette_name, palette_size)

        # Automatic color cycling index
        self._color_cycle_idx = 0

        # Apply global style settings
        if auto_apply:
            self.apply_global_style()

    def apply_global_style(self) -> None:
        """Apply global matplotlib style settings."""
        apply_rcparams(
            font_size_medium=self.font_size_medium,
            font_size_large=self.font_size_large,
            use_tex=self.use_tex,
        )

    @property
    def palette(self) -> List[Color]:
        """Get the current color palette."""
        return self.color_palette.palette

    def get_color(self, idx: int) -> Color:
        """Get a color from the palette.

        Parameters
        ----------
        idx : int
            Color index

        Returns
        -------
        Color
            RGB color tuple
        """
        return self.color_palette.get_color(idx)

    def cycle_color(self, idx: int) -> Color:
        """Get a color with automatic index wrapping.

        Parameters
        ----------
        idx : int
            Color index (will wrap if >= palette size)

        Returns
        -------
        Color
            RGB color tuple
        """
        return self.color_palette.cycle_color(idx)

    def reset_color_cycle(self) -> None:
        """Reset the automatic color cycling index to zero."""
        self._color_cycle_idx = 0

    @contextlib.contextmanager
    def style_context(self, preset: StylePreset, **kwargs):
        """Context manager for temporary style application.

        Parameters
        ----------
        preset : str
            Style preset name ('nature', 'presentation', 'poster', etc.)
        **kwargs
            Optional rcParams overrides
        """
        # Save current rcParams (simplified approach: matplotlib rcParams are global)
        # In a real implementation, we'd need to deep copy them, but for now we'll
        # just apply the preset and rely on the user to know it's global for now
        # OR better: save the ones we know we are changing.
        # For simplicity and given the scope, we apply the preset.
        old_params = plt.rcParams.copy()
        try:
            apply_style_preset(preset, **kwargs)
            yield
        finally:
            plt.rcParams.update(old_params)

    def get_linewidth(self, idx: int, base_width: Optional[float] = None) -> float:
        """Get line width for given index with progressive increase.

        Each line gets progressively thicker by the progression factor.
        For example, with factor=1.3:
        - Line 0: base_width * 1.0
        - Line 1: base_width * 1.3
        - Line 2: base_width * 1.69
        - Line 3: base_width * 2.2
        - etc.

        Parameters
        ----------
        idx : int
            Line index
        base_width : float, optional
            Base line width. If None, uses self.base_linewidth

        Returns
        -------
        float
            Line width (progressively increases with idx)
        """
        if not self.vary_linewidth:
            return base_width if base_width is not None else self.base_linewidth

        base = base_width if base_width is not None else self.base_linewidth
        # Progressive increase: base * factor^idx
        return base * (self.linewidth_progression_factor ** idx)

    def setup_axis(
        self,
        ax: matplotlib.axes.Axes,
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
    ) -> None:
        """Apply consistent styling to an axis.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            The axis to style
        xlim, ylim : tuple, optional
            x and y axis limits
        xlabel, ylabel : str, optional
            Axis labels
        title : str, optional
            Axis title
        xscale, yscale : str, optional
            Scale for each axis ('linear', 'log', etc.)
        xtick_spacing, ytick_spacing : float, optional
            Spacing for major ticks
        grid : bool
            Whether to show grid
        grid_alpha : float
            Grid transparency
        """
        # Set scales
        ax.set_xscale(xscale)
        ax.set_yscale(yscale)

        # Set limits
        if xlim is not None:
            ax.set_xlim(xlim)
        if ylim is not None:
            ax.set_ylim(ylim)

        # Set labels
        if xlabel is not None:
            ax.set_xlabel(xlabel)
        if ylabel is not None:
            ax.set_ylabel(ylabel)
        if title is not None:
            ax.set_title(title)

        # Set tick directions
        ax.tick_params(axis="both", direction="in", top=True, right=True)
        if xscale == "log":
            ax.tick_params(axis="x", which="minor", direction="in")
        if yscale == "log":
            ax.tick_params(axis="y", which="minor", direction="in")

        # Set tick spacing
        if xtick_spacing is not None:
            ax.xaxis.set_major_locator(mticker.MultipleLocator(base=xtick_spacing))
        if ytick_spacing is not None:
            ax.yaxis.set_major_locator(mticker.MultipleLocator(base=ytick_spacing))

        # Configure log scale ticks
        if yscale == "log":
            ax.yaxis.set_major_locator(mticker.LogLocator(numticks=5))
            ax.yaxis.set_minor_locator(mticker.LogLocator(numticks=15, subs="auto"))
        if xscale == "log":
            ax.xaxis.set_major_locator(mticker.LogLocator(numticks=5))
            ax.xaxis.set_minor_locator(mticker.LogLocator(numticks=15, subs="auto"))

        # Grid
        if grid:
            ax.grid(True, alpha=grid_alpha, linestyle="--", linewidth=0.5)

    def add_reference_line(
        self,
        ax: matplotlib.axes.Axes,
        horizontal: Optional[Union[float, List[float]]] = None,
        vertical: Optional[Union[float, List[float]]] = None,
        color: str = "k",
        linestyle: str = "--",
        linewidth: float = 0.5,
        alpha: float = 0.3,
        label: Optional[str] = None,
    ) -> None:
        """Add reference lines to the plot.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            The axis to add lines to
        horizontal : float or list, optional
            y-values for horizontal lines
        vertical : float or list, optional
            x-values for vertical lines
        color, linestyle, linewidth, alpha : float
            Line style parameters
        label : str, optional
            Label for legend (only applied to first line)
        """
        # Handle horizontal lines
        if horizontal is not None:
            if not isinstance(horizontal, (list, tuple, np.ndarray)):
                horizontal = [horizontal]
            for i, h in enumerate(horizontal):
                ax.axhline(
                    y=h,
                    color=color,
                    linestyle=linestyle,
                    linewidth=linewidth,
                    alpha=alpha,
                    label=label if i == 0 else None,
                )

        # Handle vertical lines
        if vertical is not None:
            if not isinstance(vertical, (list, tuple, np.ndarray)):
                vertical = [vertical]
            for i, v in enumerate(vertical):
                ax.axvline(
                    x=v,
                    color=color,
                    linestyle=linestyle,
                    linewidth=linewidth,
                    alpha=alpha,
                    label=label if i == 0 and horizontal is None else None,
                )

    def add_highlight_region(
        self,
        ax: matplotlib.axes.Axes,
        xmin: Optional[float] = None,
        xmax: Optional[float] = None,
        ymin: Optional[float] = None,
        ymax: Optional[float] = None,
        color: str = "0.85",
        alpha: float = 0.5,
        label: Optional[str] = None,
    ) -> None:
        """Add a highlighted region to the plot.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            The axis to add highlight to
        xmin, xmax, ymin, ymax : float, optional
            Region boundaries
        color : str
            Color for the highlighted region
        alpha : float
            Transparency
        label : str, optional
            Label for the legend
        """
        if ymin is not None and ymax is not None:
            ax.axhspan(ymin, ymax, color=color, alpha=alpha, label=label)
        elif xmin is not None and xmax is not None:
            ax.axvspan(xmin, xmax, color=color, alpha=alpha, label=label)

    def plot_curve(
        self,
        ax: matplotlib.axes.Axes,
        x: np.ndarray,
        y: np.ndarray,
        label: Optional[str] = None,
        color: Optional[Union[str, Color]] = None,
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
        centerline: bool = False,
        centerline_color: str = "black",
        centerline_width: Optional[float] = None,
        **kwargs,
    ) -> matplotlib.lines.Line2D:
        """Plot a curve with consistent styling.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            The axis to plot on
        x, y : array-like
            Data to plot
        label : str, optional
            Label for the legend
        color : str or Color, optional
            Line color (hex, name, or RGB tuple)
        color_idx : int, optional
            Index into the palette to select a color
        color_intensity : float, optional
            Intensity factor (0.0-1.0). Lower values make colors lighter.
        linestyle, linewidth, marker, markersize :
            Line and marker style parameters
        alpha : float, optional
            Transparency
        outline : bool
            If True, adds a thick outline behind the line for better visibility
        outline_color : str
            Color of the outline (default: 'black')
        outline_width : float, optional
            Width of the outline. If None, uses linewidth + 2
        centerline : bool
            If True, adds a thin line on top of the colored line
        centerline_color : str
            Color of the center line (default: 'black')
        centerline_width : float, optional
            Width of the center line. If None, uses linewidth / 3
        **kwargs
            Additional arguments passed to ax.plot()

        Returns
        -------
        matplotlib.lines.Line2D
            The plotted line object (the main colored line)
        """
        # Determine color
        if color_idx is None and color is None:
            color_idx = self._color_cycle_idx
            self._color_cycle_idx += 1

        if color is None and color_idx is not None:
            color = self.cycle_color(color_idx)

            # Apply intensity adjustment if specified
            if color_intensity is not None:
                color = ColorPalette.adjust_intensity(color, color_intensity)

        # Vary line width for colorblind accessibility
        if self.vary_linewidth and color_idx is not None:
            linewidth = self.get_linewidth(color_idx, linewidth)

        # Layer 1: Plot outline first (if requested) - appears behind everything
        if outline:
            if outline_width is None:
                outline_width = linewidth + 2

            ax.plot(
                x,
                y,
                color=outline_color,
                linestyle=linestyle,
                linewidth=outline_width,
                marker=marker,
                markersize=markersize + 1 if markersize else None,
                alpha=alpha,
                zorder=1,  # Behind the main line
                **kwargs,
            )

        # Layer 2: Plot the main colored curve
        line = ax.plot(
            x,
            y,
            label=label,
            color=color,
            linestyle=linestyle,
            linewidth=linewidth,
            marker=marker,
            markersize=markersize,
            alpha=alpha,
            zorder=2 if outline else None,  # In front of outline
            **kwargs,
        )[0]

        # Layer 3: Plot centerline on top (if requested) - appears in front
        if centerline:
            if centerline_width is None:
                centerline_width = max(0.5, linewidth / 3)

            ax.plot(
                x,
                y,
                color=centerline_color,
                linestyle=linestyle,
                linewidth=centerline_width,
                marker=marker,
                markersize=markersize - 1 if markersize else None,
                alpha=alpha,
                zorder=3,  # On top of main line
                **kwargs,
            )

        return line

    def scatter_styled(
        self,
        ax: matplotlib.axes.Axes,
        x: np.ndarray,
        y: np.ndarray,
        label: Optional[str] = None,
        color: Optional[Union[str, Color]] = None,
        color_idx: Optional[int] = None,
        size: float = 20,
        marker: str = "o",
        alpha: Optional[float] = None,
        **kwargs,
    ):
        """Plot scatter points with consistent styling.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            The axis to plot on
        x, y : array-like
            Data to plot
        label : str, optional
            Label for the legend
        color : str or Color, optional
            Point color
        color_idx : int, optional
            Index into the palette to select a color
        size : float
            Marker size
        marker : str
            Marker style
        alpha : float, optional
            Transparency
        **kwargs
            Additional arguments passed to ax.scatter()

        Returns
        -------
        PathCollection
            The scatter plot object
        """
        # Determine color
        if color_idx is None and color is None:
            color_idx = self._color_cycle_idx
            self._color_cycle_idx += 1

        if color is None and color_idx is not None:
            color = self.cycle_color(color_idx)

        return ax.scatter(
            x,
            y,
            label=label,
            color=color,
            s=size,
            marker=marker,
            alpha=alpha,
            **kwargs,
        )

    def plot_scatter(self, *args, **kwargs):
        """Alias for scatter_styled."""
        return self.scatter_styled(*args, **kwargs)

    def errorbar_styled(
        self,
        ax: matplotlib.axes.Axes,
        x: np.ndarray,
        y: np.ndarray,
        yerr: Optional[np.ndarray] = None,
        xerr: Optional[np.ndarray] = None,
        label: Optional[str] = None,
        color: Optional[Union[str, Color]] = None,
        color_idx: Optional[int] = None,
        linewidth: float = 2,
        capsize: float = 3,
        fmt: str = "o",
        **kwargs,
    ):
        """Plot error bars with consistent styling.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            The axis to plot on
        x, y : array-like
            Data points
        yerr, xerr : array-like, optional
            Error values
        label : str, optional
            Label for the legend
        color : str or Color, optional
            Plot color
        color_idx : int, optional
            Index into the palette
        linewidth : float
            Line width
        capsize : float
            Cap size for error bars
        fmt : str
            Format string for markers/lines
        **kwargs
            Additional arguments passed to ax.errorbar()
        """
        # Determine color
        if color_idx is None and color is None:
            color_idx = self._color_cycle_idx
            self._color_cycle_idx += 1

        if color is None and color_idx is not None:
            color = self.cycle_color(color_idx)

        # Vary line width for colorblind accessibility
        if self.vary_linewidth and color_idx is not None:
            linewidth = self.get_linewidth(color_idx, linewidth)

        return ax.errorbar(
            x,
            y,
            yerr=yerr,
            xerr=xerr,
            label=label,
            color=color,
            linewidth=linewidth,
            capsize=capsize,
            fmt=fmt,
            **kwargs,
        )

    def bar_styled(
        self,
        ax: matplotlib.axes.Axes,
        x: Union[List, np.ndarray],
        height: Union[List, np.ndarray],
        label: Optional[str] = None,
        color: Optional[Union[str, Color]] = None,
        color_idx: Optional[int] = None,
        edgecolor: str = "black",
        linewidth: float = 1,
        **kwargs,
    ):
        """Plot bar chart with consistent styling.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            The axis to plot on
        x : array-like
            x-coordinates of the bars
        height : array-like
            Heights of the bars
        label : str, optional
            Label for the legend
        color : str or Color, optional
            Bar color
        color_idx : int, optional
            Index into the palette
        edgecolor : str
            Color of bar edges
        linewidth : float
            Width of bar edges
        **kwargs
            Additional arguments passed to ax.bar()
        """
        # Determine color
        if color_idx is None and color is None:
            color_idx = self._color_cycle_idx
            self._color_cycle_idx += 1

        if color is None and color_idx is not None:
            color = self.cycle_color(color_idx)

        return ax.bar(
            x,
            height,
            label=label,
            color=color,
            edgecolor=edgecolor,
            linewidth=linewidth,
            **kwargs,
        )

    def hist_styled(
        self,
        ax: matplotlib.axes.Axes,
        x: np.ndarray,
        bins: Optional[Union[int, np.ndarray]] = None,
        label: Optional[str] = None,
        color: Optional[Union[str, Color]] = None,
        color_idx: Optional[int] = None,
        edgecolor: str = "white",
        alpha: float = 0.8,
        **kwargs,
    ):
        """Plot histogram with consistent styling.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            The axis to plot on
        x : array-like
            Data to histogram
        bins : int or array-like, optional
            Number of bins or bin edges
        label : str, optional
            Label for the legend
        color : str or Color, optional
            Histogram color
        color_idx : int, optional
            Index into the palette
        edgecolor : str
            Color of bin edges
        alpha : float
            Transparency
        **kwargs
            Additional arguments passed to ax.hist()
        """
        # Determine color
        if color_idx is None and color is None:
            color_idx = self._color_cycle_idx
            self._color_cycle_idx += 1

        if color is None and color_idx is not None:
            color = self.cycle_color(color_idx)

        return ax.hist(
            x,
            bins=bins,
            label=label,
            color=color,
            edgecolor=edgecolor,
            alpha=alpha,
            **kwargs,
        )

    def format_legend(
        self,
        ax: matplotlib.axes.Axes,
        loc: str = "best",
        frameon: bool = True,
        framealpha: float = 0.8,
        ncol: int = 1,
        **kwargs,
    ) -> matplotlib.legend.Legend:
        """Format legend with consistent styling.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            The axis containing the legend
        loc : str
            Legend location
        frameon : bool
            Whether to draw frame
        framealpha : float
            Frame transparency
        ncol : int
            Number of columns
        **kwargs
            Additional arguments passed to ax.legend()

        Returns
        -------
        matplotlib.legend.Legend
            The legend object
        """
        return ax.legend(
            loc=loc,
            frameon=frameon,
            framealpha=framealpha,
            ncol=ncol,
            **kwargs,
        )
