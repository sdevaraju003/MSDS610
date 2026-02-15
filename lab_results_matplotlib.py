import pandas as pd
import matplotlib.pyplot as plt

# Load the Lab Results dataset
df = pd.read_csv("Lab Results.csv")

# Basic cleanup
df = df.dropna()

# Select numeric columns
numeric_cols = df.select_dtypes(include="number")

if numeric_cols.empty:
    raise ValueError("No numeric columns found to plot.")

# Choose first numeric column
col = numeric_cols.columns[0]

# Create Figure and Axes (stateless / OO interface)
fig, ax = plt.subplots()

# Plot histogram
ax.hist(df[col])

# Labels and title
ax.set_xlabel(col)
ax.set_ylabel("Frequency")
ax.set_title(f"Distribution of {col}")

# Display plot
plt.show()