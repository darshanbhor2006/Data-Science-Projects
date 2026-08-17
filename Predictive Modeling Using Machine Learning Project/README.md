# 🩺 Diabetes Prediction Using Machine Learning

## 📌 Project Overview

This project is a **Predictive Modeling Using Machine Learning**
application that predicts whether a person is likely to have diabetes
based on health-related input features.

Three supervised Machine Learning algorithms are applied and compared:

-   Logistic Regression
-   Decision Tree
-   Random Forest

The project includes model training, testing, accuracy comparison,
confusion matrices, ROC curves, AUC scores, feature importance, and an
interactive Streamlit web application.

> **Note:** This project is developed for educational purposes and
> should not be used as a medical diagnostic system.

## 🎯 Objectives

-   Build a supervised Machine Learning model for diabetes prediction.
-   Apply and compare different classification algorithms.
-   Train and test the models using a diabetes dataset.
-   Evaluate model performance using accuracy and other metrics.
-   Visualize model performance using confusion matrices and ROC curves.
-   Create an interactive web application using Streamlit.

## 🚀 Key Features

-   📂 Diabetes dataset loading
-   🧹 Data preparation and preprocessing
-   📊 Exploratory data analysis
-   🤖 Logistic Regression
-   🌳 Decision Tree
-   🌲 Random Forest
-   📈 Accuracy comparison graph
-   🔲 Confusion matrices for all three algorithms
-   📉 ROC curve comparison
-   🏆 AUC score comparison
-   🌳 Random Forest feature importance
-   🩺 Interactive diabetes prediction
-   💻 Streamlit-based user interface
-   💾 Saved Random Forest model in PKL format

## 🛠️ Technologies Used

  Technology         Purpose
  ------------------ --------------------------------------------
  Python             Programming language
  Pandas             Data loading and data processing
  NumPy              Numerical operations
  Scikit-learn       Machine Learning algorithms and evaluation
  Matplotlib         Data visualization
  Seaborn            Statistical visualization
  Joblib             Saving and loading the ML model
  Streamlit          Web application and dashboard
  Jupyter Notebook   Model development and experimentation

## 📁 Project Structure

``` text
Predictive Modeling Using Machine Learning Project/
│
├── app.py
│
├── Diabetes.csv
│
├── Diabetes_model.pkl
├── Diabetes_Prediction.ipynb
│
├──README.md
│
└── requirements.txt
```

## 📊 Dataset

The dataset contains patient-related attributes used to predict the
diabetes outcome.

### Main Features

-   **Pregnancies** -- Number of pregnancies
-   **Glucose** -- Glucose concentration
-   **BloodPressure** -- Blood pressure level
-   **SkinThickness** -- Skin thickness measurement
-   **Insulin** -- Insulin level
-   **BMI** -- Body Mass Index
-   **DiabetesPedigreeFunction** -- Diabetes-related family history
    score
-   **Age** -- Patient age
-   **Outcome** -- Target variable

### Target Variable

``` text
0 → No Diabetes
1 → Diabetes
```

## 🧠 Machine Learning Algorithms

### 1. Logistic Regression

Logistic Regression is used as a baseline classification algorithm for
predicting the probability of diabetes.

### 2. Decision Tree

Decision Tree uses a series of decision rules to classify patients into
diabetes and non-diabetes classes.

### 3. Random Forest

Random Forest combines multiple decision trees to improve prediction
performance and reduce overfitting.

## 🔄 Machine Learning Workflow

``` text
Dataset
   ↓
Data Loading
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Model Training
   ↓
Model Testing
   ↓
Accuracy Evaluation
   ↓
Confusion Matrix
   ↓
ROC Curve & AUC
   ↓
Model Comparison
   ↓
Final Prediction
   ↓
Streamlit Application
```

## 📈 Model Evaluation

The project evaluates the three algorithms using:

-   Accuracy
-   Precision
-   Recall
-   F1 Score
-   Confusion Matrix
-   ROC Curve
-   AUC Score

