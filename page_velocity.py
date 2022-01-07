import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
   

def show_velo():
    df = pd.read_csv("Real_Combine.csv")
    st.write("### Velocity of wind vs PM 2.5")
    data = df.groupby(["V"])["PM 2.5"].mean().sort_values(ascending=True)
    st.line_chart(data)

    data = df.groupby(["VV"])["PM 2.5"].mean().sort_values(ascending=True)
    st.line_chart(data)
    
    data = df.groupby(["VM"])["PM 2.5"].mean().sort_values(ascending=True)
    st.line_chart(data)