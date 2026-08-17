import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    roc_curve,
    roc_auc_score
)

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="wide"
)

# =========================================================
# CUSTOM CSS FOR SKY BLUE BACKGROUND & POWER BI BUTTON SHADOWS
# =========================================================

st.markdown("""
<style>
    /* Sky Blue Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 50%, #7dd3fc 100%);
        color: #0f172a;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Title Styling */
    h1 {
        color: #0369a1;
        font-weight: 800;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.6);
    }
    
    /* Headers Styling */
    h2, h3 {
        color: #0284c7;
        font-weight: 700;
        border-bottom: 2px solid #7dd3fc;
        padding-bottom: 5px;
        margin-top: 20px;
    }
    
    /* Card Style Metrics */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.85);
        border: 1px solid #7dd3fc;
        padding: 15px 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(3, 105, 161, 0.15);
        backdrop-filter: blur(4px);
    }
    div[data-testid="stMetric"] label {
        color: #0369a1 !important;
        font-weight: 600 !important;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: #0c4a6e !important;
        font-weight: 800 !important;
    }

    /* Vibrant Multi-Color Power BI / Header Buttons Container */
    .title-button-container {
        display: flex;
        gap: 12px;
        margin: 15px 0 25px 0;
        flex-wrap: wrap;
    }
    
    /* Enhanced Power BI Style Button Shadows and Glows */
    .title-pill-btn {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        color: white;
        padding: 9px 20px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.9rem;
        box-shadow: 0 6px 16px rgba(2, 132, 199, 0.45), 0 2px 4px rgba(0, 0, 0, 0.1);
        display: inline-block;
        border: 1px solid rgba(255, 255, 255, 0.3);
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
    }
    .title-pill-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(2, 132, 199, 0.6), 0 4px 6px rgba(0, 0, 0, 0.15);
    }

    .title-pill-btn-alt1 {
        background: linear-gradient(135deg, #0d9488 0%, #115e59 100%);
        color: white;
        padding: 9px 20px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.9rem;
        box-shadow: 0 6px 16px rgba(13, 148, 136, 0.45), 0 2px 4px rgba(0, 0, 0, 0.1);
        display: inline-block;
        border: 1px solid rgba(255, 255, 255, 0.3);
        transition: all 0.3s ease;
    }
    .title-pill-btn-alt1:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(13, 148, 136, 0.6), 0 4px 6px rgba(0, 0, 0, 0.15);
    }

    .title-pill-btn-alt2 {
        background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
        color: white;
        padding: 9px 20px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.9rem;
        box-shadow: 0 6px 16px rgba(217, 119, 6, 0.45), 0 2px 4px rgba(0, 0, 0, 0.1);
        display: inline-block;
        border: 1px solid rgba(255, 255, 255, 0.3);
        transition: all 0.3s ease;
    }
    .title-pill-btn-alt2:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(217, 119, 6, 0.6), 0 4px 6px rgba(0, 0, 0, 0.15);
    }

    /* Main Action Prediction Button Styling with Enhanced Shadows */
    .stButton > button {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        color: white;
        font-weight: 700;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 0.6rem 1.2rem;
        box-shadow: 0 6px 16px rgba(2, 132, 199, 0.4), 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #0369a1 0%, #075985 100%);
        box-shadow: 0 8px 22px rgba(3, 105, 161, 0.6), 0 4px 6px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }

    /* Expander Box Styling */
    div.streamlit-expanderHeader {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 8px;
        border: 1px solid #7dd3fc;
        font-weight: 600;
        color: #0c4a6e;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.title("🩺 Diabetes Prediction Using Machine Learning")

st.markdown(
    "Predictive Modeling using Logistic Regression, "
    "Decision Tree and Random Forest."
)

# Title-styled Colorful Buttons / Pills Bar with Shadows
st.markdown("""
<div class="title-button-container">
    <span class="title-pill-btn">🔵 Logistic Regression</span>
    <span class="title-pill-btn-alt1">🟢 Decision Tree</span>
    <span class="title-pill-btn-alt2">🟠 Random Forest</span>
</div>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATASET
# =========================================================

@st.cache_data
def load_data():
    df = pd.read_csv("Diabetes.csv")
    return df

df = load_data()

# =========================================================
# DATASET PREVIEW
# =========================================================

with st.expander("📂 View Dataset"):
    st.write("Dataset Shape:", df.shape)
    st.dataframe(
        df.head(),
        use_container_width=True
    )

# =========================================================
# FEATURES AND TARGET
# =========================================================

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# =========================================================
# TRAIN TEST SPLIT
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# =========================================================
# FEATURE SCALING
# =========================================================

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# =========================================================
# LOGISTIC REGRESSION
# =========================================================

logistic_model = LogisticRegression(
    max_iter=1000,
    random_state=42
)
logistic_model.fit(X_train_scaled, y_train)
logistic_pred = logistic_model.predict(X_test_scaled)
logistic_prob = logistic_model.predict_proba(X_test_scaled)[:, 1]

# =========================================================
# DECISION TREE
# =========================================================

decision_model = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)
decision_model.fit(X_train, y_train)
decision_pred = decision_model.predict(X_test)
decision_prob = decision_model.predict_proba(X_test)[:, 1]