The Streamlit application displays the model accuracy comparison and
visual evaluation results.

## 🔲 Confusion Matrix

A confusion matrix is used to understand correct and incorrect
predictions.

It contains:

-   True Positive
-   True Negative
-   False Positive
-   False Negative

Separate confusion matrices are displayed for:

-   Logistic Regression
-   Decision Tree
-   Random Forest

## 📉 ROC Curve

The ROC curve compares the True Positive Rate against the False Positive
Rate for different classification thresholds.

The project displays ROC curves for all three algorithms and calculates
their AUC scores.

A higher AUC generally indicates better class discrimination.

## 🌳 Feature Importance

Random Forest feature importance is used to identify which input
features contribute most to the prediction.

This helps understand the relative importance of variables such as
glucose, BMI, age, and other features in the trained model.

## 💻 Streamlit Application

The `app.py` file provides an interactive dashboard.

The application displays:

1.  Model accuracy
2.  Accuracy comparison graph
3.  Confusion matrices
4.  ROC curve comparison
5.  Model performance table
6.  Random Forest feature importance
7.  Diabetes prediction form

Users can enter patient information and receive a prediction from the
Random Forest model.

## ⚙️ Installation

### Step 1: Clone the Repository

``` bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

``` bash
cd "Predictive Modeling Using Machine Learning Project"
```

### Step 3: Create a Virtual Environment

``` bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

For Windows:

``` bash
venv\Scripts\activate
```

### Step 5: Install Required Libraries

``` bash
pip install -r requirements.txt
```

## ▶️ Run the Streamlit Application

Run:

``` bash
streamlit run app.py
```

The application will open in your web browser.

## 📓 Run the Jupyter Notebook

To open the notebook:

``` bash
jupyter notebook
```

Then open:

``` text
Diabetes_Prediction.ipynb
```

Run the cells from top to bottom to perform data analysis, train the
models, evaluate them, and generate visualizations.

## 💾 Model File

The trained model is stored as:

``` text
Diabetes_model.pkl
```

The model can be loaded using Joblib:

``` python
import joblib

model = joblib.load("Diabetes_model.pkl")
```

## 📋 Example Prediction

The application accepts:

``` text
Pregnancies
Glucose
Blood Pressure
Skin Thickness
Insulin
BMI
Diabetes Pedigree Function
Age
```

After clicking **Predict Diabetes**, the application displays the
predicted result and probability.

Example:

``` text
Prediction: No Diabetes
Diabetes Probability: 18.42%
```

or

``` text
Prediction: Diabetes
Diabetes Probability: 78.31%
```

The displayed values are examples only.

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

-   Supervised Machine Learning
-   Classification algorithms
-   Data preprocessing
-   Train-test splitting
-   Feature scaling
-   Model evaluation
-   Accuracy calculation
-   Confusion matrix visualization
-   ROC and AUC analysis
-   Feature importance
-   Model saving using Joblib
-   Streamlit application development
-   GitHub project management

## 🔮 Future Scope

-   Use a larger and more diverse dataset.
-   Apply hyperparameter tuning.
-   Perform cross-validation.
-   Add additional classification algorithms.
-   Improve the Streamlit dashboard design.
-   Deploy the application online.
-   Add user authentication and prediction history.
-   Improve model interpretability with explainable AI techniques.

## ⚠️ Disclaimer

This application is created for **educational and demonstration purposes
only**. It is not intended to provide medical advice, diagnosis, or
treatment recommendations. Real medical decisions should be made by
qualified healthcare professionals.

## 👨‍💻 Author

**Darshan Bhor**

💼 LinkedIn:
https://www.linkedin.com/in/darshan-bhor-55ab22381 

🐙 GitHub:
https://github.com/darshanbhor2006

## ⭐ Project Highlights

> **Predictive Modeling Using Machine Learning**\
> Built a diabetes prediction system using Logistic Regression, Decision
> Tree, and Random Forest, with model evaluation through accuracy,
> confusion matrices, ROC curves, AUC scores, and an interactive
> Streamlit dashboard.
