"""Register the pasqal colormaps."""

from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import os
import matplotlib.pyplot as mpl_plt

# Directory that contains this file and the .npy colormap data
_CMAP_DIR = os.path.dirname(os.path.abspath(__file__))


def register_pasqal_cmap():
    """Register the pasqal colormaps.

    The colormap data files are resolved relative to this module's
    location, so this function works correctly regardless of the
    caller's working directory.
    """

    pasqal_colors = np.load(os.path.join(_CMAP_DIR, 'pasqal_cmap.npy'))
    pasqal_contrast_colors = np.load(
        os.path.join(_CMAP_DIR, 'pasqal_contrast_cmap.npy')
    )

    for name, colors in [
        ('pasqal',          pasqal_colors),
        ('pasqal_contrast', pasqal_contrast_colors),
    ]:
        cmap = LinearSegmentedColormap.from_list(name, colors)
        mpl_plt.colormaps.register(cmap, name=name, force=True)

    print(f'Colormaps "pasqal" and "pasqal_contrast" registered')


if __name__ == '__main__':
    register_pasqal_cmap()
