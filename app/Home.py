import streamlit as st
st.title('Software Developer Salary Prediction')

st.write("""
This Machine Predict Salary of a Software Engineer using various Predictors like, **Experience** and **Education** 
""")

st.subheader('Explore or Predict')
explore = st.markdown("""
 - **Model Prediction** [Predict](http://localhost:8501/Prediction)
 - **Data Exploration** [Explor](http://localhost:8501/EDA)
""")
