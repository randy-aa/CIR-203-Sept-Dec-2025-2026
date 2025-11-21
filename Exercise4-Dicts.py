inventory = {
    "Laptop": 15,
    "Phone": 8,
    "Tablet": 12,
    "Headphones": 25,
    "Charger": 5
}

inventory["Smartwatch"] = 10
inventory["Phone"] = 12

def low_stock(inv):
    return {k:v for k,v in inv.items() if v < 10}

del inventory["Charger"]

for product, qty in inventory.items():
    print(product, ":", qty)

print("Low stock products:", low_stock(inventory))
