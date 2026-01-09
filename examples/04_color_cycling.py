"""Example 04: Automatic color cycling utilities in pltx."""

import sys
import os
import numpy as np

# Add parent directory to path to enable local package import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import pltx.pyplot as plt
from pltx.colors import cycle_color

x = np.linspace(0, 10, 100)
fig, ax = plt.subplots(figsize=(8, 5))

# Show color cycling with 15 lines but only 10 colors in palette
for i in range(15):
    color = cycle_color(i)  # Automatically wraps around palette size
    y = np.sin(x + i * 0.5) + i * 0.3
    ax.plot(x, y, color=color, linewidth=2, label=f'Line {i}')

plt.setup_axis(ax, xlabel='x', ylabel='y',
              title='Automatic Color Cycling (10 color palette)')

# Format legend with many columns
plt.format_legend(ax=ax, bbox_to_anchor=(1.02, 1), loc='upper left', ncol=2)

plt.tight_layout()
plt.savefig('04_color_cycling.pdf')
print("Saved: 04_color_cycling.pdf")
