import pandas as pd
import matplotlib.pyplot as plt
data = {
    "customer_id": [1, 2, 3, 4, 5],
    "customer_age": [25, 32, 28, 35, 22],
    "purchase_made": [True, True, False, True, False]
}
sales_data = pd.DataFrame(data)


purchased_customers = sales_data[sales_data["purchase_made"]]


age_distribution = purchased_customers["customer_age"].value_counts().sort_index()


print("Age Frequency Distribution:")
print(age_distribution)


plt.figure(figsize=(10, 6))
plt.bar(age_distribution.index, age_distribution.values)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Frequency Distribution of Purchased Customers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
