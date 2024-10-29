import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the model and DataFrame globally
pipe = pickle.load(open("GBC_pipeline.pkl", 'rb'))
df = pickle.load(open("df.pkl", 'rb'))

# Display title and description in Streamlit
def display_title():
    st.write("""
        # Heart Disease Predictor  

        This is my project on heart disease prediction, using data I downloaded from Kaggle. Throughout this endeavor, I gained substantial knowledge and learned numerous new techniques.

        By applying various data preprocessing and machine learning methods, I was able to build an effective model. I achieved an accuracy of about 87% with my model.
    """)

# Define a function to collect user input
def get_user_input():
    # Create columns for better layout
    col1, col2 = st.columns(2)

    with col1:
        # Age input box
        age_input = st.text_input('Age', placeholder='Enter your Age')
        try:
            age = int(age_input)
        except ValueError:
            age = None
            
        # Sex selectbox
        sex = st.selectbox('Sex', df['Sex'].unique())

        # RestingBP input box
        RestingBP_input = st.text_input('Resting Blood Pressure', placeholder='Enter your RestingBP')
        try:
            RestingBP = int(RestingBP_input)
        except ValueError:
            RestingBP = None

        # Cholesterol input box
        #Cholesterol = st.number_input('Cholesterol')
        
        Cholesterol_input = st.text_input('Cholesterol', placeholder='Enter your Cholesterol level')
        try:
            Cholesterol = int(Cholesterol_input)
        except ValueError:
            Cholesterol = None

        # MaxHR input box
        MaxHR = st.number_input('MaxHR')

    with col2:
        # Sex selectbox
        #sex = st.selectbox('Sex', df['Sex'].unique())

        # ChestPainType selectbox
        ChestPainType = st.selectbox('ChestPainType', df['ChestPainType'].unique())

        # FastingBS selectbox
        FastingBS = st.selectbox('FastingBS', df['FastingBS'].unique())

        # RestingECG selectbox
        RestingECG = st.selectbox('RestingECG', df['RestingECG'].unique())

        # ExerciseAngina selectbox
        ExerciseAngina = st.selectbox('ExerciseAngina', df['ExerciseAngina'].unique())
        
        # ST_Slope selectbox
        ST_Slope = st.selectbox('ST_Slope', df['ST_Slope'].unique())

    # Oldpeak selectbox
    #Oldpeak = st.selectbox('Oldpeak', df['Oldpeak'].unique())
    Oldpeak = st.slider('Oldpeak', -2.6, 6.2, 0.0)
    
    input_data =  {
        'Age': age,
        'Sex': sex,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'MaxHR': max_hr,
        'ChestPainType': chest_pain_type,
        'FastingBS': fasting_bs,
        'RestingECG': resting_ecg,
        'ExerciseAngina': exercise_angina,
        'Oldpeak': oldpeak,
        'ST_Slope': st_slope
    }

# Define a function to make a prediction
def predict_heart_disease(input_data):
    query_df = pd.DataFrame([input_data])
    prediction = pipe.predict(query_df)
    return prediction[0]  # Returns 1 for "Heart Disease" and 0 for "No Heart Disease"

# Main Streamlit app
def main():
    display_title()
    user_input = get_user_input()

    if st.button('Predict Heart Disease'):
        prediction = predict_heart_disease(user_input)
        if prediction == 1:
            st.success('You have Heart Disease: Yes')
        else:
            st.success("You don't have Heart Disease: No")

if __name__ == "__main__":
    main()
