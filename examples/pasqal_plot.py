import pltx.pyplot as plt
import numpy as np

# Enable colorblind-friendly progressive widths
plt.initialize_style(
    palette_name='pasqal',
    vary_linewidth=True,              # Lines get progressively thicker
    linewidth_progression_factor=1.3  # 30% increase per line
)

# Plot with automatic styling
x = np.linspace(0, 10, 100)
for i in range(5):
    plt.plot_styled(x, np.sin(x + i*0.5),
                   color_idx=i,
                   centerline=False,  # Add thin line on top
                   label=f'Line {i+1}')

plt.setup_axis(xlabel='x', ylabel='y', grid=True)
plt.legend()
plt.savefig('plot.pdf', dpi=300)