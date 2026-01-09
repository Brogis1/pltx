"""Example 02: Using different color palettes with pltx."""

import sys
import os
import numpy as np

# Add parent directory to path to enable local package import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import pltx.pyplot as plt

# Generate data
x = np.linspace(0, 10, 100)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Different palettes for each subplot
palettes = ['plasma_r', 'viridis', 'mako_r', 'rocket_r']

for ax, palette in zip(axs.flat, palettes):
    # Temporarily change palette for this subplot
    plt.initialize_style(palette_name=palette)

    for i in range(3):
        y = np.sin(x + i) * np.exp(-0.1 * x * i)
        plt.plot_styled(x, y, color_idx=i, linewidth=3, ax=ax, label=f'Line {i+1}')

    plt.setup_axis(ax, xlabel='x', ylabel='y', title=f'Palette: {palette}', grid=True)
    ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig('02_color_palettes.pdf')
print("Saved: 02_color_palettes.pdf")
