import pytest
import pandas as pd
from src.app import predict_heart_disease
import warnings
warnings.filterwarnings("ignore", category=UserWarning)



# Load the model to ensure consistency in predictions
import pickle
pipe = pickle.load(open("GBC_pipeline.pkl", 'rb'))

@pytest.fixture
def test_sample_input():
    # Mock data for input, aligning with what `get_user_input()` would provide
    return {
        'Age': 50,
        'ChestPainType': 'ATA',
        'Sex': 'M',
        'FastingBS': 1,
        'RestingBP': 120,
        'RestingECG': 'Normal',
        'Cholesterol': 200,
        'ExerciseAngina': 'N',
        'MaxHR': 150,
        'ST_Slope': 'Up',
        'Oldpeak': 2.0
    }

def test_predict_heart_disease(test_sample_input):
    # Convert the input to a DataFrame for prediction
    input_df = pd.DataFrame([test_sample_input])
    
    # Run prediction
    prediction = predict_heart_disease(test_sample_input)

    # Use the actual model to predict directly and compare results
    expected_prediction = pipe.predict(input_df)[0]
    
    # Assert if prediction from the function matches the expected model output   

    assert prediction == expected_prediction, "Prediction result does not match the expected model output"