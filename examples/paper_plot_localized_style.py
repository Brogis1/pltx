"""Example using the style context manager for localized styling."""
import os
import sys
import numpy as np

# Enable local package import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pltx.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Figure 1: Default style
plt.figure()
plt.plot_styled(x, y, label="Default")
plt.setup_axis(title="Default Style")
plt.legend()

# Figure 2: Temporary Nature style using context manager
# This is perfect for when you want one figure in Nature style
# without affecting the global plotting state of your script.
with plt.style_context('nature'):
    plt.figure()
    plt.plot_styled(x, y, label="Nature Style", color_idx=2)
    plt.setup_axis(title="Nature Style (localized)")
    plt.legend()
    plt.savefig("paper_nature_figure.pdf")

print("Generated figures. Nature-styled saved to paper_nature_figure.pdf")
