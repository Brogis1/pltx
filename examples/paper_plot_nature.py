"""Example of a standard paper-style plot using pltx."""
import os
import sys
import numpy as np

# Enable local package import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pltx.pyplot as plt

# Generate data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = 0.8 * np.sin(x + 0.5)

# 1. Apply a preset globally or locally
plt.apply_style_preset('nature')

# 2. Plot with automatic styling and color cycling
plt.plot_styled(x, y1, label="Experimental")
plt.plot_styled(x, y2, label="Theoretical", linestyle='--')

# 3. Quick axis setup
plt.setup_axis(
    xlabel="Time (ps)",
    ylabel="Amplitude (a.u.)",
    grid=True
)

plt.legend()
plt.savefig("paper_plot.pdf")
print("Saved paper_plot.pdf")