# =========================================================
# RANDOM FOREST
# =========================================================

random_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)
random_model.fit(X_train, y_train)
random_pred = random_model.predict(X_test)
random_prob = random_model.predict_proba(X_test)[:, 1]

# =========================================================
# ACCURACY
# =========================================================

lr_accuracy = accuracy_score(y_test, logistic_pred)
dt_accuracy = accuracy_score(y_test, decision_pred)
rf_accuracy = accuracy_score(y_test, random_pred)

# =========================================================
# MODEL ACCURACY CARDS
# =========================================================

st.header("📊 Model Accuracy")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Logistic Regression", f"{lr_accuracy:.2%}")
with col2:
    st.metric("Decision Tree", f"{dt_accuracy:.2%}")
with col3:
    st.metric("Random Forest", f"{rf_accuracy:.2%}")

# =========================================================
# ACCURACY GRAPH - SMALL
# =========================================================

st.subheader("📈 Accuracy Comparison")

accuracy_df = pd.DataFrame({
    "Algorithm": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest"
    ],
    "Accuracy": [
        lr_accuracy,
        dt_accuracy,
        rf_accuracy
    ]
})

fig, ax = plt.subplots(figsize=(6, 3))
fig.patch.set_facecolor('#e0f2fe')
ax.set_facecolor('#ffffff')

palette = ["#0284c7", "#0d9488", "#d97706"]

sns.barplot(
    data=accuracy_df,
    x="Algorithm",
    y="Accuracy",
    palette=palette,
    ax=ax
)

ax.set_ylim(0, 1)
ax.set_ylabel("Accuracy", fontsize=9, fontweight='bold', color='#0f172a')
ax.set_xlabel("")
ax.set_title("Algorithm Accuracy Comparison", fontsize=11, fontweight='bold', color='#0f172a')

for i, value in enumerate(accuracy_df["Accuracy"]):
    ax.text(
        i,
        value + 0.02,
        f"{value:.2%}",
        ha="center",
        fontsize=9,
        fontweight='bold',
        color='#0f172a'
    )

plt.xticks(rotation=10, fontsize=8, fontweight='bold')
plt.yticks(fontsize=8)
sns.despine(left=True, bottom=True)
plt.tight_layout()

st.pyplot(fig, use_container_width=False)

# =========================================================
# CONFUSION MATRICES
# =========================================================

st.header("🔲 Confusion Matrices")

col1, col2, col3 = st.columns(3)

# LOGISTIC REGRESSION CONFUSION MATRIX
with col1:
    st.subheader("Logistic Regression")
    cm_lr = confusion_matrix(y_test, logistic_pred)

    fig1, ax1 = plt.subplots(figsize=(3, 2.5))
    fig1.patch.set_facecolor('#e0f2fe')
    ax1.set_facecolor('#ffffff')

    sns.heatmap(
        cm_lr,
        annot=True,
        fmt="d",
        cmap="Blues",
        annot_kws={"size": 10, "weight": "bold"},
        cbar=False,
        ax=ax1
    )
    ax1.set_xlabel("Predicted", fontsize=8, fontweight='bold')
    ax1.set_ylabel("Actual", fontsize=8, fontweight='bold')
    ax1.set_title("Logistic Regression", fontsize=9, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig1, use_container_width=False)

# DECISION TREE CONFUSION MATRIX
with col2:
    st.subheader("Decision Tree")
    cm_dt = confusion_matrix(y_test, decision_pred)

    fig2, ax2 = plt.subplots(figsize=(3, 2.5))
    fig2.patch.set_facecolor('#e0f2fe')
    ax2.set_facecolor('#ffffff')

    sns.heatmap(
        cm_dt,
        annot=True,
        fmt="d",
        cmap="BuGn",
        annot_kws={"size": 10, "weight": "bold"},
        cbar=False,
        ax=ax2
    )
    ax2.set_xlabel("Predicted", fontsize=8, fontweight='bold')
    ax2.set_ylabel("Actual", fontsize=8, fontweight='bold')
    ax2.set_title("Decision Tree", fontsize=9, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig2, use_container_width=False)

# RANDOM FOREST CONFUSION MATRIX
with col3:
    st.subheader("Random Forest")
    cm_rf = confusion_matrix(y_test, random_pred)

    fig3, ax3 = plt.subplots(figsize=(3, 2.5))
    fig3.patch.set_facecolor('#e0f2fe')
    ax3.set_facecolor('#ffffff')

    sns.heatmap(
        cm_rf,
        annot=True,
        fmt="d",
        cmap="YlOrBr",
        annot_kws={"size": 10, "weight": "bold"},
        cbar=False,
        ax=ax3
    )
    ax3.set_xlabel("Predicted", fontsize=8, fontweight='bold')
    ax3.set_ylabel("Actual", fontsize=8, fontweight='bold')
    ax3.set_title("Random Forest", fontsize=9, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig3, use_container_width=False)

