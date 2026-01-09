"""Quick test of pltx package."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pltx import PlotStyle
import pltx.pyplot as plt
import numpy as np

print("Testing pltx package...")

# Test 1: Basic imports
print(" Imports successful")

# Test 2: Initialize style
style = PlotStyle(palette_name="plasma_r", palette_size=10)
print(" PlotStyle initialized")

# Test 3: Color palette
from pltx.colors import get_color, cycle_color
color1 = get_color(0)
print(f" Color palette working: {color1}")

# Test 4: Create a simple plot
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(figsize=(8, 5))
plt.plot_styled(x, y1, label='sin(x)', color_idx=0, linewidth=2)
plt.plot_styled(x, y2, label='cos(x)', color_idx=2, linewidth=2)
plt.setup_axis(
    xlabel='x',
    ylabel='y',
    title='pltx Test Plot',
    grid=True
)
plt.legend()
plt.tight_layout()
plt.savefig('test_pltx_output.pdf')
print(" Plot created and saved to test_pltx_output.pdf")

print("\nAll tests passed! ")
print("\nYou can now use pltx in your code:")
print("  import pltx.pyplot as plt")
print("  from pltx import PlotStyle")
