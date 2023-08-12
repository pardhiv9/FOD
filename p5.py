import numpy as np

num_car_models = int(input("Enter the number of car models: "))
fuel_efficiency = np.empty(num_car_models)

for i in range(num_car_models):
    fuel_efficiency[i] = float(input(f"Enter the fuel efficiency (miles per gallon) for Car Model {i+1}: "))

average_fuel_efficiency = np.mean(fuel_efficiency)

first_model_fuel_efficiency = fuel_efficiency[0]
last_model_fuel_efficiency = fuel_efficiency[-1]
percentage_improvement = ((last_model_fuel_efficiency - first_model_fuel_efficiency) / first_model_fuel_efficiency) * 100

print("Average fuel efficiency:", average_fuel_efficiency)
print("Percentage improvement in fuel efficiency between the first and last car models:", percentage_improvement, "%")
