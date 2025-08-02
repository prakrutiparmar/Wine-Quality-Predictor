# 🍷 Wine Quality Prediction App

This project is a simple yet effective **machine learning web application** that predicts wine quality based on key chemical properties. Built using **Streamlit**, it provides an interactive UI where users can input wine attributes and get instant predictions.

## 🚀 Features

- Predicts whether a wine is **Good** or **Bad**
- Interactive sliders for input
- Built using a **Random Forest Classifier**
- Deployed with a clean and minimal **Streamlit interface**

## 🛠️ Tech Stack

- Python
- scikit-learn
- Pandas
- NumPy
- Streamlit
- Pickle

## 📊 Features Used for Prediction

- Volatile Acidity  
- Citric Acid  
- Sulphates  
- Alcohol Content

## 🧠 Model Details

- **Algorithm**: Random Forest Classifier  
- **Accuracy**: ~86% on test data  
- Model trained using the UCI Wine Quality dataset  
- Saved with `pickle` for fast loading in the app


## 📦 Installation & Usage

### 1. Clone the Repository, Install Dependencies & Run the App
```bash
# Step 1: Clone the repository
git clone https://github.com/YOUR_USERNAME/wine-quality-predictor.git
cd wine-quality-predictor

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the Streamlit app
streamlit run app.py

