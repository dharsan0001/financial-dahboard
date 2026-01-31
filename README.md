📊 Financial Dataset Generator

This repository contains a synthetic financial dataset generated for analysis, modeling, and reporting.
The dataset includes 2000 rows and the following columns:

Date

Region (East, West, North, South)

Product (Laptop, Phone, Tablet, Monitor, Accessories)

Category

Revenue

Cost

Expenses

✅ Dataset Details
File

financial_data_2000_rows.xlsx

Columns
Column	Description
Date	Transaction date
Region	Geographic region (East, West, North, South)
Product	Product type
Category	Product category
Revenue	Total revenue
Cost	Cost of goods sold
Expenses	Operating expenses
🚀 Usage

You can use this dataset for:

Data analysis (Pandas, Excel, Power BI)

Machine learning models

Financial reporting practice

Visualization projects

📥 Download

You can download the dataset from this repository:

financial_data_2000_rows.xlsx

🛠️ How to Generate the Dataset

If you want to generate the dataset again using Python, you can use the following script:

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Seed for reproducibility
np.random.seed(42)

n_rows = 2000

regions = ["East", "West", "North", "South"]
products = ["Laptop", "Phone", "Tablet", "Monitor", "Accessories"]
categories = ["Electronics", "Mobile", "Computing", "Accessories"]

start_date = datetime(2020, 1, 1)

data = []
for i in range(n_rows):
    date = start_date + timedelta(days=random.randint(0, 365*4))
    region = random.choice(regions)
    product = random.choice(products)
    category = random.choice(categories)

    revenue = round(np.random.uniform(200, 5000), 2)
    cost = round(revenue * np.random.uniform(0.4, 0.7), 2)
    expenses = round(revenue * np.random.uniform(0.1, 0.3), 2)

    data.append([date, region, product, category, revenue, cost, expenses])

df = pd.DataFrame(data, columns=["Date", "Region", "Product", "Category", "Revenue", "Cost", "Expenses"])
df.to_excel("financial_data_2000_rows.xlsx", index=False)

📌 Notes

The dataset is synthetic and generated randomly.

It is intended for practice and learning purposes only.

⭐ Contributions

Feel free to open issues or submit pull requests if you want:

more rows

additional columns

real-world data sources

enhanced formatting
