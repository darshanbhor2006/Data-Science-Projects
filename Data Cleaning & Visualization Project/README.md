# 🛒 Supermarket Sales Data Cleaning & Visualization

## 📌 Project Overview

This project focuses on **Data Cleaning, Exploratory Data Analysis (EDA), and Data Visualization** using a supermarket sales dataset.

The raw dataset is cleaned and processed using Python libraries such as **Pandas and NumPy**. After cleaning, different visualizations are created using **Matplotlib and Seaborn** to understand sales trends, customer behavior, product performance, and payment methods.

The project demonstrates the complete data analysis process from **raw data to meaningful business insights**.

---

## 🎯 Objectives

* Clean and preprocess raw supermarket sales data.
* Handle missing values.
* Identify and remove duplicate records.
* Detect and handle outliers.
* Convert and process date-related information.
* Perform Exploratory Data Analysis (EDA).
* Create attractive and colorful visualizations.
* Identify important business insights.
* Create a simple visual dashboard using Python.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation and cleaning
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization
* **Jupyter Notebook** – Project development and analysis

---

📂 Project Structure
Supermarket-Sales-Data-Analysis/
│
├── .ipynb_checkpoints/
│
├── Supermarket Sales.csv
│
├── cleaned_sales.csv
│
├── Data Visualization.png
│
├── Supermarket Sales for Cleaning and Visualization.ipynb
│
├── requirements.txt
│
└── README.md
```

---

## 📊 Dataset

The project uses a **Supermarket Sales Dataset** containing information about:

* Invoice ID
* Branch
* City
* Customer Type
* Gender
* Product Line
* Unit Price
* Quantity
* Tax
* Total Sales
* Date
* Time
* Payment Method
* Cost of Goods Sold (COGS)
* Gross Income
* Customer Rating

The dataset contains **1,000 records and 20 columns**.

---

## 🧹 Data Cleaning

The following data-cleaning techniques were performed:

### 1. Missing Values

Missing values were identified using Pandas.

```python
df.isnull().sum()
```

Numerical missing values were handled using the **median**, while categorical missing values were handled using the **mode**.

### 2. Duplicate Records

Duplicate records were identified and removed.

```python
df.duplicated().sum()
```

```python
df.drop_duplicates()
```

### 3. Date Conversion

The Date column was converted into the proper datetime format.

```python
df["Date"] = pd.to_datetime(df["Date"])
```

### 4. Outlier Detection

Outliers were detected using the **IQR (Interquartile Range)** method.

This helps identify unusually high or low sales values.

---

## 📈 Exploratory Data Analysis

The project analyzes different aspects of supermarket sales, including:

### 🛒 Sales by Product Line

Identifies which product categories generate the highest sales.

### 🏢 Sales by Branch

Compares the performance of different supermarket branches.

### 👥 Sales by Gender

Analyzes sales distribution between male and female customers.

### 💳 Payment Method

Shows which payment methods are most commonly used.

### 📦 Quantity vs Total Sales

Analyzes the relationship between the quantity purchased and total sales.

### ⭐ Customer Ratings

Visualizes the distribution of customer ratings.

### 📅 Daily Sales Trend

Shows how sales change over time.

### 🔥 Correlation Heatmap

Shows relationships between numerical variables in the dataset.

---

## 📊 Dashboard

An attractive and colorful dashboard was created using **Matplotlib and Seaborn**.

The dashboard includes:

* 🛒 Product Line Sales
* 🏢 Branch Sales
* 💳 Payment Methods
* ⭐ Customer Ratings

The dashboard uses a **faint blue background and colorful charts** to make the visual report easy to understand.

---

## 💡 Key Insights

The project helps identify:

* Best-performing product categories
* Highest-performing branch
* Most-used payment method
* Customer rating patterns
* Relationship between quantity and sales
* Overall sales trends
* Relationships between numerical variables

These insights can help businesses understand customer behavior and improve sales strategies.

---

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Supermarket-Sales-Data-Analysis.git
```

### Step 2: Open the Project

```bash
cd Supermarket-Sales-Data-Analysis
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Start Jupyter Notebook

```bash
jupyter notebook
```

### Step 5: Open the Notebook

Open:

```text
supermarket_sales_data_cleaning_visualization.ipynb
```

### Step 6: Run All Cells

Click:

**Kernel → Restart & Run All**

or use:

**Run All**

---

## 📦 Requirements

Create a `requirements.txt` file containing:

```text
pandas
numpy
matplotlib
seaborn
jupyter
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🎓 Learning Outcomes

Through this project, I learned:

* Data Cleaning
* Data Preprocessing
* Handling Missing Values
* Handling Duplicate Data
* Outlier Detection
* Exploratory Data Analysis
* Data Visualization
* Statistical Analysis
* Data Storytelling
* Creating Dashboards using Python

---

## 🔮 Future Improvements

The project can be improved by:

* Creating an interactive **Streamlit dashboard**
* Adding filters for Branch, City, Product Line, and Payment
* Adding interactive charts
* Adding sales prediction using Machine Learning
* Deploying the dashboard online
* Adding automated business reports

---

## 👨‍💻 Author

**Darshan Bhor**

Aspiring Data Scientist | Python | Machine Learning | Data Analytics

---

## ⭐ Conclusion

This project demonstrates how raw supermarket sales data can be transformed into meaningful information through **data cleaning, analysis, visualization, and storytelling**.

It provides practical experience in using Python for real-world data analysis and helps understand how data-driven insights can support business decision-making.
