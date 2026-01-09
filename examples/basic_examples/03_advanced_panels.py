"""Example 03: Advanced multi-panel plotting with shared axes and error regions."""

import sys
import os
import numpy as np

# Add parent directory to path to enable local package import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import pltx.pyplot as plt

# Reset to default palette
plt.initialize_style(palette_name='plasma_r', palette_size=10)

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = 0.5 * np.cos(x)
y3 = np.exp(-0.2 * x) * np.sin(x)

# Error data
error1 = 0.05 * np.random.rand(len(x))
error2 = 0.1 * np.random.rand(len(x))

fig, axs = plt.subplots(3, sharex=False, sharey=False,
                        gridspec_kw={"height_ratios": [3, 1, 1]})
fig.set_size_inches(5, 7)

xlim = (0, 10)

# Plot 1: Main curves
plt.setup_axis(xlim=xlim, ylim=(-1.2, 1.2),
              ylabel="Signal", xtick_spacing=2.0, ax=axs[0])

plt.plot_styled(x, y1, label="Sine", color_idx=1, linewidth=3, ax=axs[0])
plt.plot_styled(x, y2, label="Cosine", color_idx=1,
               color_intensity=0.5, linewidth=2, ax=axs[0])
plt.plot_styled(x, y3, label="Damped", color="gray",
               linestyle="-.", ax=axs[0])

# Add reference points
reference_points = [2, 5, 8]
ref_idx = [np.argmin(np.abs(x - p)) for p in reference_points]
plt.plot_styled(x[ref_idx], y1[ref_idx], label="Reference",
               color="black", marker="o", markersize=5,
               linestyle="", ax=axs[0])

axs[0].legend(bbox_to_anchor=(1.0, 0.8), framealpha=0.5, frameon=False)

# Plot 2: Error Analysis 1
plt.setup_axis(xlim=xlim, ylim=(0.001, 0.2),
              ylabel="Error 1", yscale="log", xtick_spacing=2.0, ax=axs[1])
plt.plot_styled(x, error1 + 0.01, color_idx=1, linewidth=2, ax=axs[1])
plt.add_reference_line(horizontal=0.03, ax=axs[1])
plt.add_highlight_region(ymin=0, ymax=0.03, label="Threshold", ax=axs[1])
plt.add_reference_line(vertical=reference_points, ax=axs[1])

# Plot 3: Error Analysis 2
plt.setup_axis(xlim=xlim, ylim=(0.01, 0.3),
              ylabel="Error 2", xlabel="X-axis",
              yscale="log", xtick_spacing=2.0, ax=axs[2])
plt.plot_styled(x, error2 + 0.02, color_idx=3, linewidth=2, ax=axs[2])
plt.add_reference_line(vertical=reference_points, ax=axs[2])

fig.tight_layout()
plt.savefig('03_advanced_panels.pdf')
print("Saved: 03_advanced_panels.pdf")
