import matplotlib.pyplot as plt

# Sample monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_values = [50000, 60000, 75000, 80000, 90000, 100000]

# 1. Line plot of the monthly sales data
plt.figure(figsize=(8,6))
plt.plot(months, sales_values, marker='o', linestyle='-', color='b', label='Monthly Sales')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales Value')
plt.legend()
plt.grid(True)
plt.show()

# 2. Bar plot of the monthly sales data
plt.figure(figsize=(8, 6))
plt.bar(months, sales_values, color='r', align='center', alpha=0.7)
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales Value')
plt.grid(axis='y')
plt.show()
