#PROBLEM: GLOBAL FREIGHT CALCULATOR
#inputs
sender = input("Enter sender's name -> ")
item = input("Enter item type -> ")
is_Fragile = input("Is the item fragile? (True/False) -> ") == "True"
weight = float(input("Enter weight in kg -> "))
distance = float(input("Enter distance in km -> "))
is_Express = input("Is it express delivery? (True/False) -> ") == "True"
is_International = input("Is it international delivery? (True/False) -> ") == "True"

#base_cost
base_cost = ( weight * 2.50 ) + ( distance * 0.15 )

#total shipping costs
if weight <= 2.0 and distance <= 100.0 and not is_Express and not is_International:
    total_cost = 0.0
elif is_International and is_Express:
    total_cost = ( base_cost *  1.40 ) + 50
elif is_Express or (is_International and weight > 20 ):
    total_cost = ( base_cost * 1.20 ) + 25
elif weight > 30 or distance > 1000:
    total_cost = base_cost + 30
else:
    total_cost = base_cost

#prints
print("\n")
print("---SHIPPING DETAILS---")
print("Sender's Name: ", sender)
print("Item Type: ", item)
print("Total Shipping Cost: $", total_cost)         