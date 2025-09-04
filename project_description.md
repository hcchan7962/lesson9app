### Motion Data Visualizer — Project Description

**Purpose**: A Streamlit-based web UI to visualize multi-channel time-domain motion data (e.g., Command, Encoder, Current, Velocity, Torque). Designed for rapid exploration, comparison, and export of plots and tabular data.

**Current State (Mock Only)**:
- UI scaffold planned (no parsing, plotting, or data logic yet).
- All controls are placeholders to validate layout and UX.

### UI Layout

- **Sidebar**
  - Data: multi-file upload placeholder (csv/tsv/txt), dataset selector.
  - Plot: plot type (Line/Scatter/Area), X column (time), Y columns multiselect, layout mode, color scheme.
  - Filters: time window slider, Y range slider, smoothing toggle, markers toggle.
  - Export: buttons for downloading plot (PNG) and data (CSV).

- **Main Content**
  - Tabs: Overview | Plot | Table | About
  - Overview: KPI placeholders (Samples, Duration, Channels, Sampling Rate) and summary info.
  - Plot: title, legend/grid/theme/line width controls, large chart placeholder.
  - Table: quick filters and empty dataframe placeholder.
  - About: brief help and scope note.

### Intended Features (Roadmap Targets)
- File ingest: CSV/TSV with flexible delimiters, column detection, units.
- Data processing: resampling, smoothing, detrending, normalization, alignment.
- Plotting: overlay/stacked/subplots, multi-axis, themes, export to PNG/SVG.
- Table: column filters, search, conditional presets.
- Performance: lazy loading, caching, chunked parsing for large logs.
- Persistence: session-based selections, optional presets.
- Extensibility: plugin hooks for custom channels and derived signals.

### How to Run (when logic is added)
- Install Streamlit and deps, then:
- `streamlit run main.py`
- Open the provided local URL in a browser.

### ASCII Wireframe (Reference)
```
+--------------------------------------------------------------------------------------+
|                               Motion Data Visualizer                                 |
|                         Mock UI (no backend logic yet)                               |
+--------------------------------------------------------------------------------------+
| Sidebar                                                                              |
|  - Data: upload files, dataset selector                                              |
|  - Plot: plot type, x/y columns, layout, colors                                     |
|  - Filters: time window, y range, smoothing, markers                                 |
|  - Export: download plot/data                                                        |
|--------------------------------------------------------------------------------------|
| Main                                                                                 |
|  Tabs: [ Overview ] [ Plot ] [ Table ] [ About ]                                     |
|  Overview: KPI cards + summary                                                       |
|  Plot: title/legend/grid/theme/line width + chart placeholder                        |
|  Table: quick filters + empty dataframe                                              |
|  About: help and scope                                                               |
+--------------------------------------------------------------------------------------+
```

### Notes
- This is a mock interface to validate structure and ergonomics.
- Functional logic (parsing, plotting, filtering, exports) will be implemented after approval.



