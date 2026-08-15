# 🛒 Supermarket Sales Data Cleaning & Visualization

## 📌 Project Overview

This project focuses on **Data Cleaning, Exploratory Data Analysis (EDA), and Data Visualization** using a supermarket sales dataset.

The raw supermarket sales data is cleaned, processed, and analyzed using Python. Different attractive and colorful visualizations are created to understand **sales performance, customer behavior, product performance, payment methods, and sales trends**.

The project demonstrates a complete data analysis workflow from **raw data → data cleaning → preprocessing → EDA → visualization → business insights**.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Clean and preprocess raw supermarket sales data.
* Identify and handle missing values.
* Detect and remove duplicate records.
* Identify and handle outliers.
* Convert and process date-related information.
* Perform Exploratory Data Analysis (EDA).
* Analyze sales and customer behavior.
* Create attractive and colorful visualizations.
* Create a visual dashboard using Python.
* Extract meaningful business insights from the data.
* Save the cleaned dataset for further analysis.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data cleaning, manipulation, and analysis
* **NumPy** – Numerical calculations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization
* **Jupyter Notebook** – Data analysis and project development

---

## 📂 Project Structure

```text
Data Cleaning & Visualization Project/
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

### 📁 File Description

| File / Folder                                            | Description                                                                                     |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `.ipynb_checkpoints/`                                    | Automatically generated Jupyter Notebook checkpoint folder                                      |
| `Supermarket Sales.csv`                                  | Original raw supermarket sales dataset                                                          |
| `cleaned_sales.csv`                                      | Cleaned and processed dataset                                                                   |
| `Data Visualization.png`                                 | Attractive and colorful final visualization/dashboard                                           |
| `Supermarket Sales for Cleaning and Visualization.ipynb` | Main Jupyter Notebook containing data cleaning, preprocessing, EDA, visualization, and insights |
| `requirements.txt`                                       | Contains the Python libraries required for the project                                          |
| `README.md`                                              | Project documentation                                                                           |

---

## 📊 Dataset

The project uses a **Supermarket Sales Dataset** containing information related to supermarket transactions and customers.

The dataset contains **1,000 records and 20 columns**.

### Main Dataset Features

* Invoice ID
* Branch
* City
* Customer Type
* Gender
* Product Line
* Unit Price
* Quantity
* Tax 5%
* Total
* Date
* Time
* Payment
* COGS
* Gross Margin Percentage
* Gross Income
* Rating

---

## 🧹 Data Cleaning

Data cleaning is an important part of this project. The raw dataset was processed before performing visualization and analysis.

### 1. Handling Missing Values

Missing values were checked using Pandas.

```python
df.isnull().sum()
```

Numerical missing values were handled using the **median**, while categorical missing values were handled using the **mode**.

---

### 2. Removing Duplicate Records

Duplicate records were identified using:

```python
df.duplicated().sum()
```

Duplicate records were removed using:

```python
df = df.drop_duplicates()
```

---

### 3. Date Conversion

The `Date` column was converted into a proper datetime format.

```python
df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)
```

Additional date-related features were created, such as:

* Year
* Month
* Day
* Day Name

---

### 4. Outlier Detection

Outliers were detected using the **IQR (Interquartile Range)** method.

The IQR method helps identify unusually high or low values in the sales data.

```python
Q1 = df["Total"].quantile(0.25)
Q3 = df["Total"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
```

The cleaned dataset was then created by removing values outside the acceptable range.

---

## 🔍 Exploratory Data Analysis (EDA)

After cleaning the data, Exploratory Data Analysis was performed to understand patterns and relationships within the dataset.

The project analyzes:

### 🛒 1. Sales by Product Line

Analyzes which product categories generate the highest total sales.

### 🏢 2. Sales by Branch

Compares the sales performance of different supermarket branches.

### 👥 3. Sales by Gender

Analyzes the total sales generated by different customer genders.

### 💳 4. Payment Method Distribution

Shows which payment methods are most frequently used by customers.

### 📦 5. Quantity vs Total Sales

Analyzes the relationship between the quantity purchased and total sales.

### ⭐ 6. Customer Rating Distribution

Shows how customers rate their shopping experience.

### 📈 7. Daily Sales Trend

Analyzes how supermarket sales change over different dates.

### 🔥 8. Correlation Heatmap

Shows the relationships between numerical variables in the dataset.

---

## 📊 Data Visualization

Attractive and colorful graphs were created using **Matplotlib and Seaborn**.

The visualization includes:

* 🛒 Sales by Product Line
* 🏢 Sales by Branch
* 👥 Sales by Gender
* 💳 Payment Method Distribution
* 📦 Quantity vs Total Sales
* ⭐ Customer Rating Distribution
* 📈 Daily Sales Trend
* 🔥 Correlation Heatmap

The final dashboard uses a **faint blue background with colorful charts and blue-themed titles** to make the visualizations attractive and easy to understand.

---

## 🖼️ Dashboard Preview

The final visualization/dashboard is available in:

```text
Data Visualization.png
```

The dashboard provides a quick visual overview of:

* Product line performance
* Branch performance
* Payment method distribution
* Customer ratings

---

## 💡 Key Insights

This project helps identify important business insights such as:

* Which product line performs best.
* Which supermarket branch generates the highest sales.
* Which payment method is most commonly used.
* Customer rating distribution.
* Relationship between quantity and total sales.
* Daily sales trends.
* Relationships between different numerical variables.

These insights can help businesses understand customer behavior and make better data-driven decisions.

---

## 📈 Dashboard Features

The dashboard provides a simple visual summary of the supermarket sales data.

### Dashboard includes:

```text
🛒 Product Line Sales
🏢 Branch Sales
💳 Payment Methods
⭐ Customer Ratings
```

### Design Features

* Faint blue background
* Colorful charts
* Clear titles
* Professional layout
* Easy-to-read labels
* Grid-based dashboard
* Business-focused visualizations

---

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/darshanbhor2006/Data Cleaning & Visualization Project.git
```

### Step 2: Open the Project Folder

```bash
cd Data Cleaning & Visualization Project
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
Supermarket Sales for Cleaning and Visualization.ipynb
```

### Step 6: Run the Notebook

Run all cells in order using:

**Kernel → Restart & Run All**

or select:

**Run All**

---

## 📦 Requirements

The `requirements.txt` file contains the required Python libraries:

```text
pandas
numpy
matplotlib
seaborn
jupyter
```

Install all required libraries using:

```bash
pip install -r requirements.txt
```

---

## 🎓 Learning Outcomes

By completing this project, I gained practical knowledge of:

* Python for Data Science
* Pandas
* NumPy
* Data Cleaning
* Data Preprocessing
* Missing Value Handling
* Duplicate Detection
* Outlier Detection
* Exploratory Data Analysis
* Statistical Analysis
* Data Visualization
* Matplotlib
* Seaborn
* Data Storytelling
* Dashboard Creation
* Business Insight Generation

---

## 🔮 Future Improvements

This project can be further improved by:

* Creating an interactive **Streamlit dashboard**.
* Adding filters for Branch, City, Product Line, Gender, and Payment.
* Adding interactive charts.
* Adding KPI cards such as Total Sales, Average Sales, and Total Transactions.
* Implementing sales prediction using Machine Learning.
* Adding customer segmentation.
* Deploying the dashboard online.
* Creating automated business reports.

---

## 👨‍💻 Author

**Darshan Bhor**

Aspiring Data Scientist | Python | Machine Learning | Data Analytics

---

## ⭐ Conclusion

The **Supermarket Sales Data Cleaning & Visualization** project demonstrates how raw data can be transformed into meaningful business information through **data cleaning, preprocessing, exploratory analysis, visualization, and data storytelling**.

This project provides practical experience in using Python-based Data Science tools to analyze real-world sales data and generate useful insights for business decision-making.

---

## ⭐ If You Like This Project

If you find this project useful or interesting, consider giving the repository a **⭐ Star** on GitHub.
