import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

# Load dataset
data = pd.read_csv("rainfall_data.csv")

# ✅ Use 4 features
X = data[['Day', 'Temperature', 'Humidity', 'Wind']]
y = data['Rainfall']

# Train model
model = RandomForestRegressor(n_estimators=200)
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model retrained successfully!")