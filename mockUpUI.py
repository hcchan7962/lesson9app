import streamlit as st


st.set_page_config(page_title="Motion Data Visualizer (Mock)", layout="wide")

# ----- Sidebar -----
with st.sidebar:
    st.title("Controls")
    st.caption("Upload data and configure the view (mock only).")

    st.subheader("Data")
    st.file_uploader(
        "Upload time-domain files",
        type=["csv", "tsv", "txt"],
        accept_multiple_files=True,
        help="Multiple files allowed. Parsing not implemented.",
    )
    st.selectbox(
        "Select dataset",
        options=["— None —", "Mock Dataset A", "Mock Dataset B"],
        index=0,
    )
    st.divider()

    st.subheader("Plot")
    st.radio("Plot type", ["Line", "Scatter", "Area"], horizontal=True)
    st.selectbox("X (time)", options=["time"], index=0)
    st.multiselect(
        "Y columns",
        ["Command", "Encoder", "Current", "Velocity", "Torque"],
        default=["Command", "Encoder"],
    )
    st.selectbox("Layout", ["Overlay", "Stacked", "Subplots"], index=0)
    st.selectbox("Color scheme", ["Auto", "Category10", "Viridis", "Plasma"], index=0)
    st.divider()

    st.subheader("Filters")
    st.slider("Time window (s)", min_value=0.0, max_value=60.0, value=(0.0, 10.0), step=0.1)
    st.slider("Y range (auto if unchanged)", min_value=-100.0, max_value=100.0, value=(-100.0, 100.0), step=1.0)
    st.checkbox("Apply smoothing", value=False)
    st.checkbox("Show markers", value=False)
    st.divider()

    st.subheader("Export")
    st.button("Download Plot (PNG)")
    st.button("Download Data (CSV)")


# ----- Main Content -----
st.title("Motion Data Visualizer")
st.caption("Mock UI for time-domain multi-channel visualization. No backend logic yet.")

tabs = st.tabs(["Overview", "Plot", "Table", "About"])

with tabs[0]:
    st.subheader("Overview")
    kpi_cols = st.columns(4)
    with kpi_cols[0]:
        st.metric("Samples", "—")
    with kpi_cols[1]:
        st.metric("Duration (s)", "—")
    with kpi_cols[2]:
        st.metric("Channels", "—")
    with kpi_cols[3]:
        st.metric("Sampling Rate (Hz)", "—")

    st.markdown("#### Summary")
    st.info("No dataset loaded. KPIs and summary will populate after parsing is implemented.")

with tabs[1]:
    st.subheader("Plot")
    ctrl_cols = st.columns([2, 1, 1, 1, 1])
    with ctrl_cols[0]:
        st.text_input("Title", value="Time Series")
    with ctrl_cols[1]:
        st.checkbox("Legend", value=True)
    with ctrl_cols[2]:
        st.checkbox("Grid", value=True)
    with ctrl_cols[3]:
        st.selectbox("Theme", ["Light", "Dark"], index=0)
    with ctrl_cols[4]:
        st.selectbox("Line Width", [1, 2, 3, 4], index=1)

    st.empty()
    st.warning("Plot will render here once data and logic are implemented.")

with tabs[2]:
    st.subheader("Table")
    filter_cols = st.columns([1, 1, 2, 2])
    with filter_cols[0]:
        st.text_input("Search column", placeholder="e.g., Encoder")
    with filter_cols[1]:
        st.text_input("Operator", placeholder=">, <, ==, contains")
    with filter_cols[2]:
        st.text_input("Value", placeholder="e.g., 0.1")
    with filter_cols[3]:
        st.selectbox("Preset filter", ["None", "Non-zero Current", "Saturated Torque", "Command≠Encoder"], index=0)

    st.dataframe(
        data={"time": [], "Command": [], "Encoder": [], "Current": []},
        use_container_width=True,
        hide_index=True,
    )
    st.info("Table will populate after file parsing is implemented.")

with tabs[3]:
    st.subheader("About")
    st.markdown(
        """
This is a mock interface for motion data visualization:
- Upload time-domain logs with multiple channels (e.g., Command, Encoder, Current).
- Configure plot types, layout, and filters.
- View KPIs, plots, and data table.

Functionality will be added later.
        """
    )


