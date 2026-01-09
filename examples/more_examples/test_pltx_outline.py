"""Test the outline feature for better line visibility."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pltx.pyplot as plt
import numpy as np

print("Testing outline feature...")

# Generate data
x = np.linspace(0, 10, 100)

# Create figure with two subplots for comparison
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Left plot: Without outline
for i in range(4):
    y = np.sin(x + i * 0.5) + i * 0.5
    plt.plot_styled(x, y, color_idx=i, linewidth=3, label=f'Line {i+1}', ax=ax1)

plt.setup_axis(ax1, xlabel='x', ylabel='y', title='Without Outline', grid=False)
ax1.legend()

# Right plot: With outline (better visibility)
for i in range(4):
    y = np.sin(x + i * 0.5) + i * 0.5
    plt.plot_styled(
        x, y,
        color_idx=i,
        linewidth=3,
        label=f'Line {i+1}',
        outline=True,  # Add black outline
        outline_width=5,  # Slightly wider than line
        ax=ax2
    )

plt.setup_axis(ax2, xlabel='x', ylabel='y', title='With Outline (Better Visibility)', grid=False)
ax2.legend()

plt.tight_layout()
plt.savefig('test_outline_comparison.pdf')
print(" Saved: test_outline_comparison.pdf")

# Create another example showing different outline colors
fig, ax = plt.subplots(figsize=(10, 6))

# Plot with different outline colors
plt.plot_styled(
    x, np.sin(x) + 2,
    color_idx=0,
    linewidth=3,
    label='Black outline (default)',
    outline=True,
    outline_color='black',
    ax=ax
)

plt.plot_styled(
    x, np.sin(x) + 1,
    color_idx=2,
    linewidth=3,
    label='White outline',
    outline=True,
    outline_color='white',
    outline_width=5,
    ax=ax
)

plt.plot_styled(
    x, np.sin(x),
    color_idx=4,
    linewidth=3,
    label='Gray outline',
    outline=True,
    outline_color='0.3',  # Dark gray
    outline_width=5,
    ax=ax
)

plt.setup_axis(ax, xlabel='x', ylabel='y', title='Different Outline Colors', grid=True)
ax.legend()

plt.tight_layout()
plt.savefig('test_outline_colors.pdf')
print(" Saved: test_outline_colors.pdf")

print("\nOutline feature test completed!")
print("\nUsage:")
print("  plt.plot_styled(x, y, color_idx=0, outline=True)")
print("  plt.plot_styled(x, y, color_idx=1, outline=True, outline_color='white', outline_width=5)")
