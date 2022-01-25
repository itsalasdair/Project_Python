# Codecademy Course - Len's slice


#toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", #"anchovies", "mushrooms"]
#prices = [2, 6, 1, 3, 2, 7, 2]
#
#num_two_dollar_slices = prices.count(2)
#num_pizzas = len(toppings)

#print(num_two_dollar_slices)
#print(num_pizzas)
#
#print("We sell",num_pizzas, "different kinds of pizza!")

###########################

# New 2D list

# Prices and Pizza Type
pizza_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
]

sorted_prices = pizza_and_prices.sort()

# Sort pizza_and_prices by lowest first
cheapest_pizza = pizza_and_prices[0]

# Get last (most expensive) pizza from pizza_and_prices
# priciest_pizza = pizza_and_prices[-1]
# ^ Anchovies removed from the menu

# Remove anchovies from the menu and get new most expensive
pizza_and_prices.pop()
priciest_pizza = pizza_and_prices[-1]

# 3 cheapest
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)

print(cheapest_pizza)
print()
print(priciest_pizza)
