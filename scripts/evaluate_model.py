import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, r2_score
from preprocess_data import load_and_preprocess_data

def evaluate_model(model_path, data_path):
    """Loads the trained model and evaluates it on test data."""
    # Load processed data
    data, label_encoder = load_and_preprocess_data(data_path)
    
    # Features and target
    X_test = data[['Height Start', 'Usual Size (UK)']]
    y_test = data['Recommended Size Encoded']

    # Load model
    model = joblib.load(model_path)

    # Predict
    y_pred = model.predict(X_test)

    # Convert predicted numeric values back to categorical
    y_pred_labels = [label_encoder.inverse_transform([round(pred)])[0] for pred in y_pred]

    # Evaluate
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Model Evaluation:")
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"R² Score: {r2:.2f}")

if __name__ == "__main__":
    evaluate_model('models/model.pkl', 'data/size_data.csv')

