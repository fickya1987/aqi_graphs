import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
   

def show_slp():
    df = pd.read_csv("Real_Combine.csv")
    st.write("### SLP vs PM 2.5")
    data = df.groupby(["SLP"])["PM 2.5"].mean().sort_values(ascending=True)
    st.line_chart(data)

   