"""Example 05: Using the PlotStyle class directly without the pyplot wrapper."""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Add parent directory to path to enable local package import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from pltx import PlotStyle

# Create data
x = np.linspace(0, 10, 100)

# 1. Initialize PlotStyle object
style = PlotStyle(
    palette_name='viridis',
    palette_size=8,
    font_size_medium=14,
    font_size_large=16
)

# 2. Create figure and axis using standard matplotlib
fig, ax = plt.subplots(figsize=(8, 5))

# 3. Use style methods for plotting and formatting
style.plot_curve(ax, x, np.sin(x), color_idx=0, linewidth=3, label='sin(x)')
style.plot_curve(ax, x, np.cos(x), color_idx=4, linewidth=3, label='cos(x)')

style.setup_axis(
    ax,
    xlabel='x',
    ylabel='y',
    title='Direct PlotStyle Usage',
    grid=True
)

style.format_legend(ax, loc='upper right', framealpha=0.9)

plt.tight_layout()
plt.savefig('05_direct_style_usage.pdf')
print("Saved: 05_direct_style_usage.pdf")
