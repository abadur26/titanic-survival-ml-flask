# 🚢 Titanic Survival Prediction - ML Web App

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**An interactive web application that predicts whether a passenger would have survived the Titanic disaster using Machine Learning.**

This project demonstrates a complete **end-to-end Machine Learning pipeline** — from data exploration and model training to deployment as a user-friendly web app using **Flask**.

![Capture](https://github.com/user-attachments/assets/54e74298-7729-4dd7-bd98-1dd4aca6c628)

## ✨ Features

- **Real-time Prediction**: Enter passenger details (age, gender, class, fare, etc.) and get instant survival prediction.
- **Logistic Regression Model**: Trained on the famous Titanic dataset with proper preprocessing (handling missing values, feature scaling, encoding).
- **Clean & Responsive UI**: Built with HTML, CSS, and Bootstrap for a modern look.
- **Model Persistence**: Pre-trained model and scaler saved using `joblib`/`pickle` for fast inference.
- **Educational Notebook**: Step-by-step model development in `model.ipynb`.
- **Easy to Run Locally** or deploy to platforms like Render, Heroku, or Railway.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn (Logistic Regression), Pandas, NumPy
- **Frontend**: HTML5, CSS3, Bootstrap
- **Others**: Jupyter Notebook, Pickle/Joblib for model serialization

## 📊 Project Workflow

1. **Data Exploration & Preprocessing** — Load Titanic dataset, handle missing values, encode categorical features, scale numerical features.
2. **Model Training** — Train a Logistic Regression model (you can easily extend to Random Forest, XGBoost, etc.).
3. **Evaluation** — Check accuracy, confusion matrix, and feature importance.
4. **Deployment** — Build a Flask web app that loads the saved model and scaler for real-time predictions.

## 🚀 Quick Start (Local Setup)

### Prerequisites
- Python 3.8 or higher
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/abadur26/titanic-survival-ml-flask.git
cd titanic-survival-ml-flask

# 2. Create a virtual environment (recommended)
python -m venv venv
# On Windows:
# venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt


Note: If you don't have requirements.txt yet, create one with:
flask
scikit-learn
pandas
numpy

Running the App
python app.py
Open your browser and go to: http://127.0.0.1:5000/ (or the port shown in terminal).
📁 Project Structure
titanic-survival-ml-flask/
├── app.py                    # Main Flask application
├── model.ipynb               # Jupyter notebook - model training & analysis
├── Titanic-Dataset.csv       # Raw dataset
├── titanic_model.pkl         # Trained Logistic Regression model
├── scaler.pkl                # Fitted StandardScaler
├── templates/                # HTML templates
│   ├── index.html
│   └── result.html
├── static/                   # CSS, JS, images (create if needed)
├── requirements.txt          # Python dependencies
├── LICENSE
└── README.md

📈 Model Performance
(Update this section with your actual results)

Accuracy: ~78-82% on test set (typical for Logistic Regression on Titanic)
Key Insights: Passenger class, gender, and age were among the most important factors for survival.

You can improve the model by trying ensemble methods, feature engineering (e.g., creating "Family Size" or "Title" features), or hyperparameter tuning.

🔮 How to Use the Web App

Enter passenger information:
Passenger Class (1, 2, or 3)
Gender (Male/Female)
Age
Fare
(Optional: SibSp, Parch, Embarked, etc.)

Click Predict
Get a clear result: "Survived" or "Did not survive" with probability if you implement it.

🌟 Future Improvements (Roadmap)

Add more ML models with model selection dropdown
Show prediction probability and SHAP/explainable AI insights
Deploy live version (Render / Vercel / AWS)
Add user authentication or history of predictions
Improve UI with charts (survival rate visualization)
Unit tests and CI/CD pipeline
Docker support

🤝 Contributing
Contributions are welcome! Feel free to:

Improve the model accuracy
Enhance the frontend design
Add new features
Fix bugs or documentation


Fork the project
Create your feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.
👨‍💻 Author
Abadur

GitHub: @abadur26
Feel free to connect or provide feedback!


Made with ❤️ for learning Machine Learning & Web Development
Star ⭐ this repository if you found it helpful!
