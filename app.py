import streamlit as st 
from predict_page import show_predict_page
from explore_page import show_explore_page
from page_1 import show_temp
from page_humidity import show_humidity
from page_PM import show_pm
from page_velocity import show_velo
from page_slp import show_slp

page = st.sidebar.selectbox("Explore",("Aqi", "Temperature","Humidity","Sea Level Pressure","Velocity", "PM 2.5"))
if page == "Aqi":
    show_explore_page()
elif page == "Temperature":
    show_temp()
elif page == "Humidity":
    show_humidity()
elif page == "Sea Level Pressure":
    show_slp()
elif page == "Velocity":
    show_velo()
elif page == "PM 2.5":
    show_pm()