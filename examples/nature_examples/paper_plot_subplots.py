"""Example showing multiple plot types (bars and lines) with pltx for a paper."""
import os
import sys
import numpy as np

# Enable local package import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pltx.pyplot as plt

# Generate data
categories = ['A', 'B', 'C', 'D']
v1 = [4, 7, 3, 8]
v2 = [5, 6, 4, 7]
x = np.linspace(0, 3, 100)

plt.initialize_style(vary_linewidth=True)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(4, 6))

# Panel 1: Categorical data
plt.bar_styled(categories, v1, label="Group 1", ax=ax1)
plt.bar_styled(categories, v2, label="Group 2", ax=ax1, alpha=0.5)
plt.setup_axis(ylabel="Metrics", ax=ax1)
ax1.legend()

# Panel 2: Continuous data with auto-cycling and progressive width
for i in range(3):
    plt.plot_styled(x, np.exp(-x*i), label=f"Fit {i+1}", ax=ax2)

plt.setup_axis(xlabel="Distance (nm)", ylabel="Intensity", ax=ax2)
ax2.legend()

plt.tight_layout()
plt.savefig("paper_multi_type.pdf")
print("Saved paper_multi_type.pdf")
