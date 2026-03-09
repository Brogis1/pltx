"""pltx - Enhanced Matplotlib for Scientific Visualization."""

__version__ = "0.1.3"

# Auto-register pasqal colormaps on import
from .cmap import register_pasqal_cmap as _register_pasqal_cmap
_register_pasqal_cmap()
del _register_pasqal_cmap
