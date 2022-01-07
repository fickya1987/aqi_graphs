import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


@st.cache
def load_data():
    df = pd.read_csv("Real_Combine.csv")

    return df

df = load_data()
def bar_fun():
    df = load_data()
    bins=[0,50,100,150,200,300,500]
    labels=['0-50','50-100','100-150','150-200','200-300','300-500',]
    df['PM 2.5']=pd.cut(df['PM 2.5'],bins,labels=labels)
    df.groupby('PM 2.5',as_index=False)
    data = df["PM 2.5"].value_counts()
    print(data)
    st.bar_chart(data)

def show_explore_page():
    st.title("What is AQI?")
    st.write("### The Air Quality Index (AQI) is used for reporting daily air quality. It tells you how clean or polluted your air is, and what associated health effects might be a concern for you. The AQI focuses on health effects you may experience within a few hours or days after breathing polluted air. EPA calculates the AQI for five major air pollutants regulated by the Clean Air Act: ground-level ozone, particle pollution (also known as particulate matter), carbon monoxide, sulfur dioxide, and nitrogen dioxide.")
    image = Image.open('PM2017.png')
    st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

    fig2 = sns.pairplot(df)
    st.pyplot(fig2)
    