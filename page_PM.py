import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
   
def bar_fun():
    df = pd.read_csv("Real_Combine.csv")
    bins=[0,50,100,150,200,300,500]
    labels=['0-50','50-100','100-150','150-200','200-300','300-500',]
    df['PM 2.5']=pd.cut(df['PM 2.5'],bins,labels=labels)
    df.groupby('PM 2.5',as_index=False)
    data = df["PM 2.5"].value_counts()
    print(data)
    st.bar_chart(data)

def show_pm():
    df = pd.read_csv("Real_Combine.csv")
    st.write("### PM 2.5")
    bar_fun()
    