"""Color palettes and utilities for pltx."""

from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt

try:
    import seaborn as sns
    HAS_SEABORN = True
except ImportError:
    HAS_SEABORN = False

# Type alias for RGB color
Color = Tuple[float, float, float]


class ColorPalette:
    """Manages color palettes for scientific visualizations."""

    # Default palettes - easily customizable
    DEFAULT_PALETTE = "plasma_r"
    DEFAULT_SIZE = 10

    # Predefined palette collections
    SEQUENTIAL_PALETTES = [
        "plasma_r",
        "viridis",
        "mako_r",
        "rocket_r",
        "crest",
    ]

    DIVERGING_PALETTES = [
        "coolwarm",
        "RdBu_r",
        "vlag",
        "icefire",
    ]

    CATEGORICAL_PALETTES = [
        "tab10",
        "Set2",
        "husl",
        "Paired",
    ]

    def __init__(
        self,
        palette_name: str = DEFAULT_PALETTE,
        palette_size: int = DEFAULT_SIZE,
    ):
        """Initialize color palette.

        Parameters
        ----------
        palette_name : str
            Name of the seaborn or matplotlib color palette
        palette_size : int
            Number of colors in the palette
        """
        self.palette_name = palette_name
        self.palette_size = palette_size
        self._palette = self._create_palette(palette_name, palette_size)

    @staticmethod
    def _create_palette(palette_name: str, palette_size: int) -> List[Color]:
        """Create color palette using seaborn if available, else matplotlib.

        Parameters
        ----------
        palette_name : str
            Name of the color palette
        palette_size : int
            Number of colors

        Returns
        -------
        List[Color]
            List of RGB tuples
        """
        if HAS_SEABORN:
            return sns.color_palette(palette_name, palette_size)
        else:
            # Fallback to matplotlib colormaps
            try:
                cmap = plt.get_cmap(palette_name)
            except ValueError:
                # If palette not found, use viridis as fallback
                cmap = plt.get_cmap('viridis')

            # Sample colors from colormap
            colors = [cmap(i / (palette_size - 1)) for i in range(palette_size)]
            # Convert to RGB tuples (remove alpha channel)
            return [(c[0], c[1], c[2]) for c in colors]

    @property
    def palette(self) -> List[Color]:
        """Get the current color palette."""
        return self._palette

    def get_color(self, idx: int) -> Color:
        """Get a color from the palette by index.

        Parameters
        ----------
        idx : int
            Index of the color in the palette

        Returns
        -------
        Color
            RGB color tuple

        Raises
        ------
        IndexError
            If index is out of range
        """
        if idx < 0 or idx >= len(self._palette):
            raise IndexError(
                f"Color index {idx} out of range for palette of size {len(self._palette)}"
            )
        return self._palette[idx]

    def get_colors(self, indices: List[int]) -> List[Color]:
        """Get multiple colors from the palette.

        Parameters
        ----------
        indices : List[int]
            Indices of colors to retrieve

        Returns
        -------
        List[Color]
            List of RGB color tuples
        """
        return [self.get_color(idx) for idx in indices]

    def cycle_color(self, idx: int) -> Color:
        """Get a color with automatic wrapping for large indices.

        Parameters
        ----------
        idx : int
            Index (will be wrapped if >= palette_size)

        Returns
        -------
        Color
            RGB color tuple
        """
        return self._palette[idx % len(self._palette)]

    @staticmethod
    def adjust_intensity(
        color: Color,
        intensity: float,
    ) -> Color:
        """Adjust color intensity (brightness).

        Parameters
        ----------
        color : Color
            RGB color tuple
        intensity : float
            Intensity factor (0.0-1.0). Lower values make colors lighter.

        Returns
        -------
        Color
            Adjusted RGB color tuple
        """
        intensity = np.clip(intensity, 0.0, 1.0)
        return tuple(c * intensity + (1 - intensity) for c in color)

    @staticmethod
    def adjust_alpha(
        color: Color,
        alpha: float,
    ) -> Tuple[float, float, float, float]:
        """Add alpha channel to RGB color.

        Parameters
        ----------
        color : Color
            RGB color tuple
        alpha : float
            Alpha value (0.0-1.0)

        Returns
        -------
        Tuple[float, float, float, float]
            RGBA color tuple
        """
        alpha = np.clip(alpha, 0.0, 1.0)
        return (*color, alpha)

    @staticmethod
    def create_gradient(
        color1: Color,
        color2: Color,
        n_steps: int,
    ) -> List[Color]:
        """Create a gradient between two colors.

        Parameters
        ----------
        color1 : Color
            Starting color
        color2 : Color
            Ending color
        n_steps : int
            Number of steps in the gradient

        Returns
        -------
        List[Color]
            List of colors forming the gradient
        """
        gradient = []
        for i in range(n_steps):
            t = i / (n_steps - 1)
            color = tuple(
                c1 * (1 - t) + c2 * t
                for c1, c2 in zip(color1, color2)
            )
            gradient.append(color)
        return gradient

    def set_palette(
        self,
        palette_name: str,
        palette_size: int = None,
    ) -> None:
        """Change the current palette.

        Parameters
        ----------
        palette_name : str
            Name of the seaborn or matplotlib color palette
        palette_size : int, optional
            Number of colors. If None, uses current palette_size.
        """
        self.palette_name = palette_name
        if palette_size is not None:
            self.palette_size = palette_size
        self._palette = self._create_palette(self.palette_name, self.palette_size)

    def __len__(self) -> int:
        """Return the number of colors in the palette."""
        return len(self._palette)

    def __getitem__(self, idx: int) -> Color:
        """Get a color by index."""
        return self.get_color(idx)

    def __iter__(self):
        """Iterate over colors in the palette."""
        return iter(self._palette)

    def __repr__(self) -> str:
        """String representation."""
        return f"ColorPalette('{self.palette_name}', size={self.palette_size})"


# Global default color palette
_default_palette = ColorPalette()


def get_default_palette() -> ColorPalette:
    """Get the global default color palette."""
    return _default_palette


def set_default_palette(
    palette_name: str,
    palette_size: int = ColorPalette.DEFAULT_SIZE,
) -> None:
    """Set the global default color palette.

    Parameters
    ----------
    palette_name : str
        Name of the seaborn color palette
    palette_size : int
        Number of colors in the palette
    """
    global _default_palette
    _default_palette = ColorPalette(palette_name, palette_size)


def get_color(idx: int) -> Color:
    """Get a color from the default palette.

    Parameters
    ----------
    idx : int
        Color index

    Returns
    -------
    Color
        RGB color tuple
    """
    return _default_palette.get_color(idx)


def cycle_color(idx: int) -> Color:
    """Get a color from the default palette with automatic wrapping.

    Parameters
    ----------
    idx : int
        Color index (will wrap if >= palette size)

    Returns
    -------
    Color
        RGB color tuple
    """
    return _default_palette.cycle_color(idx)
