"""Test pltx with different plot types and style presets."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pltx.pyplot as plt
from pltx.rcparams import apply_style_preset
import numpy as np

print("Testing pltx with different plot types...")

# Generate data
np.random.seed(42)
categories = ['A', 'B', 'C', 'D', 'E']
values1 = [23, 45, 56, 78, 32]
values2 = [34, 55, 43, 68, 41]
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# ============================================================================
# Test 1: Default Style with Various Plot Types
# ============================================================================
print("\n1. Default style with different plot types...")
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

# Line plot with pltx styling
plt.plot_styled(x, y1, color_idx=0, label='sin(x)', linewidth=2, ax=ax1)
plt.plot_styled(x, y2, color_idx=2, label='cos(x)', linewidth=2, ax=ax1)
plt.setup_axis(ax1, xlabel='x', ylabel='y', title='Line Plot', grid=True)
ax1.legend()

# Bar plot (uses style colors automatically)
from pltx.colors import get_color
colors = [get_color(i) for i in range(len(categories))]
ax2.bar(categories, values1, color=colors, edgecolor='black', linewidth=1)
ax2.set_xlabel('Category')
ax2.set_ylabel('Value')
ax2.set_title('Bar Plot')
ax2.tick_params(axis='both', direction='in')

# Scatter plot
plt.plot_styled(x[::5], y1[::5], marker='o', linestyle='', markersize=8,
               color_idx=0, label='sin', ax=ax3)
plt.plot_styled(x[::5], y2[::5], marker='s', linestyle='', markersize=8,
               color_idx=2, label='cos', ax=ax3)
plt.setup_axis(ax3, xlabel='x', ylabel='y', title='Scatter Plot', grid=True)
ax3.legend()

# Grouped bar plot
x_pos = np.arange(len(categories))
width = 0.35
ax4.bar(x_pos - width/2, values1, width, label='Group 1', color=get_color(0), edgecolor='black')
ax4.bar(x_pos + width/2, values2, width, label='Group 2', color=get_color(2), edgecolor='black')
ax4.set_xlabel('Category')
ax4.set_ylabel('Value')
ax4.set_title('Grouped Bar Plot')
ax4.set_xticks(x_pos)
ax4.set_xticklabels(categories)
ax4.legend()
ax4.tick_params(axis='both', direction='in')

plt.tight_layout()
plt.savefig('test_all_plots_default.pdf')
print("    Saved: test_all_plots_default.pdf")

# ============================================================================
# Test 2: Nature Journal Style
# ============================================================================
print("\n2. Nature journal style...")
apply_style_preset('nature')
plt.initialize_style(palette_name='viridis', palette_size=8)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(7, 6))

# Line plot
plt.plot_styled(x, y1, color_idx=0, label='sin(x)', linewidth=1.5, ax=ax1,
               centerline=True, centerline_width=0.5)
plt.plot_styled(x, y2, color_idx=2, label='cos(x)', linewidth=1.5, ax=ax1,
               centerline=True, centerline_width=0.5)
plt.setup_axis(ax1, xlabel='x', ylabel='y', title='Line Plot', grid=False)
ax1.legend(fontsize=7)

# Bar plot
colors = [get_color(i) for i in range(len(categories))]
ax2.bar(categories, values1, color=colors, edgecolor='black', linewidth=0.5)
ax2.set_xlabel('Category', fontsize=8)
ax2.set_ylabel('Value', fontsize=8)
ax2.set_title('Bar Plot', fontsize=9)
ax2.tick_params(axis='both', direction='in', labelsize=7)

# Scatter
plt.plot_styled(x[::5], y1[::5], marker='o', linestyle='', markersize=4,
               color_idx=0, label='sin', ax=ax3)
plt.plot_styled(x[::5], y2[::5], marker='s', linestyle='', markersize=4,
               color_idx=2, label='cos', ax=ax3)
plt.setup_axis(ax3, xlabel='x', ylabel='y', title='Scatter Plot', grid=False)
ax3.legend(fontsize=7)

# Histogram
data = np.random.randn(1000)
ax4.hist(data, bins=30, color=get_color(1), edgecolor='black', linewidth=0.5)
ax4.set_xlabel('Value', fontsize=8)
ax4.set_ylabel('Frequency', fontsize=8)
ax4.set_title('Histogram', fontsize=9)
ax4.tick_params(axis='both', direction='in', labelsize=7)

plt.tight_layout()
plt.savefig('test_all_plots_nature.pdf')
print("    Saved: test_all_plots_nature.pdf (Nature journal style)")

# ============================================================================
# Test 3: Presentation Style
# ============================================================================
print("\n3. Presentation style...")
apply_style_preset('presentation')
plt.initialize_style(palette_name='plasma_r', palette_size=10)

fig, ax = plt.subplots(1, 1, figsize=(10, 6))

# Bold lines for presentations
plt.plot_styled(x, y1, color_idx=0, label='sin(x)', linewidth=4, ax=ax,
               outline=True, outline_width=6)
plt.plot_styled(x, y2, color_idx=3, label='cos(x)', linewidth=4, ax=ax,
               outline=True, outline_width=6)
plt.setup_axis(ax, xlabel='x', ylabel='y',
              title='Presentation Style - Bold and Clear',
              grid=True)
ax.legend(fontsize=16)

plt.tight_layout()
plt.savefig('test_all_plots_presentation.pdf')
print("    Saved: test_all_plots_presentation.pdf (Presentation style)")

print("\n All plot types tested with different style presets!")
print("\nStyle presets available:")
print("  - 'default': Standard pltx style")
print("  - 'nature': Nature journal requirements (small fonts, single column)")
print("  - 'presentation': Large fonts and thick lines")
print("  - 'poster': Very large fonts for posters")
print("\nUsage:")
print("  from pltx.rcparams import apply_style_preset")
print("  apply_style_preset('nature')")
