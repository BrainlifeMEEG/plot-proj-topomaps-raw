# Plot Projector Topomaps for Raw Data

[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.740-blue.svg)](https://doi.org/10.25663/brainlife.app.740)

## Description

This Brainlife.io application plots the SSP (Signal Space Projection) projectors stored in a
continuous MEG/EEG raw file as scalp topomaps, using
[`mne.io.Raw.plot_projs_topomap`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.plot_projs_topomap).
It is a quality-control step that lets a user visually inspect the spatial pattern of each
projector (e.g. ECG/EOG SSP vectors) computed earlier in a pipeline, before deciding whether to
apply them to the data.

The app generates:
- A topomap figure of the raw file's SSP projectors
- `product.json` metadata including the topomap image

## Inputs

- **`mne`** (`neuro/meeg/mne/raw`): continuous MEG/EEG raw data file containing the SSP
  projectors to plot (required)

## Outputs

- `out_figs/projs_topomap.png`: topomap plot of the projectors found in the raw file
- `product.json`: metadata about the plotted projectors, including the figure

## Configuration Parameters

| key | type | default | description |
|---|---|---|---|
| `ch_type` | string | `None` | `'mag'` \| `'grad'` \| `'planar1'` \| `'planar2'` \| `'eeg'` \| `None`. The channel type to plot. For `'grad'`, gradiometers are collected in pairs and the RMS for each pair is plotted. If `None`, all channel types present are plotted. |
| `sensors` | boolean | `true` | Whether to add markers for sensor locations. If `True` (the default), black circles are used. |
| `show_names` | boolean | `false` | If `True`, show channel names next to each sensor marker. |
| `contours` | number | `6` | The number of contour lines to draw. If `0`, no contours are drawn. |
| `outlines` | string | `"head"` | `'head'` \| `None`. If `'head'`, the default head scheme is drawn. If `None`, nothing is drawn. |
| `sphere` | string | `None` | Sphere parameters used for the head outline. `None` (the default) is equivalent to `'auto'`. |
| `image_interp` | string | `"cubic"` | `'cubic'` \| `'nearest'` \| `'linear'`. Interpolation method for the topomap image. |
| `extrapolate` | string | `"auto"` | `'box'` \| `'local'` \| `'head'` \| `'auto'`. How far to extrapolate the topomap image beyond the sensor locations. |
| `border` | string | `"mean"` | Value to extrapolate to on the topomap borders. If `'mean'` (default), each extrapolated point gets the average value of its neighbours. |
| `res` | number | `64` | The resolution of the topomap image (number of pixels along each side). |
| `size` | number | `1` | Side length of each subplot in inches. Only applies when plotting multiple topomaps at once. |
| `cmap` | string | `None` | Colormap to use. If `None`, `'Reds'` is used for all-positive/all-negative data, `'RdBu_r'` otherwise. |
| `vlim` | string | `"joint"` | Colormap limits. If `'joint'`, limits are computed jointly across all projectors of the same channel type. |
| `cnorm` | string | `None` | Colormap normalization to use (overrides `vlim` if set). `None` uses a linear normalization. |
| `colorbar` | boolean | `true` | Plot a colorbar in the rightmost column of the figure. |
| `cbar_fmt` | string | `"%3.1f"` | Formatting string for colorbar tick labels. |
| `units` | string | `None` | Units to use for the colorbar label. If `None`, the label is `"AU"` (arbitrary units). Ignored if `colorbar` is `False`. |

## Usage

### Running on Brainlife.io

1. Upload or select your continuous MEG/EEG raw data file (`.fif`) containing SSP projectors
2. Select the plot-proj-topomaps-raw app
3. Optionally adjust the plotting parameters listed above (channel type, extrapolation,
   color limits, etc.)
4. Submit the task
5. Review the projector topomap figure in the output viewer

### Local Testing

```bash
# Update config.json with your raw .fif file path and desired plotting parameters
# Then run:
./main
```

## Technical Details

The Brainlife.io registration for this app (DOI `bl.app.740`, "Plot all projectors") currently
runs [`dnacombo/app-plot_proj_topomaps-raw@master`](https://github.com/dnacombo/app-plot_proj_topomaps-raw),
a different repository from this one, and its `config` does not yet expose the `cnorm`,
`image_interp` and `size` parameters that this repo's `main.py` reads. Until the registration is
updated to point at this repo/branch, those three parameters can only be set by editing
`config.json` directly (local testing), not through the Brainlife.io web UI.

## Authors

- Maximilien Chaumon (https://github.com/dnacombo)

## Citations

- Hayashi, S., Caron, B.A., Heinsfeld, A.S. et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. Nat Methods 21, 809–813 (2024). https://doi.org/10.1038/s41592-024-02237-2
- Gramfort, A. et al. MEG and EEG data analysis with MNE-Python. Front. Neurosci. 7, 267 (2013). https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement

brainlife.io is publicly funded. We kindly ask that you acknowledge the funding below in your code and publications.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)

## License

Copyright (c) 2026 MEEG Brainlife team. Licensed under AGPL-3.0, see [license.txt](license.txt).
