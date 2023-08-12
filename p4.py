import numpy as np
sales_data = np.array([50000, 60000, 75000, 90000])

total_sales_year = np.sum(sales_data)


first_quarter_sales = sales_data[0]
fourth_quarter_sales = sales_data[-1]
percentage_increase = ((fourth_quarter_sales - first_quarter_sales) / first_quarter_sales) * 100


print("Total sales for the year:", total_sales_year)
print("Percentage increase in sales from Q1 to Q4:", percentage_increase, "%")
