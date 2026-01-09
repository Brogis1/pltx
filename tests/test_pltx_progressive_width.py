"""Test progressive line width increase for colorblind accessibility."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pltx.pyplot as plt
import numpy as np

print("Testing progressive line width increase...")

# Generate data
x = np.linspace(0, 10, 100)

# Create comparison figure with different progression factors
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# ============================================================================
# Plot 1: No width variation (baseline)
# ============================================================================
plt.initialize_style(palette_name='viridis', vary_linewidth=False)

for i in range(6):
    y = np.sin(x + i * 0.5) + i * 0.5
    plt.plot_styled(x, y, color_idx=i, linewidth=2, label=f'Line {i+1}', ax=ax1)

plt.setup_axis(ax1, xlabel='x', ylabel='y',
              title='No Width Variation\n(All lines same thickness)',
              grid=False)
ax1.legend(fontsize=9)

# ============================================================================
# Plot 2: Progressive increase, factor=1.2 (gentle)
# ============================================================================
plt.initialize_style(
    palette_name='viridis',
    vary_linewidth=True,
    base_linewidth=1.5,
    linewidth_progression_factor=1.2  # 20% increase each line
)

for i in range(6):
    y = np.sin(x + i * 0.5) + i * 0.5
    plt.plot_styled(x, y, color_idx=i, label=f'Line {i+1}', ax=ax2)

plt.setup_axis(ax2, xlabel='x', ylabel='y',
              title='Progressive Width: Factor=1.2\n(Gentle 20% increase)',
              grid=False)
ax2.legend(fontsize=9)
ax2.text(0.02, 0.98, 'GENTLE', transform=ax2.transAxes,
         fontsize=10, fontweight='bold', va='top',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

# ============================================================================
# Plot 3: Progressive increase, factor=1.3 (moderate - DEFAULT)
# ============================================================================
plt.initialize_style(
    palette_name='viridis',
    vary_linewidth=True,
    base_linewidth=1.5,
    linewidth_progression_factor=1.3  # 30% increase each line (DEFAULT)
)

for i in range(6):
    y = np.sin(x + i * 0.5) + i * 0.5
    plt.plot_styled(x, y, color_idx=i, label=f'Line {i+1}', ax=ax3)

plt.setup_axis(ax3, xlabel='x', ylabel='y',
              title='Progressive Width: Factor=1.3 (DEFAULT)\n(Moderate 30% increase)',
              grid=False)
ax3.legend(fontsize=9)
ax3.text(0.02, 0.98, 'RECOMMENDED', transform=ax3.transAxes,
         fontsize=10, fontweight='bold', va='top',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

# ============================================================================
# Plot 4: Progressive increase, factor=1.5 (strong)
# ============================================================================
plt.initialize_style(
    palette_name='viridis',
    vary_linewidth=True,
    base_linewidth=1.5,
    linewidth_progression_factor=1.5  # 50% increase each line
)

for i in range(6):
    y = np.sin(x + i * 0.5) + i * 0.5
    plt.plot_styled(x, y, color_idx=i, label=f'Line {i+1}', ax=ax4)

plt.setup_axis(ax4, xlabel='x', ylabel='y',
              title='Progressive Width: Factor=1.5\n(Strong 50% increase)',
              grid=False)
ax4.legend(fontsize=9)
ax4.text(0.02, 0.98, 'STRONG', transform=ax4.transAxes,
         fontsize=10, fontweight='bold', va='top',
         bbox=dict(boxstyle='round', facecolor='orange', alpha=0.7))

plt.tight_layout()
plt.savefig('test_progressive_width_factors.pdf')
print(" Saved: test_progressive_width_factors.pdf")

# ============================================================================
# Show progression with many lines
# ============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Factor 1.2 (gentle) - good for many lines
plt.initialize_style(
    palette_name='tab10',
    vary_linewidth=True,
    base_linewidth=1.0,
    linewidth_progression_factor=1.2
)

for i in range(10):
    y = np.sin(x + i * 0.3) + i * 0.3
    plt.plot_styled(x, y, color_idx=i, label=f'{i+1}', ax=ax1)

plt.setup_axis(ax1, xlabel='x', ylabel='y',
              title='10 Lines: Factor=1.2\n(Good for many lines)',
              grid=False)
ax1.legend(ncol=2, fontsize=8)

# Factor 1.3 (moderate) - good for 4-6 lines
plt.initialize_style(
    palette_name='tab10',
    vary_linewidth=True,
    base_linewidth=1.0,
    linewidth_progression_factor=1.3
)

for i in range(10):
    y = np.sin(x + i * 0.3) + i * 0.3
    plt.plot_styled(x, y, color_idx=i, label=f'{i+1}', ax=ax2)

plt.setup_axis(ax2, xlabel='x', ylabel='y',
              title='10 Lines: Factor=1.3\n(Good for 4-6 lines)',
              grid=False)
ax2.legend(ncol=2, fontsize=8)

plt.tight_layout()
plt.savefig('test_progressive_width_many_lines.pdf')
print(" Saved: test_progressive_width_many_lines.pdf")

# ============================================================================
# Show exact widths
# ============================================================================
print("\n Line width progression examples:")
print("\nBase width = 2.0")
print("-" * 60)

for factor in [1.2, 1.3, 1.5]:
    print(f"\nFactor = {factor} ({int((factor-1)*100)}% increase per line):")
    widths = [2.0 * (factor ** i) for i in range(6)]
    for i, w in enumerate(widths):
        print(f"  Line {i}: {w:.2f}pt")

print("\n Progressive width feature tested!")
print("\nUsage:")
print("  plt.initialize_style(")
print("      vary_linewidth=True,")
print("      base_linewidth=2.0,")
print("      linewidth_progression_factor=1.3  # 30% increase per line")
print("  )")
print("")
print("Recommended factors:")
print("  - 1.2 (20%): Gentle, good for 8-10 lines")
print("  - 1.3 (30%): Moderate, good for 4-6 lines (DEFAULT)")
print("  - 1.5 (50%): Strong, good for 2-4 lines")
