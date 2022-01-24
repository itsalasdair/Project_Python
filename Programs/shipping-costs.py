# Codecademy Project to Calculate the costs of shipping based on weight

# float() to accept decimal input via commandline
weight = float(input("What does your package weigh?: ",))


# Ground Shipping
ground_flat_charge = 20.00

if weight <= 2:
  ground_cost = weight * 1.50
elif weight <= 6:
  ground_cost = weight * 3.00
elif weight <= 10:
  ground_cost = weight * 4.00
elif weight > 10:
  ground_cost = weight * 4.75
else:
  print("Mega!")

print("Ground Shipping: $", ground_cost + ground_flat_charge)


# Ground Shipping Premium
# Normal Ground Shipping + £125
ground_prem_flat_charge = 125.00

print("Ground Premium: $", ground_cost + ground_prem_flat_charge)


# Drone Shipping
if weight <= 2:
  drone_cost = weight * 4.50
elif weight <= 6:
  drone_cost = weight * 9.00
elif weight <=10:
  drone_cost = weight * 12.00
elif weight > 10:
  drone_cost = weight * 14.25
else:
  print("Mega!")

print("Drone Shipping: $", drone_cost)
