import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load and preprocess the data
data = pd.read_csv('car_data.csv')  # Replace with your data source

# Selecting features and target
selected_features = ['engine_size', 'horsepower', 'fuel_efficiency']
X = data[selected_features]
y = data['price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Build the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"Root Mean Squared Error: {rmse}")
print(f"R-squared Score: {r2}")

# Analyze feature importance
coefficients = model.coef_
feature_importance = pd.Series(coefficients, index=selected_features)
feature_importance = feature_importance.abs().sort_values(ascending=False)

print("\nFeature Importance:")
print(feature_importance)

# Visualization
plt.bar(feature_importance.index, feature_importance)
plt.xlabel('Feature')
plt.ylabel('Absolute Coefficient Value')
plt.title('Feature Importance')
plt.xticks(rotation=45)
plt.show()
