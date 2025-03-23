import pytest
import joblib
import pandas as pd
from sklearn.metrics import mean_absolute_error
from preprocess_data import load_and_preprocess_data
from app.size_recommendation import recommend_size
from test_utils import is_valid_size, is_valid_height

# Load model
MODEL_PATH = 'models/model.pkl'
DATA_PATH = 'data/size_data.csv'

@pytest.fixture
def model():
    """Load the trained model for testing."""
    return joblib.load(MODEL_PATH)

@pytest.fixture
def processed_data():
    """Load and preprocess the dataset for testing."""
    data, _ = load_and_preprocess_data(DATA_PATH)
    return data

def test_model_prediction(model, processed_data):
    """Test if the model predicts reasonable size values."""
    X_test = processed_data[['Height Start', 'Usual Size (UK)']]
    y_test = processed_data['Recommended Size Encoded']

    y_pred = model.predict(X_test)

    # Ensure predictions are within a reasonable range
    assert all(0 <= round(pred) < len(processed_data['Recommended Size Encoded'].unique()) for pred in y_pred), "Predicted values are out of range"

    # Check MAE is within a reasonable threshold
    mae = mean_absolute_error(y_test, y_pred)
    assert mae < 2.0, f"Mean Absolute Error too high: {mae}"

def test_recommend_size():
    """Test the recommend_size function with sample inputs."""
    assert recommend_size(10, 160, "Tight") in ["XXS", "XS", "S", "M", "L", "XL"], "Invalid size recommendation"
    assert recommend_size(14, 172, "Loose") in ["M", "L", "XL", "XXL"], "Invalid size recommendation"

def test_invalid_inputs():
    """Test invalid input handling."""
    assert not is_valid_size(-1), "Negative size should be invalid"
    assert not is_valid_size(51), "Out-of-range size should be invalid"
    assert not is_valid_height(140), "Height below range should be invalid"
    assert not is_valid_height(180), "Height above range should be invalid"

if __name__ == "__main__":
    pytest.main()
