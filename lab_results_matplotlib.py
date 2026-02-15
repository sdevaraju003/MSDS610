import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Lab Results.csv")

print("Columns found in dataset:")
print(df.columns.tolist())

column_to_plot = df.columns[0]
value_counts = df[column_to_plot].value_counts()

fig, ax = plt.subplots()
ax.bar(value_counts.index.astype(str), value_counts.values)

ax.set_xlabel(column_to_plot)
ax.set_ylabel("Count")
ax.set_title(f"Count of {column_to_plot} Values")
ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig("output_plot.png")
print("Plot saved as output_plot.png")
