import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [1000, 1200, 1500, 1300, 1600, 1800]

plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o', linestyle='-', color='b')
plt.title('Predicted Monthly Sales')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)


plt.figure(figsize=(8, 5))
plt.scatter(months, sales, color='r', marker='o')
plt.title('Predicted Monthly Sales')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)


plt.figure(figsize=(8, 5))
plt.bar(months, sales, color='g')
plt.title('Monthly Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
