"""Register the pasqal colormaps."""

from importlib import resources
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import matplotlib.pyplot as mpl_plt


def register_pasqal_cmap():
    """Register the pasqal colormaps.

    Uses importlib.resources to locate .npy data files, which works
    reliably in both development and pip-installed packages.
    """
    pkg = resources.files(__package__)

    pasqal_colors = np.load(pkg / 'pasqal_cmap.npy')
    pasqal_contrast_colors = np.load(pkg / 'pasqal_contrast_cmap.npy')
    pasqal_diverging_colors = np.load(pkg / 'pasqal_diverging.npy')

    for name, colors in [
        ('pasqal',           pasqal_colors),
        ('pasqal_contrast',  pasqal_contrast_colors),
        ('pasqal_diverging', pasqal_diverging_colors),
    ]:
        cmap = LinearSegmentedColormap.from_list(name, colors)
        mpl_plt.colormaps.register(cmap, name=name, force=True)


if __name__ == '__main__':
    register_pasqal_cmap()
