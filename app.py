from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model & scaler safely
try:
    model = pickle.load(open("titanic_model.pkl", "rb"))
    scaler = pickle.load(open("scaler.pkl", "rb"))
    print("Model and Scaler loaded successfully")
except Exception as e:
    print(f"Error loading model or scaler: {e}")
    model, scaler = None, None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None or scaler is None:
            raise ValueError("Model or scaler not loaded properly.")

        # Collect form inputs
        pclass = int(request.form.get('Pclass', 0))
        sex = int(request.form.get('Sex', 0))
        age = float(request.form.get('Age', 0))
        sibsp = int(request.form.get('SibSp', 0))
        parch = int(request.form.get('Parch', 0))
        fare = float(request.form.get('Fare', 0))
        embarked = int(request.form.get('Embarked', 0))

        # Features in same order as training
        features = np.array([[pclass, sex, age, sibsp, parch, fare, embarked]])

        print("Features before scaling:", features)
        features = scaler.transform(features)
        print("Features after scaling:", features)

        prediction = model.predict(features)[0]
        result = "Survived 🚢" if prediction == 1 else "Did Not Survive ❌"

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        print(f"Prediction error: {e}")
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
