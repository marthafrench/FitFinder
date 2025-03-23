import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load the dataset
data = pd.read_csv('data/size_data.csv')

# Split the height into ranges (for simplicity, we convert to a numerical feature)
data['Height Start'] = data['Height (cm)'].apply(lambda x: int(x.split('-')[0]) if '-' in x else int(x))

# Features (numeric)
X = data[['Height Start', 'Usual Size (UK)']]  # Use height start and usual size as features
y = data['Recommended Size']  # Target variable (this would need to be converted to a numeric value)

# Encode the target variable (Recommended Size)
y = pd.Categorical(y).codes  # Convert categorical target into numeric codes

# Train a model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'models/model.pkl')

print("Model trained and saved successfully.")
