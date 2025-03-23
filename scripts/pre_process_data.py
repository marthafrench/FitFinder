import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data(file_path):
    """Loads and preprocesses the dataset."""
    # Load data
    data = pd.read_csv(file_path)

    # Extract numerical representation of height
    data['Height Start'] = data['Height (cm)'].apply(lambda x: int(x.split('-')[0]) if '-' in x else int(x))

    # Encode categorical labels (Recommended Size)
    label_encoder = LabelEncoder()
    data['Recommended Size Encoded'] = label_encoder.fit_transform(data['Recommended Size'])

    return data, label_encoder  # Return processed data and label encoder for inverse transformations

if __name__ == "__main__":
    processed_data, encoder = load_and_preprocess_data('data/size_data.csv')
    print("Data preprocessed successfully.")
    print(processed_data.head())
