import matplotlib.pyplot as plt


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [20, 22, 25, 28, 30, 32, 34, 33, 30, 27, 24, 22]  
rainfall =[23,23,45,33,45,67,54,32,12,45,56,55]
plt.figure(figsize=(10, 6))
plt.plot(months, temperature, marker='o', linestyle='-', color='b')
plt.title('Monthly Temperature Data')
plt.xlabel('Months')
plt.ylabel('Temperature (°C)')
plt.grid(True)

plt.figure(figsize=(10, 6))
plt.scatter(months, rainfall, color='r', marker='o')
plt.title('Monthly Rainfall Data')
plt.xlabel('Months')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.show()
