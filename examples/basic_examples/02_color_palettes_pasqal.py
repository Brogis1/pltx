"""Example 02: Using the Pasqal color palettes with pltx.

pltx automatically registers the 'pasqal' and 'pasqal_contrast' colormaps
at import time (via cmap/register_cmap.py), so they can be used directly
as palette names in initialize_style().
"""

import numpy as np
import pltx.pyplot as plt

# Generate data
x = np.linspace(0, 10, 100)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Pasqal palettes -- registered automatically when pltx is imported
palettes = ['pasqal', 'pasqal_contrast']

for ax, palette in zip(axs.flat, palettes):
    # Temporarily change palette for this subplot
    plt.initialize_style(palette_name=palette)

    for i in range(3):
        y = np.sin(x + i) * np.exp(-0.1 * x * i)
        plt.plot_styled(x, y, color_idx=i, linewidth=3, ax=ax,
                        label=f'Line {i+1}')

    plt.setup_axis(ax, xlabel='x', ylabel='y',
                   title=f'Palette: {palette}', grid=True)
    ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig('02_color_palettes.pdf')
print("Saved: 02_color_palettes.pdf")
