# Titanic EDA & Data Cleaning Project

This project is part of my Machine Learning Engineering learning portfolio.  
The goal is to perform Exploratory Data Analysis (EDA), clean the dataset, and prepare it for modeling.

## 📁 Project Structure
01-eda-titanic-analysis/
│
├── notebooks/
│   └── 01_eda_titanic.ipynb        # Full exploratory data analysis
│
├── src/
│   └── data_cleaning.py # Script for cleaning and feature engineering
│
├── data/
│   └── Titanic-Dataset.csv   # Original dataset
│   └── titanic_clean.csv     # Cleaned dataset (generated)
│
└── requirements.txt
## 🚀 What I Learned

- How to load and inspect raw data  
- How to handle missing values  
- How to visualize data  
- How to extract new features (Title, FamilySize)  
- How to structure a real ML project folder  
- How to use Git + GitHub

## 📊 Main Insights

- Women survived much more often than men  
- Higher-class passengers had significantly higher survival rates  
- Traveling alone decreased survival probability

## 🔧 How to Run

```bash
pip install -r requirements.txt
python src/data_cleaning.py
