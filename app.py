from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    values = [
        float(data["ph"]),
        float(data["turbidity"]),
        float(data["tds"]),
        float(data["hardness"]),
        float(data["temperature"])
    ]

    prediction = model.predict([values])[0]
    result = "Safe ✅" if prediction==1 else "Unsafe ❌"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)