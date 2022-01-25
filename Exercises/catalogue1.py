# Codecademy Project: Catalogue
# Program to store items and values in the store

# Alasdair Corton

# Setting products/descriptions and cost

lovely_loveseat_description = "- Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

stylish_settee_description = "- Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

luxurious_lamp_description = "- Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

# Sales Tax is 8.8%
sales_tax = 0.088

# Customer One values set to Nil until they purchase
customer_one_total = 0
customer_one_itemization = ""

# Adjusting Customer total
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price
customer_one_itemization += "\n" + luxurious_lamp_description

# Calculating sales tax on the total cost
customer_one_tax = customer_one_total * sales_tax

# Printing total/final costs
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)
