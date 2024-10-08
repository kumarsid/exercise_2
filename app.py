import streamlit as st

pg = st.navigation([
        st.Page("home_page.py", title="Welcome!", icon=":material/add_circle:"),
        st.Page("des_page.py", title="Run Simulation", icon=":material/laptop:"),
        st.Page("lsoa_map.py", title="Plot Map Capacity", icon=":material/map:")
        
     ])

pg.run()