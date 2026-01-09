"""Example 01: Basic usage of pltx as a drop-in replacement for matplotlib.pyplot."""

import sys
import os
import numpy as np

# Add parent directory to path to enable local package import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import pltx.pyplot as plt

# Generate data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create plot
fig, ax = plt.subplots(figsize=(8, 5))

# Use plot_styled for automatic pltx styling
plt.plot_styled(x, y1, label='sin(x)', color_idx=0, linewidth=2)
plt.plot_styled(x, y2, label='cos(x)', color_idx=2, linewidth=2)

# Setup axis with convenience function
plt.setup_axis(
    xlabel='x',
    ylabel='y',
    title='Basic pltx Example',
    grid=True,
    xlim=(0, 10),
    ylim=(-1.5, 1.5)
)

# Add reference lines
plt.add_reference_line(horizontal=0, color='k', alpha=0.3)

plt.legend()
plt.tight_layout()
plt.savefig('01_basic_usage.pdf')
print("Saved: 01_basic_usage.pdf")
