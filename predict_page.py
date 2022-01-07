import streamlit as st
import numpy as np

def show_predict_page():
    st.title("Air Quality Index predictor")
    st.write("""### We need some data to predict AQI""")

    arr1=['a','b','c']
    arr2=['x','y','z']

    p1 = st.selectbox("argument 1", arr1)
    p2 = st.selectbox("argument 2", arr2)

    ok = st.button("Calculate AQI")
    if ok:
        X = np.array([[p1,p2]])
