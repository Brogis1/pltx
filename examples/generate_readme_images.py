import sys
import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as mpl_plt

# Make sure we can import pltx from the repo root
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

import pltx.pyplot as plt
from pltx.cmap import register_pasqal_cmap

PASQAL_CMAPS = ['pasqal', 'pasqal_contrast', 'pasqal_diverging']


def generate_images():
    # Register the colormaps
    print("Registering Pasqal colormaps...")
    register_pasqal_cmap()

    # Seed for reproducibility
    np.random.seed(42)

    # Create the img directory if it doesn't exist
    os.makedirs('img', exist_ok=True)

    # 1. Generate the Heatmap Comparison
    print("Generating img/pasqal_heatmaps.png...")
    grid_x, grid_y = np.meshgrid(np.linspace(-3, 3, 200), np.linspace(-3, 3, 200))
    Z = np.exp(-(grid_x**2 + grid_y**2) / 2) * np.cos(2 * grid_x) * np.cos(2 * grid_y)

    fig, axes = mpl_plt.subplots(1, 3, figsize=(16, 5))
    for ax, cmap_name in zip(axes, PASQAL_CMAPS):
        im = ax.imshow(Z, cmap=cmap_name, origin='lower',
                       extent=[-3, 3, -3, 3], aspect='equal')
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        plt.setup_axis(ax, xlabel='x', ylabel='y', title=cmap_name)

    fig.suptitle('Pasqal Colourmaps — Gaussian × Cosine Pattern',
                 fontsize=14, fontweight='bold')
    mpl_plt.tight_layout()
    mpl_plt.savefig('img/pasqal_heatmaps.png', dpi=150)
    mpl_plt.close()

    # 2. Generate the Swatches
    print("Generating img/pasqal_swatches.png...")
    fig, axes = mpl_plt.subplots(3, 1, figsize=(10, 3))
    for ax, name in zip(axes, PASQAL_CMAPS):
        gradient = np.linspace(0, 1, 256).reshape(1, -1)
        ax.imshow(gradient, aspect='auto', cmap=name)
        ax.set_yticks([])
        ax.set_xticks([])
        ax.set_title(name, fontsize=11, pad=4)
    mpl_plt.suptitle('Pasqal Colormap Swatches', fontsize=12, fontweight='bold', y=1.05)
    mpl_plt.tight_layout()
    mpl_plt.savefig('img/pasqal_swatches.png', dpi=150)
    mpl_plt.close()

    # 3. Generate the Sine/Cosine line plots
    print("Generating img/pasqal_sine_cosine.png...")
    x = np.linspace(0, 10, 200)
    N = 10
    fig, axes = mpl_plt.subplots(2, 3, figsize=(18, 10), sharex=True)

    for i_col, cmap_name in enumerate(PASQAL_CMAPS):
        cmap = mpl_plt.get_cmap(cmap_name)
        for i_row, func_name in enumerate(['sin', 'cos']):
            ax = axes[i_row, i_col]
            for i in range(N):
                color = cmap(i / (N-1))
                phi = i * np.pi / (N-1)
                y = np.sin(x + phi) if func_name == 'sin' else np.cos(x + phi)
                label = f'Phase {i}' if i in [0, N-1] else None
                plt.plot_styled(x, y, color=color, linewidth=2, label=label, ax=ax)

            sm = mpl_plt.cm.ScalarMappable(cmap=cmap, norm=mpl_plt.Normalize(vmin=0, vmax=1))
            cbar = fig.colorbar(sm, ax=ax, orientation='vertical', fraction=0.046, pad=0.04)
            cbar.set_label('Relative Phase shift')

            plt.setup_axis(ax,
                           ylabel=f'{func_name}(x+\u03c6)',
                           title=f'{func_name} — {cmap_name}', grid=True)
            if i_row == 1:
                ax.set_xlabel('x')

    fig.suptitle('Sampling Colors from Pasqal Colormaps', fontsize=16, fontweight='bold')
    mpl_plt.tight_layout()
    mpl_plt.savefig('img/pasqal_sine_cosine.png', dpi=150)
    mpl_plt.close()

    print("\nAll README images generated successfully in the 'img/' directory.")

if __name__ == '__main__':
    generate_images()
