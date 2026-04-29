from flask import Flask, render_template, request
import pickle
import numpy as np

from datetime import datetime



app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

import random

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    try:
        date = request.form['day']
        print("Received date:", date)

        try:
            # Format: 2026-02-28
            day = datetime.strptime(date, "%Y-%m-%d").timetuple().tm_yday
        except:
            # Format: 02/28/2026
            day = datetime.strptime(date, "%m/%d/%Y").timetuple().tm_yday

    except:
        return render_template("index.html", alert="❌ Invalid date format")

    area = float(request.form['area'])
    capacity = float(request.form['capacity'])

    # rest of your code...

    efficiency = 0.8

    # 🔥 Generate realistic 7-day weather inputs
    future_data = []

    for i in range(7):
        d = day + i

        # Simulated weather values
        temp = random.randint(25, 35)
        humidity = random.randint(60, 95)
        wind = random.randint(5, 15)

        future_data.append([d, temp, humidity, wind])

    future_data = np.array(future_data)

    # Predict rainfall
    predictions = model.predict(future_data)

    # Optional: add slight randomness (more realistic)
    predictions = [max(0, p + random.uniform(-2, 2)) for p in predictions]

    total_rainfall = sum(predictions)

    # Water calculation
    water_collected = total_rainfall * area * efficiency

    # Tank percentage
    tank_percentage = min((water_collected / capacity) * 100, 100)

    # Smart alerts
    if tank_percentage >= 100:
        alert = "🚨 Overflow expected! Plan water release."
    elif tank_percentage > 75:
        alert = "⚠️ Tank nearing full capacity."
    elif tank_percentage < 30:
        alert = "💧 Low storage. Conserve water."
    else:
        alert = "✅ Optimal water level."

    return render_template("index.html",
                           prediction=round(total_rainfall, 2),
                           water=round(water_collected, 2),
                           tank=round(tank_percentage, 2),
                           alert=alert,
                           chart_data=list(map(float, predictions)))
if __name__ == "__main__":
    app.run(debug=True,port=5001)