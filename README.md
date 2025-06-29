# 🧠 Stroke Risk Prediction Project

This is a complete end-to-end Machine Learning project that predicts the risk of a stroke based on patient health data. It includes data cleaning, visualization, model training, and an interactive web dashboard built using **Streamlit**.

---

## 📌 Features

- ✅ Data cleaning and preprocessing (missing values, encoding, etc.)
- ✅ Data storage in MySQL using SQLAlchemy
- ✅ Visualizations:
  - Bar chart (stroke cases by gender)
  - Pie chart
  - Correlation heatmap
- ✅ Feature selection and Logistic Regression model training
- ✅ Model performance evaluation (confusion matrix, classification report)
- ✅ Streamlit-based web dashboard to predict stroke risk
- ✅ Exported model and scaler for deployment

---

## 🔧 Technologies Used

- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn**
- **Seaborn**, **Matplotlib**
- **MySQL**, **SQLAlchemy**
- **Streamlit**
- **Pickle** (for saving models)

---
##install dependencies

pip install -r requirements.txt


##Dataset
Source: Kaggle - Stroke Prediction Dataset

##📊 Visual Analysis & EDA
I used data visualizations to understand patterns in the dataset before building the ML model.

##📉 Bar Graph – Stroke Cases by Gender
📄 bargraph_Visual.py
This shows how many stroke cases happened for each gender. It helps compare stroke counts between male and female patients.

##🥧 Pie Chart – Stroke Distribution by Gender
📄 pie_chart_visual.py
A pie chart that shows the percentage of stroke cases by gender. It gives a quick idea of which gender has more stroke cases in the dataset.

##🔥 Heatmap – Feature Correlation
📄 Advance_Visual.py
This heatmap shows how different health features (like age, BMI, glucose level) are related to each other and to stroke. It helped me choose important features for the model.

These visuals made it easier to understand the data and decide what features to use in training the model.


