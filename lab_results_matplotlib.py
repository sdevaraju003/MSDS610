import pandas as pd
import matplotlib.pyplot as plt
import os
# Load dataset
df = pd.read_csv("Lab Results.csv")

# Print columns so user/instructor can see what's available
print("Columns found in dataset:")
print(df.columns.tolist())

# Select a categorical column to plot (change if needed)
column_to_plot = df.columns[0]

# Count occurrences
value_counts = df[column_to_plot].value_counts()

# Create Figure and Axes (stateless / OO interface)
fig, ax = plt.subplots()

# Bar chart for categorical data
ax.bar(value_counts.index.astype(str), value_counts.values)

# Improve readability
ax.set_xlabel(column_to_plot)
ax.set_ylabel("Count")
ax.set_title(f"Count of {column_to_plot} Values")
ax.tick_params(axis='x', rotation=45)

# Display plot
plt.show()
