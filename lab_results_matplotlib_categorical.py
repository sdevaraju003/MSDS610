import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Lab Results.csv")

print("Columns in dataset:")
print(df.columns.tolist())

# -----------------------------
# PLOT 1
# -----------------------------
col1 = df.columns[0]
counts1 = df[col1].value_counts().head(10)

fig1, ax1 = plt.subplots()
ax1.bar(counts1.index.astype(str), counts1.values)
ax1.set_xlabel(col1)
ax1.set_ylabel("Count")
ax1.set_title(f"Top 10 {col1} Values")
ax1.tick_params(axis="x", rotation=45)
plt.tight_layout()
fig1.savefig("plot1.png")   # ✅ SAVE IMAGE

# -----------------------------
# PLOT 2
# -----------------------------
col2 = df.columns[1]
counts2 = df[col2].value_counts().head(10)

fig2, ax2 = plt.subplots()
ax2.bar(counts2.index.astype(str), counts2.values)
ax2.set_xlabel(col2)
ax2.set_ylabel("Count")
ax2.set_title(f"Top 10 {col2} Values")
ax2.tick_params(axis="x", rotation=45)
plt.tight_layout()
fig2.savefig("plot2.png")   # ✅ SAVE IMAGE

# -----------------------------
# PLOT 3
# -----------------------------
col3 = df.columns[2]
counts3 = df[col3].value_counts().head(10)

fig3, ax3 = plt.subplots()
ax3.bar(counts3.index.astype(str), counts3.values)
ax3.set_xlabel(col3)
ax3.set_ylabel("Count")
ax3.set_title(f"Top 10 {col3} Values")
ax3.tick_params(axis="x", rotation=45)
plt.tight_layout()
fig3.savefig("plot3.png")   # ✅ SAVE IMAGE

plt.show()
