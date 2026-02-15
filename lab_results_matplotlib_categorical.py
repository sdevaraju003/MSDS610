import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("Lab Results.csv")

print("Columns in dataset:")
print(df.columns.tolist())

# -----------------------------
# Plot 1: Top 10 Combinations of Column 1 & 2
# -----------------------------
col_a = df.columns[0]
col_b = df.columns[1]

group_counts = (
    df.groupby([col_a, col_b])
      .size()
      .reset_index(name="count")
      .sort_values("count", ascending=False)
      .head(10)
)

fig1, ax1 = plt.subplots()
ax1.bar(range(len(group_counts)), group_counts["count"])

ax1.set_xticks(range(len(group_counts)))
ax1.set_xticklabels(
    group_counts[col_a].astype(str) + " | " + group_counts[col_b].astype(str),
    rotation=45,
    ha="right"
)

ax1.set_xlabel(f"{col_a} + {col_b}")
ax1.set_ylabel("Count")
ax1.set_title("Top 10 Lab Record Combinations")

plt.tight_layout()
fig1.savefig("grouped_bar_plot.png")

# -----------------------------
# Plot 2: Horizontal Bar Chart (Top 10 Column 3 Values)
# -----------------------------
col2 = df.columns[2]
counts2 = df[col2].value_counts().head(10)

fig2, ax2 = plt.subplots()
ax2.barh(counts2.index.astype(str), counts2.values)

ax2.set_xlabel("Count")
ax2.set_ylabel(col2)
ax2.set_title(f"Top 10 {col2} Values (Horizontal)")

plt.tight_layout()
fig2.savefig("horizontal_bar_plot.png")

# -----------------------------
# Plot 3: Scatter Plot (Column 4 Distribution)
# -----------------------------
if len(df.columns) > 3:
    col3 = df.columns[3]
else:
    col3 = df.columns[0]

counts3 = df[col3].value_counts().reset_index()
counts3.columns = [col3, "count"]

fig3, ax3 = plt.subplots()
ax3.scatter(range(len(counts3)), counts3["count"])

ax3.set_xlabel("Category Index")
ax3.set_ylabel("Count")
ax3.set_title(f"Distribution of {col3} Values (Scatter)")

plt.tight_layout()
fig3.savefig("scatter_plot.png")

# -----------------------------
# Show All Plots
# -----------------------------
plt.show()

print("Plots saved successfully:")
print(" - grouped_bar_plot.png")
print(" - horizontal_bar_plot.png")
print(" - scatter_plot.png")
