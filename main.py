"""
Plot SSP projector topomaps for raw data.

This app loads raw MEG/EEG data and plots its SSP projectors as
topomaps via mne.io.Raw.plot_projs_topomap.

Inputs:
    - mne: Path to MNE raw .fif file
    - ch_type, sensors, show_names, contours, outlines, sphere,
      image_interp, extrapolate, border, res, size, cmap, vlim, cnorm,
      colorbar, cbar_fmt, units: Parameters forwarded to
      Raw.plot_projs_topomap

Outputs:
    - out_figs/projs_topomap.png: Projector topomap plot
    - product.json: Metadata about the plotted projectors
"""

# Copyright (c) 2026 brainlife.io

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'brainlife_utils'))

# Standard imports
import mne

# Import shared utilities
from brainlife_utils import (
    load_config,
    setup_matplotlib_backend,
    ensure_output_dirs,
    create_product_json,
    add_info_to_product,
    add_image_to_product,
    require_config_keys
)

# Set up matplotlib for headless execution
setup_matplotlib_backend()

# Ensure output directories exist
ensure_output_dirs('out_figs')

# Load configuration
config = load_config()
require_config_keys(config, ['mne'])

data_file = config['mne']

raw = mne.io.read_raw_fif(data_file, verbose=False)

fig = raw.plot_projs_topomap(ch_type=config['ch_type'],
sensors=config['sensors'],
show_names=config['show_names'],
contours=config['contours'],
outlines=config['outlines'],
sphere=config['sphere'],
image_interp=config['image_interp'],
extrapolate=config['extrapolate'],
border=config['border'],
res=config['res'],
size=config['size'],
cmap=config['cmap'],
vlim=config['vlim'],
cnorm=config['cnorm'],
colorbar=config['colorbar'],
cbar_fmt=config['cbar_fmt'],
units=config['units'],
show=False)

# == SAVE FIGURE ==
fig_path = os.path.join('out_figs', 'projs_topomap.png')
fig.savefig(fig_path)

# == CREATE PRODUCT.JSON ==
product_items = []
add_info_to_product(product_items, 'Plotted projector topomaps', 'success')
add_image_to_product(product_items, 'Projector topomaps', filepath=fig_path)
create_product_json(product_items)
