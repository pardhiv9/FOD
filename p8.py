import pandas as pd


data = {
    'Product': ['Product A', 'Product B', 'Product D', 'Product C', 'Product E', 'Product F', 'Product H', 'Product I'],
    'Quantity': [10, 15, 20, 5, 12, 18, 8, 14]
}


sales_data = pd.DataFrame(data)


product_group = sales_data.groupby('Product')['Quantity'].sum()


sorted_products = product_group.sort_values(ascending=False)


top_5_products = sorted_products.head(5)

print(top_5_products)

