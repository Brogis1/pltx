"""Test automatic line width variation for colorblind accessibility."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pltx.pyplot as plt
import numpy as np

print("Testing colorblind-friendly line width variation...")

# Generate data
x = np.linspace(0, 10, 100)

# Create comparison figure
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

# ============================================================================
# Plot 1: Standard (all same width) - HARD for colorblind
# ============================================================================
plt.initialize_style(palette_name='viridis', vary_linewidth=False)

for i in range(6):
    y = np.sin(x + i * 0.5) + i * 0.5
    plt.plot_styled(x, y, color_idx=i, linewidth=2, label=f'Line {i+1}', ax=ax1)

plt.setup_axis(ax1, xlabel='x', ylabel='y',
              title='Standard (Same Width)\nDifficult for Colorblind',
              grid=False)
ax1.legend(fontsize=9)

# ============================================================================
# Plot 2: Varied line widths - BETTER for colorblind
# ============================================================================
plt.initialize_style(palette_name='viridis', vary_linewidth=True, base_linewidth=2.0)

for i in range(6):
    y = np.sin(x + i * 0.5) + i * 0.5
    plt.plot_styled(x, y, color_idx=i, label=f'Line {i+1}', ax=ax2)

plt.setup_axis(ax2, xlabel='x', ylabel='y',
              title='Varied Widths (NEW!)\nColorblind Accessible',
              grid=False)
ax2.legend(fontsize=9)
ax2.text(0.02, 0.98, 'COLORBLIND\nFRIENDLY', transform=ax2.transAxes,
         fontsize=11, fontweight='bold', va='top',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

# ============================================================================
# Plot 3: Varied widths + centerlines - BEST for colorblind
# ============================================================================
for i in range(6):
    y = np.sin(x + i * 0.5) + i * 0.5
    plt.plot_styled(x, y, color_idx=i, label=f'Line {i+1}',
                   centerline=True, centerline_width=0.7, ax=ax3)

plt.setup_axis(ax3, xlabel='x', ylabel='y',
              title='Varied Widths + Centerlines\nBest Accessibility',
              grid=False)
ax3.legend(fontsize=9)
ax3.text(0.02, 0.98, 'MAXIMUM\nACCESSIBILITY', transform=ax3.transAxes,
         fontsize=11, fontweight='bold', va='top',
         bbox=dict(boxstyle='round', facecolor='gold', alpha=0.7))

plt.tight_layout()
plt.savefig('test_colorblind_comparison.pdf')
print(" Saved: test_colorblind_comparison.pdf")

# ============================================================================
# Create a demo showing many lines (> palette size)
# ============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Without width variation
plt.initialize_style(palette_name='tab10', vary_linewidth=False, palette_size=10)
for i in range(15):
    y = np.sin(x + i * 0.3) + i * 0.2
    plt.plot_styled(x, y, color_idx=i, linewidth=2, label=f'{i+1}', ax=ax1)

plt.setup_axis(ax1, xlabel='x', ylabel='y',
              title='15 Lines, No Width Variation\n(Colors repeat, hard to distinguish)',
              grid=False)
ax1.legend(ncol=2, fontsize=8)

# With width variation
plt.initialize_style(palette_name='tab10', vary_linewidth=True,
                    base_linewidth=2.0, palette_size=10)
for i in range(15):
    y = np.sin(x + i * 0.3) + i * 0.2
    plt.plot_styled(x, y, color_idx=i, label=f'{i+1}', ax=ax2)

plt.setup_axis(ax2, xlabel='x', ylabel='y',
              title='15 Lines, With Width Variation\n(Easier to distinguish)',
              grid=False)
ax2.legend(ncol=2, fontsize=8)

plt.tight_layout()
plt.savefig('test_colorblind_many_lines.pdf')
print(" Saved: test_colorblind_many_lines.pdf")

print("\n Colorblind accessibility feature tested!")
print("\nUsage:")
print("  # Enable automatic line width variation")
print("  plt.initialize_style(vary_linewidth=True, base_linewidth=2.0)")
print("")
print("  # Then plot as usual - widths are automatically varied")
print("  plt.plot_styled(x, y, color_idx=0)")
print("  plt.plot_styled(x, y, color_idx=1)  # Different width automatically")
print("")
print("Benefits:")
print("  - Lines distinguishable by width AND color")
print("  - Helps colorblind users identify different lines")
print("  - Pattern: base, base*1.5, base*0.75, base*2.0, base*0.5, ...")
print("  - Automatic cycling for any number of lines")
