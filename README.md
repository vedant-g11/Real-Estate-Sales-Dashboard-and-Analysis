# 🏡 Real Estate Sales Dashboard & Price Prediction (2001–2022)

This project presents a complete data analytics and visualization pipeline for 20 years of real estate sales data. It includes a **Power BI dashboard**, **SQL queries for business insights**, and a **machine learning model** to predict housing prices based on historical data.

---

## 📊 Project Overview

The goal of this project is to analyze real estate sales trends from 2001 to 2022 using AWS services and visualize key business insights. Additionally, a Python model has been built to predict house prices using the same dataset.

---

## 📁 Dataset

The dataset used is publicly available on Kaggle:  
🔗 [Real Estate Sales (2001–2022) – Kaggle](https://www.kaggle.com/datasets/omniamahmoudsaeed/real-estate-sales-2001-2022)

- Format: CSV
- Records: Over 200,000 property sale records
- Fields include: Sale date, price, location, year built, square footage, and more.

---

## ☁️ Technologies Used

- **Amazon S3** – for storing raw and processed data
- **AWS Glue + Crawlers** – for schema discovery and ETL processing
- **Amazon Athena** – for serverless querying of S3 data using SQL
- **Power BI** – for interactive dashboard visualization
- **Python (scikit-learn, pandas)** – for building the price prediction model

---

## 📂 Repository Contents

| File Name             | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `Real_Estate.pbix`    | Power BI dashboard file with visualizations and insights                    |
| `RealEstateQueries.docx` | Contains SQL queries run on Athena for sales trend analysis                 |
| `real_estate.py`      | Python script that trains a regression model to predict housing prices      |
| `README.md`           | This README file                                                            |

---

## 📈 Power BI Dashboard Highlights

The Power BI report includes:
- Year-over-year sales volume and average price
- Property types and price distribution
- Sale trends by location and square footage
- Heatmaps and bar charts for performance comparison

> **Note:** You need Power BI Desktop to open the `.pbix` file.

---

## 🧠 Query Logic (`RealEstateQueries.docx`)

The SQL queries include:
- Total transactions per year
- Average sale price by year and location
- Top 5 cities by price growth
- Price trend by property type
- Seasonal pattern analysis (quarterly trends)

These queries were run using **Amazon Athena** on data stored in **Amazon S3**, cataloged with **AWS Glue**.

---

## 🧮 Price Prediction Script (`real_estate.py`)

This Python script:
- Loads the cleaned dataset
- Preprocesses data (feature engineering, handling missing values)
- Splits into training and testing sets
- Trains a regression model (e.g., Linear Regression / RandomForest)
- Predicts house price based on input features like date, area, year built, etc.

### ▶️ How to Run

Make sure you have Python 3 and the required libraries:

```bash
pip install pandas scikit-learn matplotlib
python real_estate.py
