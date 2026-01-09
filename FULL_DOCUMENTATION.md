# pltx - Complete Documentation

**Enhanced matplotlib wrapper for publication-quality scientific visualization**

---

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Core Features](#core-features)
4. [API Reference](#api-reference)
5. [Style Presets](#style-presets)
6. [Colorblind Accessibility](#colorblind-accessibility)
7. [Examples](#examples)
8. [Best Practices](#best-practices)
9. [Migration Guide](#migration-guide)

---

## Overview

pltx is a matplotlib wrapper that provides:
- **Progressive line width variation** for colorblind accessibility
- **Line outlines and centerlines** for better visibility
- **Journal-ready style presets** (Nature, presentation, poster)
- **Automatic color cycling** with palette management
- **Drop-in replacement** for matplotlib.pyplot

Works with all matplotlib plot types: lines, bars, scatter, histograms, heatmaps, etc.

---

## Installation

### Option 1: Direct Import (Quick)

```python
import sys
sys.path.insert(0, '/path/to/pltx')
import pltx.pyplot as plt
```

### Option 2: Install as Package (Recommended)

```bash
cd /path/to/pltx
pip install -e .
```

Then simply:
```python
import pltx.pyplot as plt
```

### Dependencies

**Required:**
- matplotlib >= 3.5.0
- numpy >= 1.20.0

**Optional:**
- seaborn >= 0.11.0 (for extended color palettes; falls back to matplotlib colormaps)

---

## Core Features

### 1. Progressive Line Width (Colorblind Accessible)

**The Problem:** Standard plots rely solely on color to distinguish lines. For colorblind viewers (~8% of males, ~0.5% of females), this fails.

**The Solution:** Each line gets progressively thicker by a configurable factor.

```python
import pltx.pyplot as plt

plt.initialize_style(
    vary_linewidth=True,              # Enable progressive width
    base_linewidth=2.0,               # Starting width
    linewidth_progression_factor=1.3  # 30% increase per line (default)
)

# Plot multiple lines - widths increase automatically
for i in range(5):
    plt.plot_styled(x, y[i], color_idx=i, label=f'Line {i+1}')
```

**Result with factor=1.3:**
- Line 0: 2.00pt (base)
- Line 1: 2.60pt (base x 1.3)
- Line 2: 3.38pt (base x 1.3^2)
- Line 3: 4.39pt (base x 1.3^3)
- Line 4: 5.71pt (base x 1.3^4)

Lines are now distinguishable by **both color AND thickness**!

#### Choosing the Right Factor

| Factor | Increase | Best For | Example Widths (base=2.0) |
|--------|----------|----------|---------------------------|
| **1.2** | 20% | 8-10 lines | 2.0, 2.4, 2.9, 3.5, 4.2 |
| **1.3** | 30% | 4-6 lines (DEFAULT) | 2.0, 2.6, 3.4, 4.4, 5.7 |
| **1.5** | 50% | 2-4 lines | 2.0, 3.0, 4.5, 6.8, 10.1 |

**Formula:** `width(n) = base_linewidth x (factor^n)`

### 2. Line Outlines

Add a thick line behind colored lines (halo effect) for better visibility.

```python
plt.plot_styled(
    x, y,
    color_idx=0,
    outline=True,            # Enable outline
    outline_color='black',   # Default: black
    outline_width=5          # Default: linewidth + 2
)
```

**Use cases:**
- Bright colors on light backgrounds
- Busy/cluttered plots
- Presentation slides

### 3. Centerlines

Add a thin line on top of colored lines for subtle enhancement.

```python
plt.plot_styled(
    x, y,
    color_idx=0,
    centerline=True,         # Enable centerline
    centerline_color='black', # Default: black
    centerline_width=1.0     # Default: linewidth / 3
)
```

**Use cases:**
- Clean plots needing subtle distinction
- Print publications
- Better than outlines for minimal designs

### 4. Combine Both

Maximum contrast for maximum visibility:

```python
plt.plot_styled(
    x, y,
    color_idx=0,
    outline=True,      # Thick line behind
    centerline=True    # Thin line on top
)
```

### 5. Style Presets

Pre-configured styles for different media:

```python
from pltx.rcparams import apply_style_preset

# Nature journal (Arial, 7-9pt, 3.5" width, 300 DPI)
apply_style_preset('nature')

# Presentation (16-18pt, thick lines)
apply_style_preset('presentation')

# Poster (24-28pt, very thick lines)
apply_style_preset('poster')

# Default (12-13pt, general purpose)
apply_style_preset('default')
```

#### Preset Details

| Preset | Font Size | Figure Size | Line Width | DPI | Use Case |
|--------|-----------|-------------|------------|-----|----------|
| **nature** | 7-9pt | 3.5"x2.6" | 1.0pt | 300 | Nature, Nature Methods, etc. |
| **presentation** | 16-18pt | 10"x6" | 3pt | 150 | Conference talks, slides |
| **poster** | 24-28pt | 12"x8" | 4pt | 150 | Academic posters |
| **default** | 12-13pt | 6"x4" | 2pt | 100 | Papers, reports, general |

---

## API Reference

### Initialize Style

```python
plt.initialize_style(
    palette_name='plasma_r',          # Color palette name
    palette_size=10,                  # Number of colors
    font_size_medium=12,              # Standard font size
    font_size_large=13,               # Title font size
    use_tex=False,                    # LaTeX rendering
    vary_linewidth=False,             # Progressive width
    base_linewidth=2.0,               # Starting width
    linewidth_progression_factor=1.3  # Width increase factor
)
```

### Plot Styled

Enhanced line plotting with automatic color cycling:

```python
plt.plot_styled(
    x, y,                            # Data
    label=None,                      # Legend label
    color=None,                      # Explicit color
    color_idx=None,                  # Palette index (auto-cycles)
    color_intensity=1.0,             # Brightness (0.0-1.0)
    linewidth=2,                     # Line width (auto if vary_linewidth)
    linestyle='-',                   # Line style
    marker=None,                     # Marker style
    markersize=None,                 # Marker size
    alpha=None,                      # Transparency
    outline=False,                   # Add outline behind
    outline_color='black',           # Outline color
    outline_width=None,              # Outline width (default: linewidth+2)
    centerline=False,                # Add line on top
    centerline_color='black',        # Centerline color
    centerline_width=None,           # Centerline width (default: linewidth/3)
    ax=None,                         # Axis (None = current)
    **kwargs                         # Additional matplotlib args
)
```

### Setup Axis

Configure multiple axis properties at once:

```python
plt.setup_axis(
    xlabel=None,                     # X-axis label
    ylabel=None,                     # Y-axis label
    title=None,                      # Axis title
    xlim=None,                       # X-axis limits (min, max)
    ylim=None,                       # Y-axis limits
    xscale='linear',                 # X-axis scale ('linear', 'log')
    yscale='linear',                 # Y-axis scale
    xtick_spacing=None,              # X-tick spacing
    ytick_spacing=None,              # Y-tick spacing
    grid=False,                      # Show grid
    grid_alpha=0.3,                  # Grid transparency
    ax=None                          # Axis (None = current)
)
```

### Reference Lines

Add horizontal and/or vertical reference lines:

```python
plt.add_reference_line(
    horizontal=None,                 # y-values (float or list)
    vertical=None,                   # x-values (float or list)
    color='k',                       # Line color
    linestyle='--',                  # Line style
    linewidth=0.5,                   # Line width
    alpha=0.3,                       # Transparency
    label=None,                      # Legend label
    ax=None                          # Axis (None = current)
)
```

### Highlight Regions

Add shaded rectangular regions:

```python
plt.add_highlight_region(
    xmin=None, xmax=None,           # X-boundaries (for vertical region)
    ymin=None, ymax=None,           # Y-boundaries (for horizontal region)
    color='0.85',                   # Region color
    alpha=0.5,                      # Transparency
    label=None,                     # Legend label
    ax=None                         # Axis (None = current)
)
```

### Color Utilities

```python
from pltx.colors import get_color, cycle_color, ColorPalette

# Get specific color from default palette
color = get_color(3)  # 4th color (0-indexed)

# Auto-wrap for large indices (works even if palette size < idx)
color = cycle_color(15)  # Automatically wraps around

# Create custom palette
palette = ColorPalette('viridis', size=8)
color = palette.get_color(2)

# Color manipulation
light_color = ColorPalette.adjust_intensity(color, 0.5)  # Lighten
rgba_color = ColorPalette.adjust_alpha(color, 0.7)      # Add alpha
gradient = ColorPalette.create_gradient(c1, c2, n_steps=10)
```

### Direct PlotStyle Usage

For maximum control:

```python
from pltx import PlotStyle
import matplotlib.pyplot as plt

style = PlotStyle(
    palette_name='viridis',
    vary_linewidth=True,
    linewidth_progression_factor=1.3
)

fig, ax = plt.subplots()

style.plot_curve(ax, x, y, color_idx=0, centerline=True)
style.setup_axis(ax, xlabel='x', ylabel='y')
style.format_legend(ax, loc='upper right')

plt.show()
```

---

## Style Presets

### Nature Journal

```python
from pltx.rcparams import apply_style_preset
import pltx.pyplot as plt

apply_style_preset('nature')

plt.initialize_style(
    vary_linewidth=True,
    base_linewidth=1.0,
    linewidth_progression_factor=1.3
)

fig, ax = plt.subplots(figsize=(3.5, 2.6))  # Single column

for i in range(4):
    plt.plot_styled(x, data[i], color_idx=i,
                   centerline=True, label=labels[i])

plt.setup_axis(xlabel='Time (s)', ylabel='Amplitude (a.u.)')
plt.legend()
plt.savefig('figure1.pdf', dpi=300)
```

**Nature Requirements:**
- Fonts: Arial (sans-serif)
- Font sizes: 7-9pt
- Single column: 89mm (3.5")
- Double column: 183mm (7.2")
- Max height: 247mm (9.7")
- Resolution: 300+ DPI

### Presentation

```python
apply_style_preset('presentation')

plt.initialize_style(
    vary_linewidth=True,
    base_linewidth=3.0,
    linewidth_progression_factor=1.3
)

fig, ax = plt.subplots(figsize=(10, 6))

for i in range(3):
    plt.plot_styled(x, data[i], color_idx=i,
                   outline=True, label=labels[i])

plt.setup_axis(xlabel='X', ylabel='Y', title='Results', grid=True)
plt.legend(fontsize=16)
plt.savefig('slide.pdf')
```

### Poster

```python
apply_style_preset('poster')

plt.initialize_style(
    vary_linewidth=True,
    base_linewidth=4.0,
    linewidth_progression_factor=1.2  # Gentle for visibility
)

fig, ax = plt.subplots(figsize=(12, 8))

for i in range(4):
    plt.plot_styled(x, data[i], color_idx=i,
                   outline=True, centerline=True, label=labels[i])

plt.setup_axis(xlabel='X', ylabel='Y', title='Key Results')
plt.legend(fontsize=20)
plt.savefig('poster_figure.pdf')
```

---

## Colorblind Accessibility

### Understanding the Problem

Color vision deficiency affects:
- **8%** of males
- **0.5%** of females

Types:
- **Protanopia** (red-blind)
- **Deuteranopia** (green-blind)
- **Tritanopia** (blue-blind)
- **Monochromacy** (complete colorblindness)

Standard plots using only color fail for these viewers.

### The Progressive Width Solution

Each line gets progressively thicker using exponential progression:

```
width(n) = base_linewidth x (progression_factor^n)
```

**Example with factor=1.3:**
- Line 0: 2.0 x 1.3^0 = 2.00pt
- Line 1: 2.0 x 1.3^1 = 2.60pt
- Line 2: 2.0 x 1.3^2 = 3.38pt
- Line 3: 2.0 x 1.3^3 = 4.39pt
- Line 4: 2.0 x 1.3^4 = 5.71pt

### Choosing Factors

#### Factor 1.2 (Gentle - 20% increase)
```python
linewidth_progression_factor=1.2
```
- **Best for:** 8-10 lines
- **Effect:** Subtle thickness variation
- **Widths:** 2.0 -> 2.4 -> 2.9 -> 3.5 -> 4.2pt

#### Factor 1.3 (Moderate - 30% increase) [DEFAULT]
```python
linewidth_progression_factor=1.3
```
- **Best for:** 4-6 lines
- **Effect:** Clear thickness variation
- **Widths:** 2.0 -> 2.6 -> 3.4 -> 4.4 -> 5.7pt

#### Factor 1.5 (Strong - 50% increase)
```python
linewidth_progression_factor=1.5
```
- **Best for:** 2-4 lines
- **Effect:** Very pronounced variation
- **Widths:** 2.0 -> 3.0 -> 4.5 -> 6.8 -> 10.1pt

### Testing for Colorblindness

1. **Grayscale Test:**
   ```bash
   convert plot.pdf -colorspace Gray plot_gray.pdf
   ```

2. **Online Simulators:**
   - Coblis (Color Blindness Simulator)
   - Color Oracle
   - Photoshop colorblind filters

3. **Ask for Feedback:** Get input from colorblind colleagues

### Best Practices

**DO:**
- Enable `vary_linewidth=True` by default
- Choose factor based on number of lines
- Test in grayscale
- Combine with centerlines for maximum accessibility

**DON'T:**
- Use very high factors (>1.6)
- Use with too many lines (>10)
- Rely on color alone

---

## Examples

### Example 1: Basic Multi-Line Plot

```python
import pltx.pyplot as plt
import numpy as np

# Enable colorblind-friendly widths
plt.initialize_style(
    palette_name='viridis',
    vary_linewidth=True,
    base_linewidth=2.0,
    linewidth_progression_factor=1.3
)

# Generate data
x = np.linspace(0, 10, 100)

# Plot multiple lines
for i in range(5):
    y = np.sin(x + i * 0.5)
    plt.plot_styled(x, y, color_idx=i, label=f'Dataset {i+1}')

plt.setup_axis(xlabel='Time (s)', ylabel='Amplitude', grid=True)
plt.legend()
plt.savefig('example1.pdf', dpi=300)
```

### Example 2: With Centerlines

```python
plt.initialize_style(
    vary_linewidth=True,
    linewidth_progression_factor=1.3
)

for i in range(5):
    plt.plot_styled(
        x, y[i],
        color_idx=i,
        centerline=True,      # Add thin line on top
        centerline_width=0.7,
        label=f'Line {i+1}'
    )

plt.legend()
plt.savefig('example2.pdf')
```

### Example 3: Bar Plot with pltx Colors

```python
from pltx.colors import get_color

categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

# Get colors from palette
colors = [get_color(i) for i in range(len(categories))]

plt.bar(categories, values, color=colors, edgecolor='black', linewidth=1)
plt.xlabel('Category')
plt.ylabel('Value')
plt.savefig('bar_plot.pdf')
```

### Example 4: Maximum Accessibility

```python
# Combine ALL features
plt.initialize_style(
    vary_linewidth=True,
    base_linewidth=2.0,
    linewidth_progression_factor=1.3
)

for i in range(4):
    plt.plot_styled(
        x, y[i],
        color_idx=i,
        outline=True,          # Halo effect
        outline_width=5,
        centerline=True,       # Top line
        centerline_width=0.8,
        label=labels[i]
    )

plt.setup_axis(xlabel='x', ylabel='y', grid=True)
plt.legend()
plt.savefig('maximum_accessibility.pdf')
```

### Example 5: Nature Journal Figure

```python
from pltx.rcparams import apply_style_preset

# Apply Nature preset
apply_style_preset('nature')

plt.initialize_style(
    vary_linewidth=True,
    base_linewidth=1.0,
    linewidth_progression_factor=1.3,
    palette_name='viridis'
)

# Single column figure
fig, ax = plt.subplots(figsize=(3.5, 2.6))

for i, (data, label) in enumerate(zip(datasets, labels)):
    plt.plot_styled(
        x, data,
        color_idx=i,
        centerline=True,  # Better in print
        centerline_width=0.5,
        label=label
    )

plt.setup_axis(xlabel='Time (s)', ylabel='Amplitude (a.u.)')
plt.legend(fontsize=7)
plt.savefig('nature_figure.pdf', dpi=300)
```

### Example 6: Multi-Panel Plot

```python
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6, 8))

# Panel 1: Main data
for i in range(3):
    plt.plot_styled(x, data[i], color_idx=i,
                   label=labels[i], ax=ax1)
plt.setup_axis(ylabel='Signal', ax=ax1)
ax1.legend()

# Panel 2: Error
plt.plot_styled(x, errors, color_idx=0, ax=ax2)
plt.add_reference_line(horizontal=threshold, ax=ax2)
plt.setup_axis(ylabel='Error', yscale='log', ax=ax2)

# Panel 3: Residuals
plt.plot_styled(x, residuals, color_idx=3, ax=ax3)
plt.setup_axis(xlabel='Time (s)', ylabel='Residuals', ax=ax3)

plt.tight_layout()
plt.savefig('multi_panel.pdf')
```

---

## Best Practices

### General

1. **Always enable progressive width** for multi-line plots:
   ```python
   plt.initialize_style(vary_linewidth=True)
   ```

2. **Choose appropriate factors:**
   - 2-4 lines: factor=1.5
   - 4-6 lines: factor=1.3 (default)
   - 7-10 lines: factor=1.2

3. **Test in grayscale** to verify accessibility

4. **Use style presets** to match your target medium

5. **Combine features** when needed (outline + centerline)

### Line Enhancement Guidelines

| Scenario | Recommendation |
|----------|---------------|
| Clean publication figure | Centerline only |
| Busy plot/background | Outline only |
| Maximum visibility needed | Both outline + centerline |
| Colorblind accessibility | Progressive width |
| Presentation slide | Outline + progressive width |
| Nature journal | Centerline + progressive width |

### Color Palette Selection

**Sequential palettes** (continuous data):
- `'viridis'`, `'plasma_r'`, `'mako_r'`, `'crest'`

**Diverging palettes** (data with midpoint):
- `'coolwarm'`, `'RdBu_r'`, `'vlag'`

**Categorical palettes** (distinct categories):
- `'tab10'`, `'Set2'`, `'Paired'`

### Font Size Guidelines

| Medium | Font Size | Line Width |
|--------|-----------|------------|
| Nature journal | 7-9pt | 1.0pt |
| Other journals | 8-10pt | 1.5pt |
| Presentation | 16-18pt | 3pt |
| Poster | 24-28pt | 4pt |

---

## Migration Guide

### From qedft.utils.plot

```python
# Old code
from qedft.utils.plot import PlotStyle
style = PlotStyle(palette_name="plasma_r", palette_size=10)
style.plot_curve(ax, x, y, color_idx=0)
style.setup_axis(ax, xlabel='x', ylabel='y')

# New code (same API + new features)
from pltx import PlotStyle
style = PlotStyle(
    palette_name="plasma_r",
    palette_size=10,
    vary_linewidth=True  # NEW: colorblind friendly
)
style.plot_curve(ax, x, y, color_idx=0, centerline=True)  # NEW
style.setup_axis(ax, xlabel='x', ylabel='y')

# Or use enhanced pyplot interface
import pltx.pyplot as plt
plt.initialize_style(vary_linewidth=True)
plt.plot_styled(x, y, color_idx=0, centerline=True)
```

### From Standard Matplotlib

```python
# Old matplotlib code
import matplotlib.pyplot as plt
plt.plot(x, y1, color='red', linewidth=2, label='Line 1')
plt.plot(x, y2, color='blue', linewidth=2, label='Line 2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# New pltx code
import pltx.pyplot as plt
plt.initialize_style(vary_linewidth=True)  # Enable accessibility
plt.plot_styled(x, y1, color_idx=0, label='Line 1')
plt.plot_styled(x, y2, color_idx=2, label='Line 2')
plt.setup_axis(xlabel='x', ylabel='y')
plt.legend()
```

---

## Troubleshooting

### Import Errors

```python
# If you get "ModuleNotFoundError: No module named 'pltx'"
import sys
sys.path.insert(0, '/path/to/pltx')
import pltx.pyplot as plt
```

### Seaborn Not Found

pltx works without seaborn - it falls back to matplotlib colormaps. For extended palette support:
```bash
pip install seaborn
```

### Lines Too Thick

Reduce the progression factor or base width:
```python
plt.initialize_style(
    vary_linewidth=True,
    base_linewidth=1.5,  # Smaller base
    linewidth_progression_factor=1.2  # Gentler increase
)
```

### Colors Not Matching

Ensure you're using the same palette consistently:
```python
plt.initialize_style(palette_name='viridis')  # Set once
```

---

## Package Structure

```
pltx/
|-- __init__.py                      # Main interface
|-- colors.py                        # Color palettes & utilities
|-- pyplot.py                        # Enhanced pyplot interface
|-- rcparams.py                      # Style presets
|-- style.py                         # PlotStyle class
|-- pyproject.toml                   # Modern package configuration
|-- README.md                        # Quick reference
|-- FULL_DOCUMENTATION.md            # Complete documentation (this file)
\-- examples/
    |-- 01_basic_usage.py            # Basic plotting introduction
    |-- 02_color_palettes.py         # Palette switching
    |-- 03_advanced_panels.py        # Multi-panel setups
    |-- 04_color_cycling.py          # Auto-color demonstration
    |-- 05_direct_style_usage.py     # Class-based usage
    |-- paper_plot_nature.py         # Publication-ready blueprint
    |-- paper_plot_subplots.py       # Mixed-type subplots
    \-- paper_plot_localized_style.py # Context manager example
```

---

## Feature Matrix

| Feature | Standard matplotlib | pltx |
|---------|-------------------|------|
| Colorblind accessible | Manual implementation | `vary_linewidth=True` |
| Line visibility | Complex manual code | `outline=True`, `centerline=True` |
| Journal compliance | Research and implement | `apply_style_preset('nature')` |
| Color palettes | Manual setup | Automatic with `color_idx` |
| Axis configuration | Multiple function calls | Single `setup_axis()` |
| Width variation | Manual for each line | Automatic exponential progression |
| Type hints | Partial | Complete |

---

## Credits

**Author:** Igor Sokolov
**Version:** 0.1.0
**Python:** 3.10+
**Author:** Igor Sokolov
**Created:** 2026-01-09
