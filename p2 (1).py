import numpy as np

sales_data = np.array([
    [100.0, 150.0, 120.0],
    [80.0, 110.0, 90.0],
    [130.0, 100.0, 140.0],
    ])
c = np.mean(sales_data)
print("Average price of all products:", c)
