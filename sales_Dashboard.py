import pandas as pd
import matplotlib.pyplot as plt

# Realistic Sales Data
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Laptop"],
    "Sales": [50000, 2000, 3500, 15000, 60000]
}

# DataFrame Creation
df = pd.DataFrame(data)

# Total Sales
total_sales = df["Sales"].sum()

print("===== Sales Dashboard =====")
print("Total Sales:", total_sales, "BDT")

# Product Wise Sales
product_sales = df.groupby("Product")["Sales"].sum()

print("\nProduct Wise Sales:")
print(product_sales)

# Graph
product_sales.plot(kind="bar")

plt.title("Product Sales Report")
plt.xlabel("Product")
plt.ylabel("Sales (BDT)")

plt.show()