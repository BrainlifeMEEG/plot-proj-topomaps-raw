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
    - product.json: Metadata about the plotted projectors

Note: this app does not currently save the generated figure(s) to
out_figs or build a product.json with an image entry - it never did,
even before this migration (no out_figs dir was created, no savefig
call existed). Persisting the plot depends on a design decision
(single figure vs. a list when ch_type is a list) that's out of scope
for a structure-only compliance pass; flagging here rather than
guessing.
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
    create_product_json,
    add_info_to_product,
    require_config_keys
)

# Set up matplotlib for headless execution
setup_matplotlib_backend()

# Load configuration
config = load_config()
require_config_keys(config, ['mne'])

data_file = config['mne']

raw = mne.io.read_raw_fif(data_file, verbose=False)

raw.plot_projs_topomap(ch_type=config['ch_type'],
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
units=config['units'])

# == CREATE PRODUCT.JSON ==
product_items = []
add_info_to_product(product_items, 'Plotted projector topomaps', 'success')
create_product_json(product_items)