# =========================================================
# ROC CURVE
# =========================================================

st.header("📉 ROC Curve Comparison")

lr_fpr, lr_tpr, _ = roc_curve(y_test, logistic_prob)
dt_fpr, dt_tpr, _ = roc_curve(y_test, decision_prob)
rf_fpr, rf_tpr, _ = roc_curve(y_test, random_prob)

lr_auc = roc_auc_score(y_test, logistic_prob)
dt_auc = roc_auc_score(y_test, decision_prob)
rf_auc = roc_auc_score(y_test, random_prob)

fig4, ax4 = plt.subplots(figsize=(6, 4))
fig4.patch.set_facecolor('#e0f2fe')
ax4.set_facecolor('#ffffff')

ax4.plot(lr_fpr, lr_tpr, label=f"Logistic Regression (AUC = {lr_auc:.2f})", color="#0284c7", linewidth=2)
ax4.plot(dt_fpr, dt_tpr, label=f"Decision Tree (AUC = {dt_auc:.2f})", color="#0d9488", linewidth=2)
ax4.plot(rf_fpr, rf_tpr, label=f"Random Forest (AUC = {rf_auc:.2f})", color="#d97706", linewidth=2)
ax4.plot([0, 1], [0, 1], linestyle="--", label="Random Classifier", color="#64748b")

ax4.set_xlabel("False Positive Rate", fontsize=8, fontweight='bold')
ax4.set_ylabel("True Positive Rate", fontsize=8, fontweight='bold')
ax4.set_title("ROC Curve Comparison", fontsize=11, fontweight='bold', color='#0f172a')
ax4.tick_params(axis="both", labelsize=8)
ax4.legend(fontsize=7)
ax4.grid(alpha=0.3)
plt.tight_layout()

st.pyplot(fig4, use_container_width=False)

# =========================================================
# PERFORMANCE TABLE
# =========================================================

st.header("📋 Model Performance")

performance_df = pd.DataFrame({
    "Algorithm": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest"
    ],
    "Accuracy": [
        lr_accuracy,
        dt_accuracy,
        rf_accuracy
    ],
    "AUC": [
        lr_auc,
        dt_auc,
        rf_auc
    ]
})

performance_df["Accuracy"] = (performance_df["Accuracy"] * 100).round(2)
performance_df["AUC"] = (performance_df["AUC"]).round(3)

st.dataframe(
    performance_df,
    use_container_width=True,
    hide_index=True
)

# =========================================================
# FEATURE IMPORTANCE
# =========================================================

st.header("🌳 Random Forest Feature Importance")

importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": random_model.feature_importances_
})
importance_df = importance_df.sort_values("Importance", ascending=False)

fig5, ax5 = plt.subplots(figsize=(6, 3.5))
fig5.patch.set_facecolor('#e0f2fe')
ax5.set_facecolor('#ffffff')

sns.barplot(
    data=importance_df,
    x="Importance",
    y="Feature",
    color="#0284c7",
    ax=ax5
)

ax5.set_title("Random Forest Feature Importance", fontsize=11, fontweight='bold', color='#0f172a')
ax5.tick_params(labelsize=8)
sns.despine(left=True, bottom=True)
plt.tight_layout()

st.pyplot(fig5, use_container_width=False)

# =========================================================
# DIABETES PREDICTION
# =========================================================

st.header("🩺 Diabetes Prediction")
st.write("Enter patient information to predict diabetes.")

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
    glucose = st.number_input("Glucose", min_value=0, max_value=250, value=120)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=150, value=70)
    skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)

with col2:
    insulin = st.number_input("Insulin", min_value=0, max_value=900, value=80)
    bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
    age = st.number_input("Age", min_value=1, max_value=120, value=30)

# =========================================================
# PREDICT
# =========================================================

if st.button("🔍 Predict Diabetes", use_container_width=True):
    input_data = pd.DataFrame({
        "Pregnancies": [pregnancies],
        "Glucose": [glucose],
        "BloodPressure": [blood_pressure],
        "SkinThickness": [skin_thickness],
        "Insulin": [insulin],
        "BMI": [bmi],
        "DiabetesPedigreeFunction": [diabetes_pedigree],
        "Age": [age]
    })

    prediction = random_model.predict(input_data)[0]
    probability = random_model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Prediction: Diabetes")
    else:
        st.success("✅ Prediction: No Diabetes")

    st.info(f"Diabetes Probability: {probability:.2%}")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")
st.caption("Predictive Modeling Using Machine Learning | Educational Project")