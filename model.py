import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load and preprocess data
dataset = pd.read_csv("weather.csv").dropna()

drop_cols = [
    "WindDir3pm","WindSpeed9am","WindDir9am","WindGustDir",
    "WindSpeed3pm","Humidity3pm","Pressure3pm","Cloud3pm"
]
dataset = dataset.drop(drop_cols, axis=1)

dataset['RainToday'] = dataset['RainToday'].astype('category').cat.codes
dataset['RainTomorrow'] = dataset['RainTomorrow'].astype('category').cat.codes

X = dataset.drop('RainTomorrow', axis=1)
y = dataset['RainTomorrow']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

def predict_weather(input_data):
    return model.predict([input_data])[0]
