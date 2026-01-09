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
fig = plt.figure(figsize=(14, 16))
gs = fig.add_gridspec(5, 2, height_ratios=[1.2, 1, 1, 1, 1], hspace=0.35, wspace=0.3)

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
ax1.text(0.02, 0.98, 'BESTSELLER!', transform=ax1.transAxes,
         fontsize=10, fontweight='bold', va='top',
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

# ============================================================================
# Plot 2: Centerlines (Thin line on top)
# ============================================================================
ax2 = fig.add_subplot(gs[0, 1])
# Demonstrate centerline vs outline vs both
plt.plot_styled(x, y1, color_idx=1, linewidth=4, label='Outline Only',
                outline=True, ax=ax2)
plt.plot_styled(x, y1 - 1, color_idx=3, linewidth=4, label='Centerline Only',
                centerline=True, ax=ax2)
plt.plot_styled(x, y1 - 2, color_idx=6, linewidth=4, label='Both (Enhanced)',
                outline=True, centerline=True, ax=ax2)
plt.setup_axis(ax2, xlabel='x', ylabel='y',
               title='Centerlines & Hybrid Enhancements',
               grid=True, xlim=(0, 10), ylim=(-3.5, 1.5))
ax2.legend(loc='lower right', fontsize=9)

# ============================================================================
# Plot 3: Color Intensity Variations
# ============================================================================
ax3 = fig.add_subplot(gs[1, 0])
intensities = [1.0, 0.7, 0.4]
for i, intensity in enumerate(intensities):
    y = np.sin(x - i * 0.3)
    plt.plot_styled(x, y, color_idx=0, color_intensity=intensity,
                   linewidth=2, label=f'Intensity {intensity}', ax=ax3)
plt.setup_axis(ax3, xlabel='x', ylabel='y',
               title='Color Intensity Adjustment',
               grid=True, xlim=(0, 10), ylim=(-1.5, 1.5))
ax3.legend(loc='upper right')

# ============================================================================
# Plot 4: Reference Lines and Highlighted Regions
# ============================================================================
ax4 = fig.add_subplot(gs[1, 1])
plt.plot_styled(x, y1 + noise, color_idx=1, linewidth=2,
               label='Data with noise', ax=ax4)
plt.add_reference_line(horizontal=[0.5, -0.5], color='red',
                      linestyle='--', alpha=0.5, label='Threshold', ax=ax4)
plt.add_reference_line(vertical=[2, 5, 8], color='green',
                      alpha=0.3, ax=ax4)
plt.add_highlight_region(ymin=-0.5, ymax=0.5, color='yellow',
                        alpha=0.2, label='Safe zone', ax=ax4)
plt.setup_axis(ax4, xlabel='x', ylabel='y',
               title='Reference Lines & Regions',
               grid=True, xlim=(0, 10), ylim=(-1.5, 1.5))
ax4.legend(loc='upper right', fontsize=9)

# ============================================================================
# Plot 5: Log Scale with Auto Color Cycling
# ============================================================================
ax5 = fig.add_subplot(gs[2, 0])
for i in range(5):
    y = np.exp(0.4 * x + i)
    plt.plot_styled(x, y, color_idx=i, linewidth=2,
                   label=f'exp(0.4x + {i})', ax=ax5)
plt.setup_axis(ax5, xlabel='x', ylabel='y (log scale)',
               title='Log Scale with Color Cycling',
               yscale='log', grid=True, xlim=(0, 10))
ax5.legend(loc='upper left', fontsize=9)

# ============================================================================
# Plot 6: Progressive Line Width (Accessibility)
# ============================================================================
ax6 = fig.add_subplot(gs[2, 1])
# Temporarily enable varying linewidth for this plot
with plt.style_context('default', vary_linewidth=True):
    for i in range(4):
        plt.plot_styled(x, np.sin(x) + i*0.8, color_idx=i+2,
                       label=f'Line {i} (Width x{1.3**i:.1f})', ax=ax6)
plt.setup_axis(ax6, xlabel='x', ylabel='y',
               title='Accessibility: Progressive Widths',
               grid=True, xlim=(0, 10))
ax6.legend(loc='upper right', fontsize=8)
ax6.text(0.05, 0.05, 'Distinguishable by both color AND width',
         transform=ax6.transAxes, fontsize=9, style='italic')

# ============================================================================
# Plot 7: Styled Bar Charts
# ============================================================================
ax7 = fig.add_subplot(gs[3, 0])
categories = ['A', 'B', 'C', 'D', 'E']
values = [4, 7, 3, 8, 5]
plt.bar_styled(categories, values, color_idx=2, alpha=0.8, ax=ax7)
plt.setup_axis(ax7, xlabel='Category', ylabel='Value',
               title='Styled Bar Charts', grid=True)

# ============================================================================
# Plot 8: Styled Histograms
# ============================================================================
ax8 = fig.add_subplot(gs[3, 1])
data = np.random.normal(0, 1, 1000)
plt.hist_styled(data, bins=30, color_idx=4, alpha=0.7,
               edgecolor='white', ax=ax8)
plt.setup_axis(ax8, xlabel='Value', ylabel='Frequency',
               title='Styled Histograms', grid=True)

# ============================================================================
# Plot 9: Error Bars with Styling
# ============================================================================
ax9 = fig.add_subplot(gs[4, 0])
x_err = np.linspace(0, 10, 10)
y_err = np.sin(x_err)
err = 0.2 * np.ones_like(x_err)
plt.errorbar_styled(x_err, y_err, yerr=err, color_idx=7,
                   linewidth=2, capsize=4, label='Data w/ Error', ax=ax9)
plt.setup_axis(ax9, xlabel='x', ylabel='y',
               title='Error Bars with Styling',
               grid=True, xlim=(0, 10), ylim=(-1.5, 1.5))
ax9.legend(loc='upper right', fontsize=9)

# ============================================================================
# Plot 10: Markers with Outlines
# ============================================================================
ax10 = fig.add_subplot(gs[4, 1])
x_sparse = x[::15]
plt.plot_styled(x_sparse, np.sin(x_sparse), color_idx=0,
               marker='o', markersize=8, linestyle='-', linewidth=2,
               label='Circles', outline=True, ax=ax10)
plt.plot_styled(x_sparse, np.cos(x_sparse), color_idx=3,
               marker='s', markersize=8, linestyle='--', linewidth=2,
               label='Squares', outline=True, ax=ax10)
plt.setup_axis(ax10, xlabel='x', ylabel='y',
               title='Markers with Outlines',
               grid=True, xlim=(0, 10), ylim=(-1.5, 1.5))
ax10.legend(loc='upper right', fontsize=9)

# Add main title
fig.suptitle('pltx - Enhanced Matplotlib Showcase',
             fontsize=18, fontweight='bold', y=0.99)

# Save
os.makedirs('img', exist_ok=True)
plt.savefig('img/showcase.pdf', dpi=300, bbox_inches='tight')
plt.savefig('img/showcase.png', dpi=150, bbox_inches='tight')
print(" Saved: img/showcase.pdf and img/showcase.png")

print("\nShowcase includes:")
print("  1. Line outlines for better visibility")
print("  2. Centerlines (thin line on top)")
print("  3. Color intensity variations")
print("  4. Reference lines and highlighted regions")
print("  5. Log scale with automatic color cycling")
print("  6. Progressive line width (Accessibility feature)")
print("  7. Styled bar charts")
print("  8. Styled histograms")
print("  9. Error bars with styling")
print("  10. Markers with outlines")
print("\nAll features demonstrated in one comprehensive example!")
