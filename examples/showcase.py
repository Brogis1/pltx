"""Showcase all pltx features in one comprehensive example."""

import sys
import os
# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

import pltx.pyplot as plt
import numpy as np

# Generate sample data
np.random.seed(42)
x = np.linspace(0, 10, 200)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.exp(-0.1 * x)
noise = 0.1 * np.random.randn(len(x))

# Initialize with custom style
plt.initialize_style(
    palette_name='plasma_r',
    palette_size=10,
    font_size_medium=11,
    font_size_large=13,
    use_tex=False
)

# Create comprehensive figure
fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(3, 2, height_ratios=[1.5, 1, 1], hspace=0.3, wspace=0.3)

# ============================================================================
# Plot 1: Line Outlines Feature (NEW!)
# ============================================================================
ax1 = fig.add_subplot(gs[0, 0])
plt.plot_styled(x, y1, color_idx=0, linewidth=3, label='sin(x)',
                outline=True, outline_width=5, ax=ax1)
plt.plot_styled(x, y2, color_idx=2, linewidth=3, label='cos(x)',
                outline=True, outline_width=5, ax=ax1)
plt.plot_styled(x, y3, color_idx=5, linewidth=3, label='damped sin(x)',
                outline=True, outline_width=5, ax=ax1)
plt.setup_axis(ax1, xlabel='x', ylabel='y',
               title='Line Outlines for Better Visibility',
               grid=False, xlim=(0, 10), ylim=(-1.2, 1.2))
ax1.legend(loc='upper right', framealpha=0.9)
ax1.text(0.02, 0.98, 'NEW FEATURE!', transform=ax1.transAxes,
         fontsize=10, fontweight='bold', va='top',
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

# ============================================================================
# Plot 2: Color Intensity Variations
# ============================================================================
ax2 = fig.add_subplot(gs[0, 1])
intensities = [1.0, 0.7, 0.4]
for i, intensity in enumerate(intensities):
    y = np.sin(x - i * 0.3)
    plt.plot_styled(x, y, color_idx=0, color_intensity=intensity,
                   linewidth=2, label=f'Intensity {intensity}', ax=ax2)
plt.setup_axis(ax2, xlabel='x', ylabel='y',
               title='Color Intensity Adjustment',
               grid=True, xlim=(0, 10), ylim=(-1.5, 1.5))
ax2.legend(loc='upper right')

# ============================================================================
# Plot 3: Reference Lines and Highlighted Regions
# ============================================================================
ax3 = fig.add_subplot(gs[1, 0])
plt.plot_styled(x, y1 + noise, color_idx=1, linewidth=2,
               label='Data with noise', ax=ax3)
plt.add_reference_line(horizontal=[0.5, -0.5], color='red',
                      linestyle='--', alpha=0.5, label='Threshold', ax=ax3)
plt.add_reference_line(vertical=[2, 5, 8], color='green',
                      alpha=0.3, ax=ax3)
plt.add_highlight_region(ymin=-0.5, ymax=0.5, color='yellow',
                        alpha=0.2, label='Safe zone', ax=ax3)
plt.setup_axis(ax3, xlabel='x', ylabel='y',
               title='Reference Lines & Regions',
               grid=True, xlim=(0, 10), ylim=(-1.5, 1.5))
ax3.legend(loc='upper right', fontsize=9)

# ============================================================================
# Plot 4: Log Scale with Auto Color Cycling
# ============================================================================
ax4 = fig.add_subplot(gs[1, 1])
for i in range(5):
    y = np.exp(0.5 * x + i)
    plt.plot_styled(x, y, color_idx=i, linewidth=2,
                   label=f'exp(0.5x + {i})', ax=ax4)
plt.setup_axis(ax4, xlabel='x', ylabel='y (log scale)',
               title='Log Scale with Color Cycling',
               yscale='log', grid=True, xlim=(0, 10))
ax4.legend(loc='upper left', fontsize=9)

# ============================================================================
# Plot 5: Multiple Line Styles
# ============================================================================
ax5 = fig.add_subplot(gs[2, 0])
styles = ['-', '--', '-.', ':']
for i, style in enumerate(styles):
    plt.plot_styled(x, np.sin(x + i * 0.5) + i * 0.5,
                   color_idx=i*2, linestyle=style, linewidth=2,
                   label=f'Style: {style}', ax=ax5)
plt.setup_axis(ax5, xlabel='x', ylabel='y',
               title='Different Line Styles',
               grid=True, xlim=(0, 10))
ax5.legend(loc='upper left', fontsize=9)

# ============================================================================
# Plot 6: Scatter with Markers and Outlines
# ============================================================================
ax6 = fig.add_subplot(gs[2, 1])
x_sparse = x[::10]
plt.plot_styled(x_sparse, np.sin(x_sparse), color_idx=0,
               marker='o', markersize=8, linestyle='-', linewidth=2,
               label='Circles', outline=True, ax=ax6)
plt.plot_styled(x_sparse, np.cos(x_sparse), color_idx=3,
               marker='s', markersize=8, linestyle='--', linewidth=2,
               label='Squares', outline=True, ax=ax6)
plt.plot_styled(x_sparse, np.sin(x_sparse + 1), color_idx=6,
               marker='^', markersize=8, linestyle='-.', linewidth=2,
               label='Triangles', outline=True, ax=ax6)
plt.setup_axis(ax6, xlabel='x', ylabel='y',
               title='Markers with Outlines',
               grid=True, xlim=(0, 10), ylim=(-1.5, 1.5))
ax6.legend(loc='upper right', fontsize=9)

# Add main title
fig.suptitle('pltx - Enhanced Matplotlib Showcase',
             fontsize=16, fontweight='bold', y=0.995)

# Save
plt.savefig('pltx_showcase.pdf', dpi=300, bbox_inches='tight')
print(" Saved: pltx_showcase.pdf")
print("\nShowcase includes:")
print("  1. Line outlines for better visibility (NEW!)")
print("  2. Color intensity variations")
print("  3. Reference lines and highlighted regions")
print("  4. Log scale with automatic color cycling")
print("  5. Multiple line styles")
print("  6. Markers with outlines")
print("\nAll features demonstrated in one comprehensive example!")
