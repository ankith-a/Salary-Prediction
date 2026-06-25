# 💼 Salary Prediction Using Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A complete Machine Learning project that predicts **software developer salaries** using data from the Stack Overflow Developer Survey. This project demonstrates the complete ML workflow, including data preprocessing, exploratory data analysis (EDA), feature engineering, categorical encoding, regression modeling, and salary prediction.

---

# 📌 Project Objective

The objective of this project is to build a machine learning model capable of predicting a developer's annual salary based on professional experience, education level, and country.

The model helps estimate salary expectations for software developers by learning patterns from real-world survey data.

---

# 📊 Dataset

The project uses the **Stack Overflow Developer Survey** dataset.

### Dataset Includes

- Country
- Education Level
- Years of Professional Coding Experience
- Annual Salary (Target Variable)

The dataset is cleaned by removing invalid salary ranges, filtering countries with insufficient data, and handling missing values before model training. :contentReference[oaicite:2]{index=2}

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Cleaning & Analysis |
| NumPy | Numerical Operations |
| Matplotlib | Data Visualization |
| Scikit-Learn | Machine Learning |
| Jupyter Notebook | Development Environment |

---

# 🔄 Project Workflow

### 1️⃣ Data Collection

- Import survey dataset
- Explore dataset structure
- Inspect features and data types

### 2️⃣ Data Cleaning

- Handle missing values
- Remove salary outliers
- Filter unnecessary records
- Select relevant features

### 3️⃣ Exploratory Data Analysis

Performed analysis on:

- Salary Distribution
- Country-wise Salary Analysis
- Education Level Distribution
- Years of Experience Analysis
- Boxplots and Statistical Summaries

### 4️⃣ Feature Engineering

Applied preprocessing techniques including:

- Label Encoding
- Data Filtering
- Categorical Feature Transformation
- Numerical Feature Preparation

### 5️⃣ Model Building

Built a regression model using:

- Linear Regression

Prepared the feature matrix (`X`) and target variable (`Salary`) before training the model. :contentReference[oaicite:3]{index=3}

### 6️⃣ Model Evaluation

Evaluated the regression model using prediction performance and compared predicted salary values against actual salaries.

---

# 📈 Key Insights

- Salary generally increases with years of professional coding experience.
- Country has a significant impact on salary distribution.
- Higher education levels are associated with higher salary ranges.
- Removing outliers improves regression model performance.
- Feature encoding enables categorical variables to be used effectively in machine learning models.

---

# 📁 Project Structure

```text
Salary-Prediction-Using-Machine-Learning/
│
├── notebook/
│   └── salary_prediction.ipynb
│
├── data/
│   └── survey_results.csv
│
├── screenshots/
│   ├── salary_by_country.png
│
├── models/
│   └── salary_prediction_model.pkl
│
├── requirements.txt
│
└── README.md
```

---

# 🚀 Future Improvements

- Implement Random Forest Regressor
- Compare multiple regression algorithms
- Hyperparameter tuning using GridSearchCV
- Deploy using Streamlit
- Build a salary prediction web application
- Save and load trained models with Joblib

---

# 💡 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Regression Modeling
- Data Visualization
- Machine Learning
- Predictive Analytics
- Python Programming

---

# 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/Salary-Prediction-Using-Machine-Learning.git

# Navigate to the project folder
cd Salary-Prediction-Using-Machine-Learning

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook
```

---

# 📋 requirements.txt

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
jupyter
notebook
ipykernel
```

---

# 👨‍💻 Author

**Ankith A**

**BCA Graduate | Data Science & Artificial Intelligence Enthusiast**

Passionate about Machine Learning, Data Analytics, Artificial Intelligence, and Predictive Modeling.

⭐ **If you found this project useful, consider giving it a Star!**
