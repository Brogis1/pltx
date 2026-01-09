"""Test the centerline feature - thin line on top of colored lines."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pltx.pyplot as plt
import numpy as np

print("Testing centerline feature...")

# Generate data
x = np.linspace(0, 10, 100)

# Create figure with comparison plots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# ============================================================================
# Plot 1: Without any enhancement (baseline)
# ============================================================================
for i in range(4):
    y = np.sin(x + i * 0.5) + i * 0.5
    plt.plot_styled(x, y, color_idx=i, linewidth=4, label=f'Line {i+1}', ax=ax1)

plt.setup_axis(ax1, xlabel='x', ylabel='y', title='Baseline (No Enhancement)', grid=False)
ax1.legend()

# ============================================================================
# Plot 2: With OUTLINE (thick line behind)
# ============================================================================
for i in range(4):
    y = np.sin(x + i * 0.5) + i * 0.5
    plt.plot_styled(
        x, y,
        color_idx=i,
        linewidth=4,
        label=f'Line {i+1}',
        outline=True,
        outline_width=6,
        ax=ax2
    )

plt.setup_axis(ax2, xlabel='x', ylabel='y', title='With Outline (Behind)', grid=False)
ax2.legend()

# ============================================================================
# Plot 3: With CENTERLINE (thin line on top) - NEW!
# ============================================================================
for i in range(4):
    y = np.sin(x + i * 0.5) + i * 0.5
    plt.plot_styled(
        x, y,
        color_idx=i,
        linewidth=4,
        label=f'Line {i+1}',
        centerline=True,  # NEW FEATURE!
        centerline_width=1.0,
        ax=ax3
    )

plt.setup_axis(ax3, xlabel='x', ylabel='y', title='With Centerline (On Top) - NEW!', grid=False)
ax3.legend()
ax3.text(0.02, 0.98, 'NEW FEATURE!', transform=ax3.transAxes,
         fontsize=10, fontweight='bold', va='top',
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

# ============================================================================
# Plot 4: Both OUTLINE + CENTERLINE (maximum contrast)
# ============================================================================
for i in range(4):
    y = np.sin(x + i * 0.5) + i * 0.5
    plt.plot_styled(
        x, y,
        color_idx=i,
        linewidth=4,
        label=f'Line {i+1}',
        outline=True,
        outline_width=6,
        centerline=True,
        centerline_width=0.8,
        ax=ax4
    )

plt.setup_axis(ax4, xlabel='x', ylabel='y', title='Both Outline + Centerline', grid=False)
ax4.legend()

plt.tight_layout()
plt.savefig('test_centerline_comparison.pdf')
print(" Saved: test_centerline_comparison.pdf")

# ============================================================================
# Create another example with different centerline colors
# ============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Black centerline (default)
for i in range(4):
    y = np.sin(x + i * 0.5) + i * 0.5
    plt.plot_styled(
        x, y,
        color_idx=i,
        linewidth=5,
        label=f'Line {i+1}',
        centerline=True,
        centerline_color='black',
        centerline_width=1.2,
        ax=ax1
    )

plt.setup_axis(ax1, xlabel='x', ylabel='y', title='Black Centerline (Default)', grid=False)
ax1.legend()

# White centerline
for i in range(4):
    y = np.sin(x + i * 0.5) + i * 0.5
    plt.plot_styled(
        x, y,
        color_idx=i,
        linewidth=5,
        label=f'Line {i+1}',
        centerline=True,
        centerline_color='white',
        centerline_width=1.2,
        ax=ax2
    )

plt.setup_axis(ax2, xlabel='x', ylabel='y', title='White Centerline', grid=False)
ax2.legend()

plt.tight_layout()
plt.savefig('test_centerline_colors.pdf')
print(" Saved: test_centerline_colors.pdf")

print("\nCenterline feature test completed!")
print("\nUsage:")
print("  # Thin line on top of colored line")
print("  plt.plot_styled(x, y, color_idx=0, centerline=True)")
print("")
print("  # Custom centerline")
print("  plt.plot_styled(x, y, color_idx=1, centerline=True,")
print("                  centerline_color='white', centerline_width=1.0)")
print("")
print("  # Both outline and centerline for maximum contrast")
print("  plt.plot_styled(x, y, color_idx=2, outline=True, centerline=True)")
