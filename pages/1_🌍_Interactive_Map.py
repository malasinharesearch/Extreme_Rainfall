import streamlit as st
import leafmap.foliumap as leafmap

# ----------------------------------
# Page configuration
# ----------------------------------
st.set_page_config(layout="wide")

# ----------------------------------
# Sidebar
# ----------------------------------
st.sidebar.title("🌍 Interactive Climate Map")

st.sidebar.info(
    """
    **Extreme Rainfall & Water Vapour Explorer**

    This interactive map allows users to explore
    geographical regions relevant to extreme rainfall
    and atmospheric moisture studies.

    Use this page to:
    • Navigate to regions of interest  
    • Change climate-relevant basemaps  
    • Prepare spatial context for rainfall & moisture analysis  
    """
)

# ----------------------------------
# Main title
# ----------------------------------
st.title("🌍 Interactive Map: Extreme Rainfall & Water Vapour Context")

st.markdown(
    """
    This interactive map provides spatial context for analyzing
    extreme rainfall events and associated atmospheric water vapour
    conditions. Users can explore different regions and basemaps
    before applying advanced analytical layers.
    """
)

# ----------------------------------
# Layout
# ----------------------------------
col1, col2 = st.columns([4, 1])

# ----------------------------------
# Basemap selector (climate friendly)
# ----------------------------------
options = [
    "CartoDB dark_matter",
    "OpenTopoMap",
    "Esri.WorldImagery",
    "Stamen.Terrain",
    "CartoDB positron",
]

with col2:
    basemap = st.selectbox("🗺️ Select basemap", options, index=0)

# ----------------------------------
# Map view (India-focused by default)
# ----------------------------------
with col1:
    m = leafmap.Map(
        center=[22.5, 80.0],  # India-centered (change later if needed)
        zoom=4,
        locate_control=True,
        latlon_control=True,
        draw_export=True,
        minimap_control=True,
    )

    m.add_basemap(basemap)
    m.to_streamlit(height=700)
