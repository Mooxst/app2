import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


st.set_option('deprecation.showPyplotGlobalUse', False)


uploaded_file = st.file_uploader("Corelogic_NZ_HousePriceIndex_Residentialpricemovement_APR2024__1_.xlsx", type="xlsx")

if uploaded_file:
   
    df = pd.read_excel(uploaded_file)
    df.rename(columns={'Territorial authority': 'region'}, inplace=True)

    
    st.write("DataFrame Overview:")
    st.dataframe(df)

    
    st.write("### Average house price per region")
    plt.figure(figsize=(25, 16))
    plt.bar(df['region'], df['Average current value'], color='skyblue')
    plt.xlabel('Region')
    plt.ylabel('Average Current Value')
    plt.title('Average house price per region')
    plt.xticks(rotation=90)
    plt.tight_layout()
    st.pyplot()

    
    st.write("### Distribution of Property Prices")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Average current value'], bins=50, kde=True)
    plt.title('Distribution of Property Prices')
    plt.xlabel('Average price')
    plt.ylabel('Frequency')
    st.pyplot()
