import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


st.write("""
## Exploratory Data Analysis and Visualization
""")

def digest_catgories(catgories, cutoff):
    catgoricalMap = {}

    for i in range(len(catgories)):
        if catgories.values[i] >= cutoff:
            catgoricalMap[catgories.index[i]] = catgories.index[i]
        else:
            catgoricalMap[catgories.index[i]] = 'Other'

    return catgoricalMap

def setExperience(i):
    if i == 'More than 50 years':
        return 50
    if i == 'Less than 1 year':
        return 0.5
    return float(i)

def setEducation(i):
    if 'Master’s degree' in i:
        return 'Master’s degree'
    if 'Bachelor’s degree' in i:
        return 'Bachelor’s degree'
    if 'Professional degree' in i or 'Other doctoral degree' in i:
        return 'Post gard'
    return 'Less than a Bachelors'

@st.cache_data
def load_data():
    data = pd.read_csv('survey.csv')
    df = data[['Country','EdLevel','YearsCodePro','Employment','ConvertedCompYearly']]
    df = df.rename({'ConvertedCompYearly': 'Salary'}, axis=1)
    df = df[df['Salary'].notnull()]
    df = df.dropna()
    shaped = df[df['Employment'] == 'Employed, full-time']
    df = shaped.drop('Employment', axis=1)
    countryMap = digest_catgories(df.Country.value_counts(), 500)
    df.Country = df['Country'].map(countryMap)
    df = df[df['Salary'] <= 250000]
    df = df[df['Salary'] > 10000]
    df = df[df['Country'] != 'Other']
    df['YearsCodePro'] = df['YearsCodePro'].apply(setExperience)
    df['EdLevel'] = df['EdLevel'].apply(setEducation)
    return df

df = load_data()
def dataDist():
    viz = df['Country'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(viz, labels=viz, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    st.subheader("""
    Data Distribution by Countries
    """)
    st.pyplot(fig1)
    ##bar chart
    st.subheader("""
    Mean Salary by Countries
    """)
    data = df.groupby(['Country'])['Salary'].mean().sort_values(ascending=True)
    st.bar_chart(data)
    ##Line chart
    data = df.groupby(['YearsCodePro'])['Salary'].mean().sort_values(ascending=True)
    st.line_chart(data)
dist = dataDist()