#Sal's Shipping
"""This program will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:
 - Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
 - Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
 - Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
"""

weight = 41.5
flat_charge = 20.00
premium_groud_shipping = 125.00

#Ground Shipping
if weight <= 2:
  cost = (weight * 1.5) + flat_charge 
elif weight > 2 and weight <= 6:
  cost = (weight * 3) + flat_charge 
elif weight > 6 and weight <= 10:
  cost = (weight * 4) + flat_charge 
elif weight > 10:
  cost = (weight * 4.75) + flat_charge 
else:
  print("Please enter a valid weight")

print("Your ground shipping total is $" + (str("{:.2f}".format(cost))))

print("Premium Ground shipping is: $" + str("{:.2f}".format(premium_groud_shipping)) + " ...just FYI ;)")

#Drone Shipping
if weight <= 2:
  cost = (weight * 4.5)
elif weight > 2 and weight <= 6:
  cost = (weight * 9)
elif weight > 6 and weight <= 10:
  cost = (weight * 12)
elif weight > 10:
  cost = (weight * 14.25)
else:
  print("Please enter a valid weight")

print("Your drone shipping total is $" + (str("{:.2f}".format(cost))))
