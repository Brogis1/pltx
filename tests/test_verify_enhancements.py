import os
import sys
import numpy as np
import matplotlib.pyplot as plt

# Insert parent directory to enable package import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pltx.pyplot as pltx

def test_auto_cycling():
    print("Testing auto-cycling...")
    pltx.reset_color_cycle()
    x = np.linspace(0, 10, 10)
    for i in range(3):
        line = pltx.plot_styled(x, x + i, label=f"Line {i}")
        print(f"  Line {i} color: {line.get_color()}")
    print("Auto-cycling OK")

def test_context_manager():
    print("Testing context manager...")
    # Default style is already initialized in pltx.pyplot
    with pltx.style_context("nature"):
        print(f"  Nature font size: {plt.rcParams['font.size']}")
        assert plt.rcParams['font.size'] == 8

    print(f"  Back to default font size: {plt.rcParams['font.size']}")
    # Reset to default might be needed if initialize_style was called before
    print("Context manager OK")

def test_new_plot_types():
    print("Testing new plot types...")
    x = np.arange(5)
    y = np.array([2, 4, 3, 5, 1])

    print("  Testing bar_styled...")
    pltx.bar_styled(x, y, label="Bars")

    print("  Testing hist_styled...")
    pltx.hist_styled(np.random.randn(100), bins=10, label="Hist")

    print("  Testing errorbar_styled...")
    pltx.errorbar_styled(x, y, yerr=0.5, label="Errors")

    print("New plot types OK")

if __name__ == "__main__":
    try:
        test_auto_cycling()
        test_context_manager()
        test_new_plot_types()
        print("\nALL VERIFICATIONS PASSED!")
    except Exception as e:
        print(f"\nVERIFICATION FAILED: {e}")
        sys.exit(1)
