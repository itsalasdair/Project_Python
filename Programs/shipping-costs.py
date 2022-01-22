# Codecademy Project to Calculate the costs of shipping based on weight


weight = 18
ground_flat = 20
ground_prem_flat = 125
drone_flat = 0


# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + ground_flat
elif weight <= 6:
  cost_ground = weight * 3.0 + ground_flat
elif weight <= 10:
  cost_ground = weight * 4.00 + ground_flat
else:
  cost_ground = weight * 4.75 + ground_flat
print("Ground Shipping: $", + cost_ground)

# Ground Shipping Premium
# Normal Ground Shipping + £125
ground_premium_cost = cost_ground + ground_prem_flat
print("Ground Shipping Premium: $", + ground_premium_cost)


# Drone Shipping
if weight <= 2:
  cost_air = weight * 4.50 + drone_flat
elif weight <= 6:
  cost_air = weight * 9.00 + drone_flat
elif weight <= 10:
  cost_air = weight * 12.00 + drone_flat
else:
  cost_air = weight * 14.25 + drone_flat
print("Drone Shipping: $", + cost_air)
