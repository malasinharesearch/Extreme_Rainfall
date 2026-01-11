import streamlit as st
import leafmap.foliumap as leafmap

# ----------------------------------
# Page configuration
# ----------------------------------
st.set_page_config(
    page_title="Extreme Rainfall & Water Vapour",
    page_icon="💧",
    layout="wide",
)

# ----------------------------------
# Sidebar
# ----------------------------------
st.sidebar.title("💧 About This App")

st.sidebar.info(
    """
    **Extreme Rainfall and Atmospheric Water Vapour Analysis**

    This application focuses on understanding the role of
    atmospheric water vapour in driving extreme rainfall events.

    **Research Focus**
    • Extreme rainfall events  
    • Atmospheric moisture (TCWV)  
    • Spatial hotspot analysis  
    • Flood and climate extremes  

    Developed for academic and research use.
    """
)

# ----------------------------------
# Main Title
# ----------------------------------
st.title("💧 Extreme Rainfall and Atmospheric Water Vapour")

st.markdown(
    """
    ### 🌧️ Scientific Motivation

    Extreme rainfall events are among the most destructive hydro-meteorological hazards. A key physical driver of such extremes is the 
    **availability and transport of atmospheric water vapour**.
    
    This application is designed to explore how
    **moisture-rich atmospheric conditions influence the
    intensity and spatial distribution of extreme rainfall**.
    """
)

# ----------------------------------
# Objectives
# ----------------------------------
st.subheader("🎯 Objectives")

st.markdown(
    """
    • Identify spatial hotspots of extreme rainfall  
    • Examine atmospheric water vapour conditions during extreme events  
    • Explore rainfall–water vapour relationships  
    • Support flood hazard and climate extreme studies  
    """
)

# ----------------------------------
# Navigation guide
# ----------------------------------
st.subheader("🧭 How to Use This Application")

st.markdown(
    """
    Use the navigation menu on the left to explore:

    • **Interactive Maps** – spatial exploration  
    • **Extreme Rainfall Heatmap** – rainfall intensity patterns  
    • **Water Vapour Analysis** – moisture-driven extremes  
    • **Basemaps & WMS** – contextual geospatial layers  

    Each section focuses on a specific scientific component
    of extreme rainfall analysis.
    """
)

# ----------------------------------
# Context map (visual only)
# ----------------------------------
st.subheader("🌍 Global Context Map")

m = leafmap.Map(minimap_control=True)
m.add_basemap("CartoDB dark_matter")
m.to_streamlit(height=450)
