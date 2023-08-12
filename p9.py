import pandas as pd


data = {
    'Property ID': [1, 2, 3, 4, 5],
    'Location': ['City A', 'City B', 'City A', 'City C', 'City B'],
    'Number of Bedrooms': [3, 4, 2, 5, 3],
    'Area (sq ft)': [1500, 2000, 1200, 2500, 1800],
    'Listing Price': [250000, 350000, 180000, 500000, 300000]
}

property_data = pd.DataFrame(data)


average_price_by_location = property_data.groupby('Location')['Listing Price'].mean()
print("Average Listing Price by Location:")
print(average_price_by_location)

num_properties_with_more_than_four_bedrooms = (property_data['Number of Bedrooms'] > 4).sum()
print("Number of Properties with More Than Four Bedrooms:", num_properties_with_more_than_four_bedrooms)


property_with_largest_area = property_data[property_data['Area (sq ft)'] == property_data['Area (sq ft)'].max()]
print("Property with the Largest Area:",property_with_largest_area)

