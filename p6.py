
item_prices = [10, 20, 5, 8]  
quantities = [2, 3, 1, 4]     
discount_rate = 10           
tax_rate = 8                  


total_cost_before_discount = sum(price * quantity for price, quantity in zip(item_prices, quantities))


discount_amount = (discount_rate / 100) * total_cost_before_discount


cost_after_discount = total_cost_before_discount - discount_amount


tax_amount = (tax_rate / 100) * cost_after_discount


final_total_cost = cost_after_discount + tax_amount

print("Total cost before any discounts: $", total_cost_before_discount)
print("Discount amount: $", discount_amount)
print("Cost after applying discount: $", cost_after_discount)
print("Tax amount: $", tax_amount)
print("Final total cost after taxes: $", final_total_cost)
