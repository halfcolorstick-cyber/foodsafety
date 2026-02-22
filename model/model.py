import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
df = pd.read_csv("data/milknew.csv")

# Convert target labels to numbers
df['Grade'] = df['Grade'].map({'low': 0, 'medium': 1, 'high': 2})

# Features and target
X = df.drop('Grade', axis=1)
y = df['Grade']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

import os

# Ensure folder exists
os.makedirs("model", exist_ok=True)

# Save model
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved at: model/model.pkl")
print("Model trained and saved successfully!")