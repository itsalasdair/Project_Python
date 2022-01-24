# Developed version of 'shipping-costs.py'


# To add:
# "Press Any Key to Close/Finish"


shipping_type = int(input("""Please enter your preferred shipping:
1.) Ground
2.) Ground Premium
3.) Drone
"""))

if shipping_type == 1:
    # Experimental: clear()
    ground_flat_charge = 20.00

    ground_weight = float(input("Please enter parcel weight: "))
    if ground_weight <= 2:
        ground_cost = ground_weight * 1.50
    elif ground_weight <= 6:
        ground_cost = ground_weight * 3.00
    elif ground_weight <= 10:
        ground_cost = ground_weight * 4.00
    elif ground_weight > 10:
        ground_cost = ground_weight * 4.75

    print("Ground Shipping Total: $", ground_cost + ground_flat_charge)


elif shipping_type == 2:

    ground_prem_flat_charge = 125.00

    ground_prem_weight = float(input("Please enter parcel weight: "))
    if ground_prem_weight <= 2:
        ground_prem_cost = ground_prem_weight * 1.50
    elif ground_prem_weight <= 6:
        ground_prem_cost = ground_prem_weight * 3.00
    elif ground_prem_weight <= 10:
        ground_prem_cost = ground_prem_weight * 4.00
    elif ground_prem_weight > 10:
        ground_prem_cost = ground_prem_weight * 4.75

    print("Ground Shipping Total: $", ground_prem_cost + ground_prem_flat_charge)


elif shipping_type == 3:

    drone_weight = float(input("Please enter parcel weight: "))
    if drone_weight <= 2:
        drone_cost = drone_weight * 4.50
    elif drone_weight <= 6:
        drone_cost = drone_weight * 9.00
    elif drone_weight <= 10:
        drone_cost = drone_weight * 12.00
    elif drone_weight > 10:
        drone_cost = drone_weight * 14.25

    print("Drone Shipping Total: $", drone_cost)

else:
    print("ERROR: Please enter 1, 2 or 3.")
