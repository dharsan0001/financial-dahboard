import pandas as pd
import numpy as np

np.random.seed(42)
rows = 2000

data = {
    "Date": pd.date_range(start="2023-01-01", periods=rows, freq="D"),
    "Region": np.random.choice(["East", "West", "North", "South"], rows),
    "Product": np.random.choice(
        ["Laptop", "Phone", "Tablet", "Monitor", "Accessories"], rows
    ),
    "Category": np.random.choice(["Electronics", "Office", "Personal"], rows),
    "Revenue": np.random.randint(100, 5000, rows),
    "Cost": np.random.randint(50, 3000, rows),
    "Expenses": np.random.randint(20, 1500, rows),
}

df = pd.DataFrame(data)
df.to_excel("chatgpt_2000_dataset.xlsx", index=False)
