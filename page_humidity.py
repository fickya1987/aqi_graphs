import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
   

def show_humidity():
    df = pd.read_csv("Real_Combine.csv")
    st.write("### Humidity vs PM 2.5")
    data = df.groupby(["H"])["PM 2.5"].mean().sort_values(ascending=True)
    st.line_chart(data)

   