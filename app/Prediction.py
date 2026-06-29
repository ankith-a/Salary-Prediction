import pandas as pd
import numpy as np
import pickle
import streamlit as st


st.write("""
## Salary Prediction Using Machine Learning💸
""")

#creating a fuction to load model


def loadmodel():
    with open('saveModel.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = loadmodel()
model_dt = data['model']
leCountry = data['leCountry']
leEducation = data['leEducation']

countries = [
    'United States of America',
    'Germany',
    'United Kingdom of Great Britain and Northern Ireland ',
    'India',
    'Canada',
    'France',
    'Brazil',
    'Spain',
    'Netherlands',
    'Australia',
    'Italy',
    'Poland',
    'Sweden',
]

education = [
    'Master’s degree',
    'Bachelor’s degree',
    'Post gard',
    'Less than a Bachelors'
]

country = st.selectbox('Country',countries,index=0)
education = st.selectbox('Education Level',education,index=0)
experience = st.slider('Years of Experience',0,50,3)
#creating a button
submit = st.button('Salary Prediction')
if submit:
    p = np.array([[country,education,experience]])
    p[:, 0] = leCountry.transform(p[:, 0])
    p[:, 1] = leEducation.transform(p[:, 1])
    p = p.astype(float)

    salary = model_dt.predict(p)
    st.subheader(f'The Estimated Salary for  is ${salary[0]:.2f}')
    